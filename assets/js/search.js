
document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById("search-input");
  const searchResults = document.getElementById("search-results");
  let searchData = [];

  if (!searchInput || !searchResults) return;

  fetch("/index.json")
    .then(res => res.json())
    .then(data => { searchData = data; })
    .catch(err => console.error("Error loading search index:", err));

  searchInput.addEventListener("input", function() {
    const query = this.value.trim().toLowerCase();
    if (query.length < 1) {
      searchResults.style.display = "none";
      searchResults.innerHTML = "";
      return;
    }

    const matches = searchData.filter(item => {
      return (item.title && item.title.toLowerCase().includes(query)) ||
             (item.summary && item.summary.toLowerCase().includes(query)) ||
             (item.contents && item.contents.toLowerCase().includes(query));
    }).slice(0, 8);

    if (matches.length > 0) {
      searchResults.innerHTML = matches.map(m => `
        <a href="${m.permalink}">
          <strong>${m.title}</strong>
          <div style="font-size:0.75rem; color:#94a3b8; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${m.summary || ''}</div>
        </a>
      `).join('');
      searchResults.style.display = "block";
    } else {
      searchResults.innerHTML = `<div style="padding:10px; font-size:0.85rem; color:#94a3b8;">未找到匹配文章</div>`;
      searchResults.style.display = "block";
    }
  });

  document.addEventListener("click", function(e) {
    if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
      searchResults.style.display = "none";
    }
  });
});
