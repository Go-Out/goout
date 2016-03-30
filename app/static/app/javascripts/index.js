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
        insertImageAsynchronously(window.location.origin + "/" + experience.images_path + "/0.jpg", experienceElem.find("#experienceMain"));
      });
      row.append(experienceElem);

      if((i + 1) % 4 == 0 || (i + 1) == data.length)
        row = $("<div class='row'></div>");
    });
  };

  var getExperiences = function() {
    $.ajax({
      url: experiencesUrl,
      method: "GET",
      dataType: "json",
      success: function(data) {
        renderExperiences(data);
      }
    });
  };

  getExperiences();


  $("#bannerLink").click(function() {
    $("body").animate({
      scrollTop: $("#experiences").offset().top
    }, 500);
  });
});
