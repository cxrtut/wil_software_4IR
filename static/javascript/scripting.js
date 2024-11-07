// Loader 
document.addEventListener("DOMContentLoaded", function () {
    const loader = document.getElementById("loader");

    function showLoader() {
        loader.classList.add('show');
    }

    function hideLoader() {
        loader.classList.remove('show');
    }

    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function (e) {
            showLoader();
        });
    });

    window.addEventListener('load', hideLoader);

    document.addEventListener('visibilitychange', function () {
        if (document.visibilityState === 'visible') {
            hideLoader();
        }
    });
});

// Back button 
function goBack() {
    window.history.back();
}

// Toggle FAQ answers
document.querySelectorAll('.faq-item h2.question').forEach(question => {
    question.addEventListener('click', () => {
        const answer = question.nextElementSibling;
        answer.style.display = answer.style.display === 'none' ? 'block' : 'none';
    });
});

// The collapsing and showing of the nav bar in profile.html
function toggleCollapse() {
    const options = document.getElementById('navbarOptions');
    options.classList.toggle('show');
}

// The collapsing of the nav items
// Profile content
function toggleProfile() {
    const profile = document.getElementById('profile');
    const track = document.getElementById('track');
    const history = document.getElementById('history');
    const ori_content = document.getElementById('ori_content');

    if (profile.style.display === 'none') {
        profile.style.display = 'block';
        ori_content.style.display = 'none';
        track.style.display = 'none';
        history.style.display = 'none';
    } else {
        profile.style.display = 'none';
        ori_content.style.display = 'block';
    }
}

// Track content
function toggleTrack() {
    const profile = document.getElementById('profile');
    const track = document.getElementById('track');
    const history = document.getElementById('history');
    const ori_content = document.getElementById('ori_content');

    if (track.style.display === 'none') {
        track.style.display = 'block';
        ori_content.style.display = 'none';
    } else {
        track.style.display = 'none';
        ori_content.style.display = 'block';
    }
}

// History content
function toggleHistory() {
    const profile = document.getElementById('profile');
    const track = document.getElementById('track');
    const history = document.getElementById('history');
    const ori_content = document.getElementById('ori_content');

    if (history.style.display === 'none') {
        history.style.display = 'block';
        ori_content.style.display = 'none';
    } else {
        history.style.display = 'none';
        ori_content.style.display = 'block';
    }
}
