$(document).ready(function() {
    $('.menu-button').click(function() {
        $(this).toggleClass('change');
        $('.full-page-menu').toggleClass('open');
    });
});