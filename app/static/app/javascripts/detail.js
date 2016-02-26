(function() {
  $(document).ready(function() {
    var priceBox = $("#hardBox");
    var pos = priceBox.offset();
    var initialWidth = priceBox.width();

    $(window).scroll(function() {
      var windowpos = $(window).scrollTop();
      if (windowpos >= (pos.top - 20)) {
        priceBox.addClass("stick");
        priceBox.css("width", initialWidth);
      }
      else {
        priceBox.removeClass("stick"); 
        priceBox.css("width", "auto");
      }
    });
  });

  $("#mainPicture").click(function() {
    $("#picturesContainer").removeClass("hidden");
    $("body").addClass("no-overflow");
  });
  $("#picturesClose").click(function() {
    $("#picturesContainer").addClass("hidden");
    $("body").removeClass("no-overflow");
  });

  insertImageAsynchronously(imgUrl, $("#mainPicture"), experienceName);

  var renderAvailability = function(available) {
    var bookHtml = available ? "<p>Reservar</p><p class='booking-number'><strong>333 359 7080</strong></p>" : "<p class='booking-number'><strong>No disponible</strong></p>";
    $("#booking").html(bookHtml);
    $("#bookingWide").html(bookHtml);
  };

  var getExperienceAvailability = function(date) {
    var dateStr = dateToStr(new Date(date));
    $.ajax({
      url: availabilityUrl.replace("123", experienceId) + "?date=" + dateStr,
      method: "GET",
      dataType: "json",
      success: function(data) {
        renderAvailability(data.available);
        window.history.replaceState(data, "ExperienceAvailability", experienceUrl.replace("123", experienceId) + "?date=" + dateStr);
      }
    });
  };

  var dateInput = $("#datepicker");
  var dateInputWide = $("#datepickerWide");
  var datepickerOptions = {
    dateFormat: dateFormat,
    minDate: +1,
    dayNames: dayNames,
    monthNames: monthNames,
    onSelect: function(date, inst) {
      getExperienceAvailability(date);
    }
  };
  dateInput.datepicker(datepickerOptions);
  dateInputWide.datepicker(datepickerOptions);

  var dateStr = getQueryValue("date");
  var startDate = new Date(dateStr);
  dateInput.datepicker("setDate", startDate);
  dateInputWide.datepicker("setDate", startDate);

  getExperienceAvailability(dateStr);
})();
