Conekta.setPublishableKey('key_LyWdGMc3hsbMwMzV1Uqytag');

$(function () {
  $("#card-form").submit(function(event) {
    var $form = $(this);

    // Previene hacer submit más de una vez
    $form.find("button").prop("disabled", true);
    Conekta.token.create($form, conektaSuccessResponseHandler, conektaErrorResponseHandler);

    // Previene que la información de la forma sea enviada al servidor
    return false;
  });

  var dateObj = new Date(getQueryValue("date"));
  $("#date").text(dayNames[dateObj.getDay()] + " " + monthNames[dateObj.getMonth()] + " " + dateObj.getFullYear());
});

var conektaSuccessResponseHandler = function(token) {
  var $form = $("#card-form");

  /* Inserta el token_id en la forma para que se envíe al servidor */
  $form.append($("<input type='hidden' name='conektaTokenId'>").val(token.id));

  /* and submit */
  $form.get(0).submit();
};

var conektaErrorResponseHandler = function(response) {
  var $form = $("#card-form");

  /* Muestra los errores en la forma */
  $form.find(".card-errors").text(response.message);
  $form.find("button").prop("disabled", false);
};
