// Event listeners for toggling forms
document.getElementById('login-btn').addEventListener('click', () => {
    document.getElementById('login-form').classList.remove('hidden');
    document.getElementById('signup-form').classList.add('hidden');
    document.getElementById('login-btn').classList.add('active');
    document.getElementById('signup-btn').classList.remove('active');
});

document.getElementById('signup-btn').addEventListener('click', () => {
    document.getElementById('signup-form').classList.remove('hidden');
    document.getElementById('login-form').classList.add('hidden');
    document.getElementById('signup-btn').classList.add('active');
    document.getElementById('login-btn').classList.remove('active');
});

// Login Functionality
function login(event) {
    event.preventDefault(); // Prevent default form submission

    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    // Simple validation (can be extended as needed)
    if (!email || !password) {
        alert("Please enter your email and password.");
        return;
    }

    // Save login information to localStorage
    localStorage.setItem('email', email);
    localStorage.setItem('password', password);

    // Redirect to Person Information page
    window.location.href = 'index.html';
}

// Signup Functionality
function signup(event) {
    event.preventDefault(); // Prevent default form submission

    const name = document.getElementById('signup-name').value;
    const email = document.getElementById('signup-email').value;
    const phone = document.getElementById('signup-phone').value;
    const password = document.getElementById('signup-password').value;
    const confirmPassword = document.getElementById('signup-confirm-password').value;

    // Simple validation (can be extended as needed)
    if (!name || !email || !phone || !password || password !== confirmPassword) {
        alert("Please fill in all fields correctly.");
        return;
    }

    // Save signup information to localStorage
    localStorage.setItem('name', name);
    localStorage.setItem('email', email);
    localStorage.setItem('phone', phone);
    localStorage.setItem('password', password);

    // Redirect to Person Information page
    window.location.href = 'index.html';
};

