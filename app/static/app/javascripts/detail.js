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


  insertImageAsynchronously(imgUrl.replace("123", "0.jpg"), $("#mainPicture"), experienceName);

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

  var i = 0;
  var mainPicture = $("#mainPicture");
  $("#controlLeft").click(function() {
    i--;
    if(i < 0)
      i = experienceImgs.length - 1;
    mainPicture.css({
      "background": "url('" + imgUrl.replace("name", experienceName.replace(/ /g, "_")).replace("123", experienceImgs[i])  + "') no-repeat center center",
      "background-size": "cover"
    });
    console.log(experienceImgs[i])
  });
  $("#controlRight").click(function() {
    i++;
    if(i == experienceImgs.length)
      i = 0;
    mainPicture.css({
      "background": "url('" + imgUrl.replace("name", experienceName.replace(/ /g, "_")).replace("123", experienceImgs[i])  + "') no-repeat center center",
      "background-size": "cover"
    });
    console.log(experienceImgs[i])
  });

  $.each(experienceImgs, function(i, img) {
    imgUrl.replace("name", experienceName.replace(/ /g, "_")).replace("123.jpg", img)
  });
})();
