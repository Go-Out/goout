(function() {
  var people = 1;
  var dateStr;

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

  var renderAvailability = function(available, date) {
    var bookHtml = available ? "<a href='" + payment + "?date=" + date + "&people=" + people + "' class='payment-link'>Reservar</a><p class='booking-recommendation'>1 semana de antipación (recomendado)</p>" : "<p class='booking-number'><strong>No disponible</strong></p>";
    $("#booking").html(bookHtml);
    $("#bookingWide").html(bookHtml);
  };

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

  var dateInput = $("#datepicker");
  var dateInputWide = $("#datepickerWide");
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

  $("#participants").change(function() {
    people = parseInt($("#participants").val())
    $(".payment-link").attr("href", payment + "?date=" + dateStr + "&people=" + people);
    $("#price").text("$ " + (people * price));
  });
  $("#participantsWide").change(function() {
    people = parseInt($("#participantsWide").val())
    $(".payment-link").attr("href", payment + "?date=" + dateStr + "&people=" + people);
    $("#priceWide").text("$ " + (people * price));
  });
})();
