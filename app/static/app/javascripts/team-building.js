(function() {
  $(".banner-link").click(function() {
    $("body").animate({
      scrollTop: $("#contact").offset().top
    }, 500);
  });
})();
