(function() {
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
    var bookHtml = available ? "<a href='" + payment + "?date=" + date + "&people=" + people + "' class='payment-link'>Reservar</a><p class='booking-recommendation'>1 semana de antipación (recomendado)</p>" : "<p class='booking-unavailable'><strong>No disponible</strong></p>";
    $(".booking").html(bookHtml);
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
  startDate.setDate(today.getDate() + (6 - today.getDay()));
  dateInput.datepicker("setDate", startDate);

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


  var getPrice = function() {
    var total = price * people;
    return (total - (total * (0.73 * (people - 1) + 1.14 * (noExperiences - 1)) / 100)).toFixed(1);
  };

  var getHuttPrice = function() {
    if(noExperiences < 1)
      return 0;
    if(people < 5)
      return 1450;
    if(people < 9)
      return 2700;
    if(people <= 10)
      return 2959;
    return 3900;
  };

  $(".price").text("$ " + getPrice());

  $(".participants").val(people);
  $(".participants").change(function() {
    people = parseInt($(this).val())
    $(".payment-link").attr("href", payment + "?date=" + dateStr + "&people=" + people);
    $(".price").text("$ " + getPrice());
  });
})();
