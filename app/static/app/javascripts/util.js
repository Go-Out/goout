var insertImageAsynchronously = function(imgSrc, imgElem, experience) {
  var img = new Image();
  img.onload = function() {
    imgElem.css({
      "background": "url('" + img.src  + "') no-repeat center center",
      "background-size": "cover"
    }); 
  };
  img.src = imgSrc.replace("name", experience.replace(/ /g, "_"));
};
