//footer and header calling back
function loadContent(elementId, filePath) {
    fetch(filePath)
        .then(response => response.text())
        .then(data => {
            document.getElementById(elementId).innerHTML = data;
        })
        .catch(error => console.error('Error loading content:', error));
}


//window.onload = function() {
//    loadContent('header', 'header.html');
//    loadContent('footer', 'footer.html');
//};

function searchIcon() {
    const searchBar = document.getElementById('search-bar');
    if (searchBar) {
        searchBar.classList.toggle('show');
    } else {
        console.error('Search bar element not found. Check the ID.');
    }
};

function userIcon() {
    const userDiv = document.getElementById('user-div');
    if (userDiv) {
        // Toggle visibility of the user div
        userDiv.style.display = (userDiv.style.display === 'none' || userDiv.style.display === '') ? 'flex' : 'none';
    } else {
        console.error('User div element not found.');
    }
}
