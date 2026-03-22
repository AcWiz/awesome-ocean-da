// AI + 海洋数据同化论文库 - 搜索和过滤功能

(function() {
  'use strict';

  let currentMethodFilter = 'all';
  let currentApplicationFilter = 'all';
  let currentYearFilter = 'all';
  let searchQuery = '';
  let allPapers = [];

  // Initialize when DOM is ready
  document.addEventListener('DOMContentLoaded', init);

  function init() {
    setupEventListeners();
    updateLastUpdated();
  }

  function setupEventListeners() {
    // Search input
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
      searchInput.addEventListener('input', debounce(handleSearch, 300));
    }

    // Event delegation for filter buttons (handles dynamically added year buttons)
    document.addEventListener('click', (e) => {
      if (e.target.classList.contains('filter-btn')) {
        handleFilterClick(e);
      }
    });

    // Modal close
    const modal = document.getElementById('paper-modal');
    const closeBtn = document.querySelector('.close');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => modal.style.display = 'none');
    }
    if (modal) {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) modal.style.display = 'none';
      });
    }
  }

  function debounce(func, wait) {
    let timeout;
    return function(...args) {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  }

  function handleSearch(e) {
    searchQuery = e.target.value.toLowerCase().trim();
    renderFilteredPapers();
  }

  function handleFilterClick(e) {
    const btn = e.target;
    const filterType = btn.dataset.type;
    const filterValue = btn.dataset.filter;

    // Update active state
    document.querySelectorAll(`.filter-btn[data-type="${filterType}"]`).forEach(b => {
      b.classList.remove('active');
    });
    btn.classList.add('active');

    // Update filter
    if (filterType === 'method') {
      currentMethodFilter = filterValue;
    } else if (filterType === 'application') {
      currentApplicationFilter = filterValue;
    } else if (filterType === 'year') {
      currentYearFilter = filterValue;
    }

    renderFilteredPapers();
  }

  function renderFilteredPapers() {
    const filtered = allPapers.filter(paper => {
      // Search filter - enhanced to include tags and abstract_preview
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const titleMatch = paper.title.toLowerCase().includes(q);
        const authorMatch = paper.authors.some(a => a.toLowerCase().includes(q));
        const methodMatch = paper.method_tags.some(t => t.toLowerCase().includes(q));
        const appMatch = paper.application_tags.some(t => t.toLowerCase().includes(q));
        const abstractMatch = (paper.abstract_preview || '').toLowerCase().includes(q);
        if (!titleMatch && !authorMatch && !methodMatch && !appMatch && !abstractMatch) return false;
      }

      // Method filter
      if (currentMethodFilter !== 'all') {
        if (!paper.method_tags.includes(currentMethodFilter)) return false;
      }

      // Application filter
      if (currentApplicationFilter !== 'all') {
        if (!paper.application_tags.includes(currentApplicationFilter)) return false;
      }

      // Year filter
      if (currentYearFilter !== 'all') {
        if (String(paper.year) !== currentYearFilter) return false;
      }

      return true;
    });

    // Sort: year descending, then alphabetical
    filtered.sort((a, b) => {
      if (b.year !== a.year) return b.year - a.year;
      return a.title.localeCompare(b.title);
    });

    renderPapers(filtered);
  }

  function renderPapers(papers) {
    const grid = document.getElementById('papers-grid');
    const noResults = document.getElementById('no-results');

    if (!grid) return;

    if (papers.length === 0) {
      grid.innerHTML = '';
      noResults.style.display = 'block';
      noResults.querySelector('p').textContent =
        '没有找到匹配的论文。尝试使用更通用的关键词。';
      return;
    }

    noResults.style.display = 'none';

    grid.innerHTML = papers.map(paper => {
      const venueBadge = paper.venue && paper.venue !== ''
        ? `<span class="paper-venue-badge" title="正式发表">${escapeHtml(paper.venue)}</span>`
        : (paper.source === 'arXiv' ? `<span class="paper-arxiv-badge" title="arXiv预印本">arXiv</span>` : '');

      const difficultyStars = paper.difficulty || '';
      const importanceStars = paper.importance || '';
      const readStatusBadge = paper.read_status
        ? `<span class="paper-status-badge status-${paper.read_status}" title="阅读状态">${paper.read_status === 'deep_read' ? '精读' : '泛读'}</span>`
        : '';

      return `
      <div class="paper-card" data-id="${paper.arxiv || paper.title}">
        <div class="paper-header">
          <h3 class="paper-title">${escapeHtml(paper.title)}</h3>
          <div class="paper-meta-badges">
            ${venueBadge}
            <span class="paper-year">${paper.year}</span>
            ${readStatusBadge}
          </div>
        </div>
        <div class="paper-authors">
          ${paper.authors.slice(0, 3).join(', ')}${paper.authors.length > 3 ? ' et al.' : ''}
        </div>
        <div class="paper-tags">
          ${paper.method_tags.map(tag => `<span class="tag method-tag">${tag}</span>`).join('')}
          ${paper.application_tags.map(tag => `<span class="tag application-tag">${tag}</span>`).join('')}
        </div>
        ${(difficultyStars || importanceStars) ? `
        <div class="paper-ratings">
          ${difficultyStars ? `<span class="rating" title="难度">${difficultyStars}</span>` : ''}
          ${importanceStars ? `<span class="rating" title="重要度">${importanceStars}</span>` : ''}
        </div>` : ''}
        <div class="paper-actions">
          ${paper.paper_url ? `<a href="${paper.paper_url}" target="_blank" class="btn btn-primary">arXiv</a>` : ''}
          <a href="${paper.path}/" class="btn btn-secondary">详情</a>
        </div>
      </div>
    `}).join('');

    // Add click handlers for cards
    grid.querySelectorAll('.paper-card').forEach(card => {
      card.addEventListener('click', (e) => {
        if (e.target.tagName !== 'A') {
          const title = card.querySelector('.paper-title').textContent;
          showPaperDetail(title);
        }
      });
    });
  }

  function showPaperDetail(title) {
    const paper = allPapers.find(p => p.title === title);
    if (!paper) return;

    const modal = document.getElementById('paper-modal');
    const body = document.getElementById('modal-body');

    const venueDisplay = paper.venue && paper.venue !== ''
      ? `<span class="paper-venue-badge">${escapeHtml(paper.venue)}</span>`
      : (paper.source === 'arXiv' ? `<span class="paper-arxiv-badge">arXiv 预印本</span>` : `<span>${paper.source}</span>`);

    body.innerHTML = `
      <h2>${escapeHtml(paper.title)}</h2>
      <p><strong>作者:</strong> ${paper.authors.join(', ')}</p>
      <p><strong>年份:</strong> ${paper.year}</p>
      <p><strong>发表:</strong> ${venueDisplay}</p>
      ${paper.doi ? `<p><strong>DOI:</strong> <a href="https://doi.org/${paper.doi}" target="_blank">${paper.doi}</a></p>` : ''}
      <div class="paper-tags">
        ${paper.method_tags.map(tag => `<span class="tag method-tag">${tag}</span>`).join('')}
        ${paper.application_tags.map(tag => `<span class="tag application-tag">${tag}</span>`).join('')}
      </div>
      ${(paper.difficulty || paper.importance || paper.read_status) ? `
      <div class="paper-meta-row">
        ${paper.difficulty ? `<span class="meta-item"><strong>难度:</strong> ${paper.difficulty}</span>` : ''}
        ${paper.importance ? `<span class="meta-item"><strong>重要度:</strong> ${paper.importance}</span>` : ''}
        ${paper.read_status ? `<span class="meta-item"><strong>状态:</strong> ${paper.read_status === 'deep_read' ? '精读' : '泛读'}</span>` : ''}
      </div>` : ''}
      <hr style="margin: 1rem 0; border: none; border-top: 1px solid #eee;">
      <p>${escapeHtml(paper.abstract_preview || '')}</p>
      <div style="margin-top: 1rem;">
        ${paper.paper_url ? `<a href="${paper.paper_url}" target="_blank" class="btn btn-primary">查看原文</a>` : ''}
      </div>
    `;

    modal.style.display = 'block';
  }

  function updateStats(stats) {
    if (!stats) return;

    const totalEl = document.getElementById('total-papers');
    const yearsEl = document.getElementById('total-years');

    if (totalEl) totalEl.textContent = stats.total || 0;
    if (yearsEl) yearsEl.textContent = Object.keys(stats.by_year || {}).length || 0;
  }

  function updateLastUpdated() {
    const el = document.getElementById('last-updated');
    if (el && window.papersStats) {
      // This will be set when data loads
    }
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Expose renderPapers for external use
  window.renderPapers = renderPapers;

})();
