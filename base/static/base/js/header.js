//footer and header calling back
function loadContent(elementId, filePath) {
    fetch(filePath)
        .then(response => response.text())
        .then(data => {
            document.getElementById(elementId).innerHTML = data;
        })
        .catch(error => console.error('Error loading content:', error));
}

window.onload = function() {
    loadContent('header', 'header.html');
    loadContent('footer', 'footer.html');
};

function userIcon() {
    const userDiv = document.getElementById('user-div');
    if (userDiv) {
        // Toggle visibility of the user div
        userDiv.style.display = (userDiv.style.display === 'none' || userDiv.style.display === '') ? 'flex' : 'none';
    } else {
        console.error('User div element not found.');
    }
};

// Get the current page from the URL
const currentPage = window.location.pathname.split("/").pop(); // Extract the current file name

// Select all navigation links
const navLinks = document.querySelectorAll(".nav-links a");

// Loop through each navigation link
navLinks.forEach(link => {
    const linkPage = link.getAttribute("href"); // Get the 'href' attribute of the link

    // If the link's href matches the current page, add the active class
    if (currentPage === linkPage) {
        link.classList.add("active-link");
    }
});

