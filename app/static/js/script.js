$(document).ready(function() {
    $('.menu-button').on('click', function() {
        $('.full-page-menu').addClass('open');
    });

    $('.close-button').on('click', function() {
        $('.full-page-menu').removeClass('open');
    });

    $('.dropdown-header').on('click', function() {
        $(this).children('.dropdown-content').slideToggle();
    });
});