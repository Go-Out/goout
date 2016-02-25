$(function() {
  var insertExperienceData = function(experienceElem, experience) {
    experienceElem.find("a").attr("href", experienceUrl.replace("123", experience.id));
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

  var getExperiences = function(date) {
    $.ajax({
      url: experiencesUrl + "?date=" + dateToStr(new Date(date)),
      method: "GET",
      dataType: "json",
      success: function(data) {
        renderExperiences(data);
      }
    });
  };

  var dateToStr = function(date) {
    return date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate();
  };

  var dateInput = $("#datepicker");
  dateInput.datepicker({
    dateFormat: "DD dd MM yy",
    minDate: +1,
    dayNames: [ "Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado" ],
    monthNames: [ "Enero","Febrero","Marzo","Abril","Mayo","Junio", "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre" ],
    onSelect: function(date, inst) {
      getExperiences(date);
    }
  });

  var today = new Date();
  var startDate = new Date();
  startDate.setDate(today.getDate() + (6 - today.getDay()));
  dateInput.datepicker("setDate", startDate);

  getExperiences(startDate);
});
