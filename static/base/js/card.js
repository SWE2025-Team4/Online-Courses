
document.addEventListener("DOMContentLoaded", () => {
    const layers = document.querySelectorAll('.layer-up-1, .layer-up-2, .layer-down-1, .layer-down-2');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            } else {
                entry.target.classList.remove('animate'); // Optional: Remove class if you want to reset
            }
        });
    }, {
        threshold: 0.1
    });

    layers.forEach(layer => observer.observe(layer));
});


// Data for courses
const courses = [
    {
        videoSrc: "course-intro.mp4",
        courseName: "HTML & CSS Basics",
        instructor: "Eng / Mona Maher",
        rating: 4, // Number of stars
        reviews: 340,
        detailsLink: "courseDetails.html"
    },
    {
        videoSrc: "course-javascript.mp4",
        courseName: "JavaScript Basics",
        instructor: "Eng / Ahmed Ali",
        rating: 5,
        reviews: 120,
        detailsLink: "courseDetails.html"
    }
];

// Function to create and render course cards
function renderCourses(courses, repeatCount) {
    const container = document.getElementById("coursesContainer");

    for (let i = 0; i < repeatCount; i++) {
        courses.forEach(course => {
            // Create course card
            const courseCard = document.createElement("div");
            courseCard.className = "course-card";

            // Add video
            const video = document.createElement("video");
            video.src = course.videoSrc;
            video.className = "video-player-home";
            video.controls = true;

            // Add course name
            const courseName = document.createElement("h4");
            courseName.textContent = `Course Name: ${course.courseName}`;

            // Add instructor name
            const instructor = document.createElement("h5");
            instructor.textContent = `Instructor: ${course.instructor}`;

            // Add rating
            const ratingContainer = document.createElement("div");
            ratingContainer.className = "rating-container";

            for (let j = 0; j < 5; j++) {
                const star = document.createElement("span");
                star.className = j < course.rating ? "star1" : "star1 empty";
                star.innerHTML = "&#9733;";
                ratingContainer.appendChild(star);
            }

            const review = document.createElement("span");
            review.className = "review";
            review.textContent = `(${course.reviews} Reviews)`;
            ratingContainer.appendChild(review);

            // Add View Course button
            const buttonLink = document.createElement("a");
            buttonLink.href = course.detailsLink;

            const button = document.createElement("button");
            button.className = "btn spbtn";
            button.textContent = "View Course";
            buttonLink.appendChild(button);

            // Append all elements to the course card
            courseCard.appendChild(video);
            courseCard.appendChild(courseName);
            courseCard.appendChild(instructor);
            courseCard.appendChild(ratingContainer);
            courseCard.appendChild(buttonLink);

            // Append the course card to the container
            container.appendChild(courseCard);
        });
    }
}

// Call the function to render courses, repeating them twice
renderCourses(courses, 3);
