//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

// Travel Notes

document.getElementById('travelNotes').addEventListener('click', function() {

    var link1 = document.createElement('a');
    link1.href = 'https://trello.com/b/AvEQKz0L/travel-notes';
    link1.target = '_blank';

    var link2 = document.createElement('a');
    link2.href = 'https://rewqwer.atlassian.net/issues/?jql=project+%3D+%22IT%22+ORDER+BY+created+DESC&atlOrigin=eyJpIjoiM2RlZmVhMTI5NWM3NDNmZTg5NzU2MjI1YTAwY2FmNGEiLCJwIjoiaiJ9';
    link2.target = '_blank';

    document.body.appendChild(link1);

    link1.addEventListener('click', function(event) {

        if (!confirm('"Travel Notes" is a web application for creating travel notes.\n\nYou are about to open the test documentation for the Travel Notes application. Confirm the action.')) {
            event.preventDefault();
        } else {
            document.body.appendChild(link2);
            link2.click();
            document.body.removeChild(link2);
        }
    });

    link1.click();
    document.body.removeChild(link1);
});

// KIMBA 2

document.getElementById('kimba2').addEventListener('click', function() {

    var link1 = document.createElement('a');
    link1.href = 'https://trello.com/b/7PiG0Oit';
    link1.target = '_blank';

    var link2 = document.createElement('a');
    link2.href = 'https://rewqwer.atlassian.net/issues/?jql=project+%3D+%22K2%22+ORDER+BY+created+DESC&atlOrigin=eyJpIjoiNzhmZjgxZjBiYjViNDkwNjk5N2ZkYThhNDllMDU5YzciLCJwIjoiaiJ9';
    link2.target = '_blank';

    document.body.appendChild(link1);

    link1.addEventListener('click', function(event) {

        if (!confirm('"KIMBA 2" is a desktop application for photo editing.\n\nYou are about to open the test documentation for the KIMBA 2 application. Confirm the action.')) {
            event.preventDefault();
        } else {
            document.body.appendChild(link2);
            link2.click();
            document.body.removeChild(link2);
        }
    });

    link1.click();
    document.body.removeChild(link1);
});
