$(function() {
    $('#topbar').scrollSpy()

    $('#topbar ul li a').bind('click', function(e) {
        e.preventDefault();
        target = this.hash;
        console.log(target);
        $.scrollTo(target, 1000);
   });
});
