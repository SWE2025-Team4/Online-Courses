// Select the main video player and playlist items
const mainVideo = document.getElementById('main-video');
const playlistItems = document.querySelectorAll('.playlist-item');

// Add click event to each playlist item
playlistItems.forEach(item => {
            console.log('playlistItems111111111111')

    item.addEventListener('click', () => {
        // Get the video source from the data attribute
        const videoSource = item.getAttribute('data-video');

        // Update the main video player's source
        mainVideo.src = videoSource;

        // Automatically play the selected video
        mainVideo.play();

        // Highlight the selected item
        playlistItems.forEach(i => i.classList.remove('active'));
        item.classList.add('active');
    });
});

 document.addEventListener('DOMContentLoaded', () => {
        const mainVideo = document.getElementById('main-video');
        const mainVideoSource = document.getElementById('main-video-source');
        const playlistItems = document.querySelectorAll('.playlist-item');
        console.log('playlistItems')
        // Set the first video as the source on load
        const firstVideo = document.querySelector('.playlist-item');
        if (firstVideo) {
            const firstVideoUrl = firstVideo.getAttribute('data-video');
            mainVideoSource.src = firstVideoUrl;
            mainVideo.load();
        }

        // Update the main video player when clicking a playlist item
        playlistItems.forEach(item => {
            item.addEventListener('click', () => {
                const videoUrl = item.getAttribute('data-video');
                mainVideoSource.src = videoUrl;
                mainVideo.load();
                mainVideo.play();

                // Highlight the active playlist item
                playlistItems.forEach(i => i.classList.remove('active'));
                item.classList.add('active');
            });
        });
    });