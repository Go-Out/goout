Conekta.setPublishableKey('key_LyWdGMc3hsbMwMzV1Uqytag');

$(function () {
  $("#card-form").submit(function(event) {
    var $form = $(this);

    $form.find(".card-errors").text("");

    if(validateForm($form)) {
      // Previene hacer submit más de una vez
      $form.find("button").prop("disabled", true);
      Conekta.token.create($form, conektaSuccessResponseHandler, conektaErrorResponseHandler);
    }
    else
      $form.find(".card-errors").text("Hay campos vacíos");

    // Previene que la información de la forma sea enviada al servidor
    return false;
  });

  var dateObj = new Date(getQueryValue("date"));
  $("#date").text(dayNames[dateObj.getDay()] + " " + monthNames[dateObj.getMonth()] + " " + dateObj.getFullYear());
  var people = getQueryValue("people")
  $("#people").text(people);
  $("#price").text("$ " + (parseInt(people) * price));

  var validateForm = function(form) {
    var valid = true;
    $.each(form.find("input"), function(i, child) {
      if(!child.value) {
        $(child).addClass("invalid")
        valid = false;
      }
    });
    return valid;
  };
});

var conektaSuccessResponseHandler = function(token) {
  var $form = $("#card-form");

  /* Inserta el token_id en la forma para que se envíe al servidor */
  $form.append($("<input type='hidden' name='conektaTokenId'>").val(token.id));
  $form.append($("<input type='hidden' name='date'>").val($("#date").text()));
  $form.append($("<input type='hidden' name='people'>").val($("#people").text()));
  $form.append($("<input type='hidden' name='price'>").val($("#price").text()));
  $form.append($("<input type='hidden' name='experience'>").val($("#experience").text()));
  $form.append($("<input type='hidden' name='location'>").val($("#location").text()));

  /* and submit */
  $form.get(0).submit();
};

var conektaErrorResponseHandler = function(response) {
  var $form = $("#card-form");

  /* Muestra los errores en la forma */
  $form.find(".card-errors").text(response.message);
  $form.find("button").prop("disabled", false);
};
