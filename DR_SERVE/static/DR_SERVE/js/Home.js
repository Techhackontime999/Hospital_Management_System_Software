// javascript for DR_SERVE Home page

// Navbar dropdown start
// this is navbar dropdown 1
// JavaScript for dropdown functionality
document.getElementById('dropdownDividerButton1').addEventListener('click', function () {
    const dropdown = document.getElementById('dropdownDivider1');
    dropdown.classList.toggle('hidden');
});

// Optional: Close dropdown when clicking outside of it
window.addEventListener('click', function (event) {
    const dropdown = document.getElementById('dropdownDivider1');
    if (!dropdown.contains(event.target) && event.target !== dropdownDividerButton1) {
        dropdown.classList.add('hidden');
    }
});



// this is navbar dropdown 2
// JavaScript for dropdown functionality
document.getElementById('dropdownDividerButton2').addEventListener('click', function () {
    const dropdown = document.getElementById('dropdownDivider2');
    dropdown.classList.toggle('hidden');
});

// Optional: Close dropdown when clicking outside of it
window.addEventListener('click', function (event) {
    const dropdown = document.getElementById('dropdownDivider2');
    if (!dropdown.contains(event.target) && event.target !== dropdownDividerButton2) {
        dropdown.classList.add('hidden');
    }
});

// this is navbar dropdown 3
// JavaScript for dropdown functionality
document.getElementById('dropdownDividerButton3').addEventListener('click', function () {
    const dropdown = document.getElementById('dropdownDivider3');
    dropdown.classList.toggle('hidden');
});

// Optional: Close dropdown when clicking outside of it
window.addEventListener('click', function (event) {
    const dropdown = document.getElementById('dropdownDivider3');
    if (!dropdown.contains(event.target) && event.target !== dropdownDividerButton3) {
        dropdown.classList.add('hidden');
    }
});


// this is navbar dropdown 4
// JavaScript for dropdown functionality
document.getElementById('dropdownDividerButton4').addEventListener('click', function () {
    const dropdown = document.getElementById('dropdownDivider4');
    dropdown.classList.toggle('hidden');
});

// Optional: Close dropdown when clicking outside of it
window.addEventListener('click', function (event) {
    const dropdown = document.getElementById('dropdownDivider4');
    if (!dropdown.contains(event.target) && event.target !== dropdownDividerButton4) {
        dropdown.classList.add('hidden');
    }
});

// this is navbar dropdown 5
// JavaScript for dropdown functionality
document.getElementById('dropdownDividerButton5').addEventListener('click', function () {
    const dropdown = document.getElementById('dropdownDivider5');
    dropdown.classList.toggle('hidden');
});

// Optional: Close dropdown when clicking outside of it
window.addEventListener('click', function (event) {
    const dropdown = document.getElementById('dropdownDivider5');
    if (!dropdown.contains(event.target) && event.target !== dropdownDividerButton5) {
        dropdown.classList.add('hidden');
    }
});

// this is navbar dropdown 6
// JavaScript for dropdown functionality
document.getElementById('dropdownDividerButton6').addEventListener('click', function () {
    const dropdown = document.getElementById('dropdownDivider6');
    dropdown.classList.toggle('hidden');
});

// Optional: Close dropdown when clicking outside of it
window.addEventListener('click', function (event) {
    const dropdown = document.getElementById('dropdownDivider6');
    if (!dropdown.contains(event.target) && event.target !== dropdownDividerButton6) {
        dropdown.classList.add('hidden');
    }
});

// Navbar dropdown close








//  javascript for closing navbar in small device 
document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu button
    const mobileMenuButton = document.querySelector('button[aria-controls="mobile-menu"]');
    const mobileMenu = document.getElementById('mobile-menu');

    // Ensure the mobile menu is hidden initially
    mobileMenu.classList.add('hidden');
    mobileMenuButton.setAttribute('aria-expanded', 'false');

    // Toggle mobile menu
    mobileMenuButton.addEventListener('click', () => {
        const isOpen = mobileMenuButton.getAttribute('aria-expanded') === 'true';
        mobileMenuButton.setAttribute('aria-expanded', !isOpen);
        mobileMenu.classList.toggle('hidden', isOpen);
    });

    // User menu button
    const userMenuButton = document.getElementById('user-menu-button');
    const userMenu = document.querySelector('[role="menu"]');

    // Ensure the user menu is hidden initially
    userMenu.classList.add('hidden');
    userMenuButton.setAttribute('aria-expanded', 'false');

    // Toggle user menu
    userMenuButton.addEventListener('click', () => {
        const isOpen = userMenuButton.getAttribute('aria-expanded') === 'true';
        userMenuButton.setAttribute('aria-expanded', !isOpen);
        userMenu.classList.toggle('hidden', isOpen);
    });

    // Close the user menu when clicking outside
    document.addEventListener('click', (event) => {
        if (!userMenuButton.contains(event.target) && !userMenu.contains(event.target)) {
            userMenu.classList.add('hidden');
            userMenuButton.setAttribute('aria-expanded', 'false');
        }
    });
});


// close javascript for closing nav in small










//  animation page start 
// Simulating a loading period
window.onload = function () {
    setTimeout(() => {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('content').classList.remove('hidden');
    }, 3000); // Adjust time as needed
};
// animation page close








// some unknown js code in home start 1
function toggleDropdown(event) {
    event.preventDefault();
    const dropdown = document.getElementById('dropdown');
    dropdown.classList.toggle('hidden');
}

// Close dropdown if clicked outside
window.onclick = function (event) {
    const dropdown = document.getElementById('dropdown');
    if (!event.target.matches('#menu-button')) {
        if (!dropdown.classList.contains('hidden')) {
            dropdown.classList.add('hidden');
        }
    }
}
// some unknown js code in home close 1
// some unknown js code in home start 2
const navLinks = document.querySelector('.nav-links')
function onToggleMenu(e) {
    e.name = e.name === 'menu' ? 'close' : 'menu'
    navLinks.classList.toggle('top-[7%]')
}
// some unknown js code in home close 2
