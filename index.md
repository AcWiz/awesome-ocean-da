---
layout: default
title: AI + 海洋数据同化论文库
---

<!-- Hero Section -->
<section class="hero">
  <h1>🤖 AI + 🌊 海洋数据同化论文库</h1>
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
  <div class="filter-buttons">
    <span class="filter-label">方法:</span>
    <button class="filter-btn active" data-filter="all" data-type="method">全部</button>
    <button class="filter-btn" data-filter="PINN" data-type="method">PINN</button>
    <button class="filter-btn" data-filter="Koopman" data-type="method">Koopman</button>
    <button class="filter-btn" data-filter="Neural-Operator" data-type="method">神经算子</button>
    <button class="filter-btn" data-filter="GNN" data-type="method">GNN</button>
    <button class="filter-btn" data-filter="EnKF" data-type="method">EnKF</button>
    <button class="filter-btn" data-filter="4D-Var" data-type="method">4D-Var</button>
  </div>
  <div class="filter-buttons">
    <span class="filter-label">应用:</span>
    <button class="filter-btn active" data-filter="all" data-type="application">全部</button>
    <button class="filter-btn" data-filter="Global-Forecast" data-type="application">全球预报</button>
    <button class="filter-btn" data-filter="Regional-Forecast" data-type="application">区域预报</button>
    <button class="filter-btn" data-filter="SST" data-type="application">SST</button>
    <button class="filter-btn" data-filter="ENSO" data-type="application">ENSO</button>
    <button class="filter-btn" data-filter="Deep-Ocean" data-type="application">深海</button>
  </div>
  <div class="filter-buttons" id="year-filters">
    <span class="filter-label">年份:</span>
    <!-- Year buttons populated by JS -->
  </div>
</section>

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
    })
    .catch(error => {
      console.error('Error loading papers:', error);
      document.getElementById('papers-grid').innerHTML =
        '<p class="error">加载论文数据失败，请稍后重试。</p>';
    });
</script>
