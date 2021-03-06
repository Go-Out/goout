// Inserts an image asynchronously, given the image url and the element where to put it
var insertImageAsynchronously = function(imgSrc, imgElem) {
  var img = new Image();
  img.onload = function() {
    imgElem.css({
      "background": "url('" + img.src  + "') no-repeat center center",
      "background-size": "cover"
    }); 
  };
  img.src = imgSrc;
};

// Just loads an image asynchronously, without putting it anywhere
var loadImageAsynchronously = function(imgSrc) {
  var img = new Image();
  img.src = imgSrc;
};

var dateToStr = function(date) {
  return date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate();
};

var reverseDate = function(dateStr) {
  var dateParts = dateStr.split(" ");
  return dateParts[3] + "-" + (monthNames.indexOf(dateParts[2]) + 1) + "-" + dateParts[1];
}

// Gets a quert parameter's value
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
