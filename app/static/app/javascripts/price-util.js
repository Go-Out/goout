// Gets the price for all experiences
var getExperiencesPrice = function() {
  if(experiencePrices.length > 0) {
    var experiencesPrice = 0;
    for(var i = 0; i < experiencePrices.length; i++)
      experiencesPrice += experiencePrices[i] * people;
    return experiencesPrice;
  }
  else
    return price * people;
}

// Subtracts the discount from the total price
var getRealPrice = function() {
  var total = getHuttPrice() + getExperiencesPrice();
  return total - (total * (0.73 * (people - 1) + 1.14 * experiencePrices.length) / 100);
};

// Price for the hutt
var getHuttPrice = function() {
  if(experiencePrices.length < 1)
    return 0;
  if(people < 5)
    return 1450;
  if(people < 9)
    return 2700;
  if(people < 11)
    return 2959;
  return 3900;
};

// Gets the discount
var getDiscount = function() {
  var total = getHuttPrice() + getExperiencesPrice();
  return total - getPrice();
};

// Gets the price to be displayed, rounding prices per person to avoid decimals
var getPrice = function() {
  return Math.ceil(getRealPrice() / people) * people;
};

var formatNumber = function(n) {
  return n.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1,');
}
