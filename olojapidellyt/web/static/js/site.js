$(document).ready(function() {
    $("a.menu, open, .menu-dropdown").hover(function (e) {
        var $li = $(this).parent("li").toggleClass('open');
        return false;
    });
});

