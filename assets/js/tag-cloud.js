// AI + 海洋数据同化论文库 - 标签云和作者筛选功能

(function() {
  'use strict';

  // Configuration
  var MAX_TAGS = 20;  // Top 20 tags by frequency
  var MAX_AUTHORS = 15;  // Top 15 authors by paper count

  // State
  var tagFrequencies = {};
  var authorCounts = {};
  var activeTag = null;
  var activeAuthor = null;

  // Initialize when DOM is ready
  document.addEventListener('DOMContentLoaded', init);

  function init() {
    // Wait for allPapers to be populated (search.js loads the data)
    waitForData();
  }

  function waitForData() {
    if (typeof allPapers !== 'undefined' && allPapers.length > 0) {
      processData();
      renderTagCloud();
      renderAuthorFilter();
      setupEventListeners();
    } else {
      // Retry after a short delay
      setTimeout(waitForData, 100);
    }
  }

  function processData() {
    // Count tag frequencies
    tagFrequencies = {};
    allPapers.forEach(function(paper) {
      // Method tags
      paper.method_tags.forEach(function(tag) {
        tagFrequencies[tag] = (tagFrequencies[tag] || 0) + 1;
      });
      // Application tags
      paper.application_tags.forEach(function(tag) {
        tagFrequencies[tag] = (tagFrequencies[tag] || 0) + 1;
      });
    });

    // Count author paper counts
    authorCounts = {};
    allPapers.forEach(function(paper) {
      paper.authors.forEach(function(author) {
        authorCounts[author] = (authorCounts[author] || 0) + 1;
      });
    });
  }

  function renderTagCloud() {
    var container = document.getElementById('tag-cloud');
    if (!container) return;

    // Sort tags by frequency
    var sortedTags = Object.keys(tagFrequencies).sort(function(a, b) {
      return tagFrequencies[b] - tagFrequencies[a];
    });

    // Take top N tags
    var topTags = sortedTags.slice(0, MAX_TAGS);

    // Calculate font sizes using log scale
    var maxFreq = Math.max.apply(null, Object.values(tagFrequencies));
    var minFreq = Math.min.apply(null, Object.values(tagFrequencies));

    // Create tag cloud HTML
    var html = topTags.map(function(tag) {
      var freq = tagFrequencies[tag];
      var size = calculateTagSize(freq, minFreq, maxFreq);
      var isActive = activeTag === tag;
      var activeClass = isActive ? ' active' : '';

      return '<span class="cloud-tag size-' + size + activeClass + '" ' +
             'data-tag="' + escapeHtml(tag) + '">' +
             escapeHtml(tag) + ' (' + freq + ')</span>';
    }).join('');

    container.innerHTML = html;
  }

  function calculateTagSize(freq, minFreq, maxFreq) {
    if (maxFreq === minFreq) return 3;
    // Normalize frequency to 1-5 range using log scale
    var logMin = Math.log(minFreq);
    var logMax = Math.log(maxFreq);
    var logFreq = Math.log(freq);
    var normalized = (logFreq - logMin) / (logMax - logMin);
    return Math.max(1, Math.min(5, Math.ceil(normalized * 5)));
  }

  function renderAuthorFilter() {
    var container = document.getElementById('author-select-container');
    if (!container) return;

    // Sort authors by paper count
    var sortedAuthors = Object.keys(authorCounts).sort(function(a, b) {
      return authorCounts[b] - authorCounts[a];
    });

    // Take top N authors
    var topAuthors = sortedAuthors.slice(0, MAX_AUTHORS);

    // Create select HTML
    var html = '<select class="author-select" id="author-select">';
    html += '<option value="">全部作者</option>';
    topAuthors.forEach(function(author) {
      var count = authorCounts[author];
      var selected = activeAuthor === author ? ' selected' : '';
      html += '<option value="' + escapeHtml(author) + '"' + selected + '>' +
              escapeHtml(author) + ' (' + count + ')</option>';
    });
    html += '</select>';

    container.innerHTML = html;

    // Add change listener
    var select = document.getElementById('author-select');
    if (select) {
      select.addEventListener('change', handleAuthorChange);
    }
  }

  function setupEventListeners() {
    // Event delegation for tag clicks
    document.addEventListener('click', function(e) {
      if (e.target.classList.contains('cloud-tag')) {
        handleTagClick(e.target);
      }
    });
  }

  function handleTagClick(element) {
    var tag = element.dataset.tag;

    // Toggle active state
    if (activeTag === tag) {
      activeTag = null;
      element.classList.remove('active');
    } else {
      // Remove active from all tags
      document.querySelectorAll('.cloud-tag').forEach(function(t) {
        t.classList.remove('active');
      });
      activeTag = tag;
      element.classList.add('active');
    }

    // Trigger filter update in search.js
    updateSearchFilters();
  }

  function handleAuthorChange(e) {
    var author = e.target.value;
    activeAuthor = author || null;
    updateSearchFilters();
  }

  function updateSearchFilters() {
    // Dispatch custom event for search.js to handle
    var event = new CustomEvent('tagcloud:filter', {
      detail: {
        tag: activeTag,
        author: activeAuthor
      }
    });
    document.dispatchEvent(event);
  }

  // Expose methods for external access
  window.tagCloud = {
    getActiveTag: function() { return activeTag; },
    getActiveAuthor: function() { return activeAuthor; },
    clearFilters: function() {
      activeTag = null;
      activeAuthor = null;
      document.querySelectorAll('.cloud-tag').forEach(function(t) {
        t.classList.remove('active');
      });
      var select = document.getElementById('author-select');
      if (select) select.value = '';
      updateSearchFilters();
    }
  };

  function escapeHtml(text) {
    var div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

})();
