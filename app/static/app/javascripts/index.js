$(function() {
  var insertExperienceData = function(experienceElem, experience) {
    experienceElem.find("a").attr("href", experienceUrl.replace("123", experience.id));
    experienceElem.find("#experiencePrice").text("$ " + experience.price);
    experienceElem.find("#experienceNameLink").text(experience.name);
    experienceElem.find("#experienceLocationLink").text(experience.location);
    experienceElem.find("#experienceSubheader").text(experience.subheader);
  }

  var renderExperiences = function(data) {
    var experiencesContainer = $("#experiencesContainer");
    experiencesContainer.empty();

    if(data.length > 0) {
      var row = $("<div class='row'></div>");
      $.each(data, function(i, experience) {
        if(i % 4 == 0)
          experiencesContainer.append(row);

        var experienceElem = $("<div>");
        experienceElem.load(experienceHtml, function() {
          insertExperienceData(experienceElem, experience);
          insertImageAsynchronously("https://dp95gqg0hgx2o.cloudfront.net/" + JSON.parse(experience.images)[0], experienceElem.find("#experienceMain"));
        });
        row.append(experienceElem);

        if((i + 1) % 4 == 0)
          row = $("<div class='row'></div>");
      });
      row = $("<div class='row'></div>");
    }
    else
      experiencesContainer.append("<p class='no-results'>No hay experiencias disponibles</p>");
  };

  var ajax;
  var getExperiences = function(category) {
    if(ajax)
      ajax.abort();

    var experiencesContainer = $("#experiencesContainer");
    experiencesContainer.empty();
    experiencesContainer.append("<p class='no-results'><img src='" + loader + "'></p>");

    ajax = $.ajax({
      url: experiencesUrl + "?category=" + category.replace(/ /g, "_"),
      method: "GET",
      dataType: "json",
      success: function(data) {
        renderExperiences(data);
      }
    });
  };

  getExperiences("Aventura 2 días");


  $("#bannerLink").click(function() {
    $("body").animate({
      scrollTop: $("#experiences").offset().top
    }, 500);
  });


  $(".navbar-exp-element").click(function() {
    $(".navbar-exp-element").removeClass("selected");
  });
  $("#adv1").click(function() {
    if(!$("#adv1").hasClass("selected")) {
      $("#adv1").addClass("selected");
      getExperiences("Aventura 1 día");
    }
  });
  $("#adv2").click(function() {
    if(!$("#adv2").hasClass("selected")) {
      $("#adv2").addClass("selected");
      getExperiences("Aventura 2 días");
    }
  });
  /*$("#gastro").click(function() {
    if(!$("#gastro").hasClass("selected")) {
      $("#gastro").addClass("selected");
      getExperiences("Gastronomía");
    }
    });*/
});
