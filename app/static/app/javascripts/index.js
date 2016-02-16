$(function() {
  var dateToStr = function(date) {
    return date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate();
  };

  var renderExperiences = function(data) {
    var html = "";
    $.each(data, function(i, experience) {
      if(i % 4 == 0)
        html += "<div class='row'>";

      html += "<div class='col-md-3 experience-col'>";
      html += "<a href='" + experience_url.replace("123", experience.id) + "'>";
      html += "<div class='experience'>";
      html += "</div>";
      html += "<div class='experience-description'>";
      html += "<p>" + experience.name + "</p>";
      html += "</div>";
      html += "</a>";
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
    dateFormat: "dd M yy",
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
