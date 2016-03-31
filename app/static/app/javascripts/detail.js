(function() {
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

  var renderAvailability = function(available) {
    var bookHtml = available ? "<a href='" + payment + "' class='payment-link'>Reservar</a><p class='booking-recommendation'>1 semana de antipación (recomendado)</p>" : "<p class='booking-number'><strong>No disponible</strong></p>";
    $("#booking").html(bookHtml);
    $("#bookingWide").html(bookHtml);
  };

  var getExperienceAvailability = function(date) {
    var dateStr = dateToStr(date);
    $.ajax({
      url: availabilityUrl + "?date=" + dateStr,
      method: "GET",
      dataType: "json",
      success: function(data) {
        renderAvailability(data.available);
        window.history.replaceState(data, "ExperienceAvailability");
      }
    });
  };


  insertImageAsynchronously(imgUrl + "/" + experienceImgs[0], $("#mainPicture"));

  var dateInput = $("#datepicker");
  var dateInputWide = $("#datepickerWide");
  var datepickerOptions = {
    dateFormat: dateFormat,
    minDate: +1,
    dayNames: dayNames,
    monthNames: monthNames,
    onSelect: function(date, inst) {
      var dateParts = date.split(" ");
      var dateStr = dateParts[3] + "-" + (monthNames.indexOf(dateParts[2]) + 1) + "-" + dateParts[1];
      getExperienceAvailability(new Date(dateStr));
    }
  };
  dateInput.datepicker(datepickerOptions);
  dateInputWide.datepicker(datepickerOptions);

  var today = new Date();
  var startDate = new Date();
  startDate.setDate(today.getDate() + (6 - today.getDay()));
  dateInput.datepicker("setDate", startDate);
  dateInputWide.datepicker("setDate", startDate);

  getExperienceAvailability(startDate);

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

  $.each(experienceImgs, function(i, img) {
    loadImageAsynchronously(imgUrl + "/" + img);
  });
})();
