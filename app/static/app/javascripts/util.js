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

var dateToStr = function(date) {
  return date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate();
};

var getQueryValue = function(variable) {
  var query = window.location.search.substring(1);
  var vars = query.split("&");
  for(var i = 0; i < vars.length; i++) {
    var pair = vars[i].split("=");
    if(pair[0] == variable)
      return pair[1];
  }
  return "";
};

var dateFormat = "DD dd MM yy";
var dayNames = ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"];
var monthNames = ["Enero","Febrero","Marzo","Abril","Mayo","Junio", "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
