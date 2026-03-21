// AI + 海洋数据同化论文库 - 搜索和过滤功能

(function() {
  'use strict';

  let currentMethodFilter = 'all';
  let currentApplicationFilter = 'all';
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

    // Filter buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
      btn.addEventListener('click', handleFilterClick);
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
    } else {
      currentApplicationFilter = filterValue;
    }

    renderFilteredPapers();
  }

  function renderFilteredPapers() {
    const filtered = allPapers.filter(paper => {
      // Search filter
      if (searchQuery) {
        const titleMatch = paper.title.toLowerCase().includes(searchQuery);
        const authorMatch = paper.authors.some(a => a.toLowerCase().includes(searchQuery));
        if (!titleMatch && !authorMatch) return false;
      }

      // Method filter
      if (currentMethodFilter !== 'all') {
        if (!paper.method_tags.includes(currentMethodFilter)) return false;
      }

      // Application filter
      if (currentApplicationFilter !== 'all') {
        if (!paper.application_tags.includes(currentApplicationFilter)) return false;
      }

      return true;
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
      return;
    }

    noResults.style.display = 'none';

    grid.innerHTML = papers.map(paper => `
      <div class="paper-card" data-id="${paper.arxiv || paper.title}">
        <div class="paper-header">
          <h3 class="paper-title">${escapeHtml(paper.title)}</h3>
          <span class="paper-year">${paper.year}</span>
        </div>
        <div class="paper-authors">
          ${paper.authors.slice(0, 3).join(', ')}${paper.authors.length > 3 ? ' et al.' : ''}
        </div>
        <div class="paper-tags">
          ${paper.method_tags.map(tag => `<span class="tag method-tag">${tag}</span>`).join('')}
          ${paper.application_tags.map(tag => `<span class="tag application-tag">${tag}</span>`).join('')}
        </div>
        <div class="paper-actions">
          ${paper.paper_url ? `<a href="${paper.paper_url}" target="_blank" class="btn btn-primary">arXiv</a>` : ''}
          <a href="${paper.path}/" class="btn btn-secondary">详情</a>
        </div>
      </div>
    `).join('');

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

    body.innerHTML = `
      <h2>${escapeHtml(paper.title)}</h2>
      <p><strong>作者:</strong> ${paper.authors.join(', ')}</p>
      <p><strong>年份:</strong> ${paper.year}</p>
      <p><strong>来源:</strong> ${paper.source}${paper.venue ? ` - ${paper.venue}` : ''}</p>
      <div class="paper-tags">
        ${paper.method_tags.map(tag => `<span class="tag method-tag">${tag}</span>`).join('')}
        ${paper.application_tags.map(tag => `<span class="tag application-tag">${tag}</span>`).join('')}
      </div>
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
