var dateStr;
$(function() {
  $(document).ready(function() {
    if(window.location.href.indexOf("herokuapp") != -1)
      $("#bannerLink").attr("href", experienceUrl.replace("123", 91) + "?date=2016-3-5");
    else
      $("#bannerLink").attr("href", experienceUrl.replace("123", 313) + "?date=2016-3-5");
  });

  var insertExperienceData = function(experienceElem, experience) {
    experienceElem.find("a").attr("href", experienceUrl.replace("123", experience.id) + "?date=" + dateStr);
    experienceElem.find("#experiencePrice").text("$ " + experience.price);
    experienceElem.find("#experienceNameLink").text(experience.name);
    experienceElem.find("#experienceLocationLink").text(experience.location);
  }

  var renderExperiences = function(data) {
    var experiencesContainer = $("#experiencesContainer");
    experiencesContainer.empty();

    var row = $("<div class='row'></div>");
    $.each(data, function(i, experience) {
      if(i % 4 == 0)
        experiencesContainer.append(row);

      var experienceElem = $("<div>");
      experienceElem.load(experienceHtml, function() {
        insertExperienceData(experienceElem, experience);
        insertImageAsynchronously(experienceImg, experienceElem.find("#experienceMain"), experience.name);
      });
      row.append(experienceElem);

      if((i + 1) % 4 == 0 || (i + 1) == data.length)
        row = $("<div class='row'></div>");
    });
  };

  var getExperiences = function(date, first) {
    $.ajax({
      url: experiencesUrl + "?date=" + dateStr,
      method: "GET",
      dataType: "json",
      success: function(data) {
        renderExperiences(data);
        if(!first)
          window.setTimeout(function() {
            $(window).scrollTop($("#experiences").offset().top);
          }, 500);
      }
    });
  };


  var dateInput = $("#datepicker");
  dateInput.datepicker({
    dateFormat: dateFormat,
    minDate: +1,
    dayNames: dayNames,
    monthNames: monthNames,
    onSelect: function(date, inst) {
      dateStr = dateToStr(new Date(date));
      getExperiences(date, false);
    }
  });

  var today = new Date();
  var startDate = new Date();
  startDate.setDate(today.getDate() + (6 - today.getDay()));
  dateInput.datepicker("setDate", startDate);

  dateStr = dateToStr(startDate);

  getExperiences(startDate, true);
});
