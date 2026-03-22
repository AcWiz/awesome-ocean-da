---
layout: default
title: AI + 海洋数据同化论文库
---

<!-- Hero Section -->
<section class="hero">
  <h1>AI + 海洋数据同化论文库</h1>
  <p>收集整理 AI/深度学习 + 海洋数据同化、预报相关的学术论文</p>

  <div class="stats">
    <div class="stat">
      <span class="stat-number" id="total-papers">--</span>
      <span class="stat-label">论文总数</span>
    </div>
    <div class="stat">
      <span class="stat-number" id="total-years">--</span>
      <span class="stat-label">覆盖年份</span>
    </div>
  </div>
</section>

<!-- Search Section -->
<section class="search-section">
  <input type="text" id="search-input" placeholder="搜索论文标题、作者、摘要..." />
  <div class="filter-row">
    <span class="filter-label">方法:</span>
    <button class="filter-btn active" data-filter="all" data-type="method">全部</button>
    <button class="filter-btn" data-filter="PINN" data-type="method">PINN</button>
    <button class="filter-btn" data-filter="Koopman" data-type="method">Koopman</button>
    <button class="filter-btn" data-filter="Neural-Operator" data-type="method">神经算子</button>
    <button class="filter-btn" data-filter="GNN" data-type="method">GNN</button>
    <button class="filter-btn" data-filter="EnKF" data-type="method">EnKF</button>
    <button class="filter-btn" data-filter="4D-Var" data-type="method">4D-Var</button>
    <div class="sort-controls">
      <select id="sort-select" class="sort-select">
        <option value="year-desc">按年份 (最新)</option>
        <option value="year-asc">按年份 (最早)</option>
        <option value="importance">按重要度</option>
      </select>
    </div>
  </div>
  <div class="filter-row">
    <span class="filter-label">应用:</span>
    <button class="filter-btn active" data-filter="all" data-type="application">全部</button>
    <button class="filter-btn" data-filter="Global-Forecast" data-type="application">全球预报</button>
    <button class="filter-btn" data-filter="Regional-Forecast" data-type="application">区域预报</button>
    <button class="filter-btn" data-filter="SST" data-type="application">SST</button>
    <button class="filter-btn" data-filter="ENSO" data-type="application">ENSO</button>
    <button class="filter-btn" data-filter="Deep-Ocean" data-type="application">深海</button>
  </div>
  <div class="filter-row" id="year-filters">
    <span class="filter-label">年份:</span>
    <!-- Year buttons populated by JS -->
  </div>
</section>

<!-- Tag Cloud Section -->
<section class="tag-cloud-section">
  <h3 class="section-title">
    <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
      <path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 7C4.67 7 4 6.33 4 5.5S4.67 4 5.5 4 7 4.67 7 5.5 6.33 7 5.5 7z"/>
    </svg>
    热门标签
  </h3>
  <div id="tag-cloud" class="tag-cloud">
    <!-- Tags populated by tag-cloud.js -->
  </div>
</section>

<!-- Author Filter Section -->
<section class="author-filter-section">
  <h3 class="section-title">
    <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
      <path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/>
    </svg>
    作者筛选
  </h3>
  <div id="author-select-container">
    <!-- Author select populated by tag-cloud.js -->
  </div>
</section>

<!-- Result Count -->
<div id="result-count" class="result-count">
  加载中...
</div>

<!-- Papers Grid -->
<section class="papers-section">
  <div id="papers-grid" class="papers-grid">
    <!-- Papers will be loaded here via JavaScript -->
  </div>
  <div id="no-results" class="no-results" style="display: none;">
    <p>没有找到匹配的论文</p>
  </div>
</section>

<!-- Paper Modal -->
<div id="paper-modal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <div id="modal-body"></div>
  </div>
</div>

<!-- Load paper data -->
<script>
  // Load papers.json
  fetch('{{ "/_data/papers.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      window.papersData = data.papers;
      window.papersStats = data.statistics;
      allPapers = data.papers;

      // Populate year filter buttons dynamically
      const years = Object.keys(data.statistics.by_year || {}).sort((a, b) => b - a);
      const yearFilterContainer = document.getElementById('year-filters');
      if (yearFilterContainer && years.length > 0) {
        let html = '<span class="filter-label">年份:</span>';
        html += '<button class="filter-btn active" data-filter="all" data-type="year">全部</button>';
        years.forEach(year => {
          html += `<button class="filter-btn" data-filter="${year}" data-type="year">${year}</button>`;
        });
        yearFilterContainer.innerHTML = html;
        // Re-attach event listeners for new buttons
        document.querySelectorAll('#year-filters .filter-btn').forEach(btn => {
          btn.addEventListener('click', handleFilterClick);
        });
      }

      renderPapers(data.papers);
      updateStats(data.statistics);
      updateResultCount(data.papers.length, data.papers.length);
    })
    .catch(error => {
      console.error('Error loading papers:', error);
      document.getElementById('papers-grid').innerHTML =
        '<p class="error">加载论文数据失败，请稍后重试。</p>';
    });
</script>
