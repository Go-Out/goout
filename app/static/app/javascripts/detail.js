(function() {
  $(document).ready(function() {
    var priceBox = $("#hardBox");
    var pos = priceBox.offset();
    var initialWidth = priceBox.width();

    $(window).scroll(function() {
      var windowpos = $(window).scrollTop();
      if (windowpos >= (pos.top - 71)) {
        priceBox.addClass("stick");
        priceBox.css("width", initialWidth);
      }
      else {
        priceBox.removeClass("stick"); 
        priceBox.css("width", auto);
      }
    });
  });
})();
