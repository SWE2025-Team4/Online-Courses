// Define the courses in an array of objects, including video link and instructor's name
alert("This is an alert message base catalog!");
console.log("Hello from catalog.js!");

const courses = {
    "Frontend Development": [
        {
            title: "HTML & CSS Mastery",
            description: "Learn the foundations of web development with HTML and CSS.",
            buttonText: "Enroll Now",
            videoLink: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  // Add a video link
            instructor: "John Doe"  // Add instructor's name
        },
        {
            title: "JavaScript for Beginners",
            description: "Start your JavaScript journey with this beginner-friendly course.",
            buttonText: "Enroll Now",
            videoLink: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  // Add a video link
            instructor: "Jane Smith"  // Add instructor's name
        }
    ],
    "Backend Development": [
        {
            title: "Node.js for Beginners",
            description: "Master backend development with Node.js and Express.",
            buttonText: "Enroll Now",
            videoLink: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  // Add a video link
            instructor: "Alice Johnson"  // Add instructor's name
        }
    ],
    "Data Science": [
        {
            title: "Introduction to Data Science",
            description: "Learn the basics of data science and analysis with Python.",
            buttonText: "Enroll Now",
            videoLink: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  // Add a video link
            instructor: "David Lee"  // Add instructor's name
        }
    ],
    "Artificial Intelligence": [
        {
            title: "AI for Everyone",
            description: "Get introduced to artificial intelligence concepts and applications.",
            buttonText: "Enroll Now",
            videoLink: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  // Add a video link
            instructor: "Emma Wang"  // Add instructor's name
        }
    ],
    "UI/UX Design": [
        {
            title: "UI/UX Design Fundamentals",
            description: "Understand the core principles of UI/UX design for building user-friendly interfaces.",
            buttonText: "Enroll Now",
            videoLink: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  // Add a video link
            instructor: "Michael Brown"  // Add instructor's name
        }
    ],
};

// Function to populate categories
function populateCategories() {
    const categoryList = document.getElementById('category-list');
    for (const category in courses) {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<a href="#${category.replace(/\s+/g, '-').toLowerCase()}">${category}</a>`;
        categoryList.appendChild(listItem);
    }
}

// Function to populate courses for each category
function populateCourses() {
    const courseContainer = document.getElementById('course-container');
    for (const category in courses) {
        // Create a section for each category
        const section = document.createElement('div');
        section.id = category.replace(/\s+/g, '-').toLowerCase(); // Unique ID for each category section
        section.classList.add('course-category');

        // Category title
        const title = document.createElement('h3');
        title.innerText = category;
        section.appendChild(title);

        // Create course list
        const courseList = document.createElement('div');
        courseList.classList.add('course-list');

        // Loop through courses and create course items
        courses[category].forEach(course => {
            const courseItem = document.createElement('div');
            courseItem.classList.add('course');

            // Course title
            const courseTitle = document.createElement('h4');
            courseTitle.innerText = course.title;
            courseItem.appendChild(courseTitle);

            // Course description
            const courseDescription = document.createElement('p');
            courseDescription.innerText = course.description;
            courseItem.appendChild(courseDescription);


            // Instructor Name
            const instructorName = document.createElement('p');
            instructorName.classList.add('instructor');
            instructorName.innerText = `Instructor: ${course.instructor}`;
            courseItem.appendChild(instructorName);

            // Video Link
            const videoLink = document.createElement('a');
            videoLink.classList.add('video-link');
            videoLink.href = course.videoLink;
            videoLink.innerText = "Watch Introduction Video";
            videoLink.target = "_blank";  // Opens video in a new tab
            courseItem.appendChild(videoLink);

            // Enroll button
            const enrollButton = document.createElement('button');
            enrollButton.classList.add('enroll-btn');
            enrollButton.innerText = course.buttonText;
            courseItem.appendChild(enrollButton);

            // Append the course item to the course list
            courseList.appendChild(courseItem);
        });

        // Append the course list to the section
        section.appendChild(courseList);

        // Append the section to the course container
        courseContainer.appendChild(section);
    }
}


// Initialize the catalog
function initCatalog() {
    populateCategories();
    populateCourses();
}

// Call the function to populate the catalog when the page loads
//window.onload = function() {
//    initCatalog();
//    loadContent('header', 'header.html');
//    loadContent('footer', 'footer.html');
//};
