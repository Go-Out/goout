$(function() {
  var dateToStr = function(date) {
    console.log(date);
    return date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate();
  };

  var renderExperiences = function(data) {
    var html = "";
    $.each(data, function(i, experience) {
      if(i % 4 == 0)
        html += "<div class='row'>";

      html += "<div class='col-md-3 experience-col'>";
      html += "<div class='experience'>";
      html += "<a class='fill' href='" + experience_url.replace("123", experience.id) + "'></a>";
      html += "<span class='experience-price'>";
      html += "$ " + experience.price;
      html += "</span>";
      html += "</div>";
      html += "<div class='experience-description'>";
      html += "<p class='experience-name'><a href='" + experience_url.replace("123", experience.id) + "'>" + experience.name + "</a></p>";
      html += "<p class='experience-location'><a href='" + experience_url.replace("123", experience.id) + "'>" + experience.location + "</a></p>";
      html += "</div>";
      html += "</div>";

      if((i + 1) % 4 == 0 || (i + 1) == data.length)
        html += "</div>";
    });
    $("#experiences_container").html(html);
  };

  var getExperiences = function(date) {
    $.ajax({
      url: experiences_url + "?date=" + dateToStr(new Date(date)),
      method: "GET",
      dataType: "json",
      success: function(data) {
        renderExperiences(data);
      }
    });
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
