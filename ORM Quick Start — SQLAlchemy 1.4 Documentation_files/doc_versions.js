

var doc_versions = [
  {
    "version": "Version 2.0 (beta)",
    "slug": "20"
    
  },
  {
    "version": "Version 1.4",
    "slug": "14"
    
  },
  {
    "version": "Version 1.3",
    "slug": "13"
    
  },
  {
    "version": "Version 1.2",
    "slug": "12"
    ,"latest_warning": true
  }
];

var _version_lookup = {};
for (var key in doc_versions) {
    version = doc_versions[key];
    _version_lookup[version.slug] = version;
}

function empty(selector) {
    var nodes = document.querySelectorAll(selector);
    for (var i = 0; i < nodes.length; i++) {
        nodes[i].textContent = '';
    }
}

function append(selector, to_append) {
    var nodes = document.querySelectorAll(selector);
    for (var i = 0; i < nodes.length; i++) {
        nodes[i].innerHTML += to_append
    }
}

function renderDocVersions() {

    empty('#version_menu,.version-listing');
    for (var key in doc_versions) {
        obj = doc_versions[key];
        current_url = docs_base + "/en/" + obj.slug + "/";
        append("#version_menu,.version-listing", '<li><a href="' + current_url + '">' + obj.version + '</a></li>');
    }
}

document.addEventListener("DOMContentLoaded", function() { 
  renderDocVersions();
});
