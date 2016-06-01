// Call to action controll
(function() {
  $(".cta-link").click(function() {
    $("body").animate({
      scrollTop: $("#contact").offset().top
    }, 500);
  });
})();

// Team building form validation
var validateForm = function(form) {
  if(!form.name.value)
    form.name.className = "invalid";
  if(!form.email.value)
    form.email.className = "invalid";
  if(!form.phone.value)
    form.phone.className = "invalid";

  if(!form.phone.name || !form.email.value || !form.phone.value)
    return false;

  return true;
};
