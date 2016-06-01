(function() {
  var dateStr;

/*** Controls ***/

  // Constrols the stickiness of the price box
  $(document).ready(function() {
    var priceBox = $("#hardBox");
    var boxTop = priceBox.offset().top - 30;
    var initialWidth = priceBox.width() + 2;

    $(window).scroll(function() {
      var scrollTop = $(window).scrollTop();

      if (scrollTop >= boxTop) {
        priceBox.addClass("stick");
        priceBox.css("width", initialWidth);
      }
      else {
        priceBox.removeClass("stick"); 
        priceBox.css("width", "auto");
      }
    });
  });

  // Pictures controls
  var i = 0;
  var mainPicture = $("#mainPicture");
  $("#controlLeft").click(function() {
    i--;
    if(i < 0)
      i = experienceImgs.length - 1;
    mainPicture.css({
      "background": "url('" + imgUrl + "/" +  experienceImgs[i]  + "') no-repeat center center",
      "background-size": "cover"
    });
  });
  $("#controlRight").click(function() {
    i++;
    if(i == experienceImgs.length)
      i = 0;
    mainPicture.css({
      "background": "url('" + imgUrl + "/" +  experienceImgs[i]  + "') no-repeat center center",
      "background-size": "cover"
    });
  });

/*** Initial operations ***/

  // Renders book button or the 'No disponible' text
  var renderAvailability = function(available, date) {
    var bookHtml = available ? "<a href='" + payment + "?date=" + date + "&people=" + people + "' class='payment-link'>Reservar</a>" : "<p class='booking-unavailable'><strong>No disponible</strong></p>";
    $(".booking").html(bookHtml);
  };

  // Call to check availability of experience
  var getExperienceAvailability = function(date) {
    dateStr = dateToStr(date);
    $.ajax({
      url: availabilityUrl + "?date=" + dateStr,
      method: "GET",
      dataType: "json",
      success: function(data) {
        renderAvailability(data.available, dateStr);
        window.history.replaceState(data, "ExperienceAvailability");
      }
    });
  };


  insertImageAsynchronously(imgUrl + "/" + experienceImgs[0], $("#mainPicture"));

  // Datepicker controls
  var dateInput = $(".datepicker");
  var datepickerOptions = {
    dateFormat: dateFormat,
    minDate: +1,
    dayNames: dayNames,
    monthNames: monthNames,
    onSelect: function(date, inst) {
      getExperienceAvailability(new Date(reverseDate(date)));
    }
  };
  dateInput.datepicker(datepickerOptions);

  var today = new Date();
  var startDate = new Date();
  startDate.setDate(today.getDate() + 1);
  dateInput.datepicker("setDate", startDate);

  getExperienceAvailability(startDate);

  // Loads every image asynchronously
  $.each(experienceImgs, function(i, img) {
    loadImageAsynchronously(imgUrl + "/" + img);
  });

/*** Price updates ***/

  var updatePrice = function() {
    var  finalPrice = getPrice();
    var discount = getDiscount();

    $(".price").text("$ " + formatNumber(finalPrice));

    if(discount > 0) {
      $(".discount-row").show();
      $(".discount").text("$ " + formatNumber(discount));
    }
    else
      $(".discount-row").hide();

    $(".price-per-person").text("$ " + formatNumber(finalPrice / people));
  };

  updatePrice();

  $(".participants").val(people);
  $(".participants").change(function() {
    people = parseInt($(this).val())
    $(".payment-link").attr("href", payment + "?date=" + dateStr + "&people=" + people);
    updatePrice();
  });
})();
