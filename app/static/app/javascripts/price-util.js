var getPrice = function() {
  if(experiencePrices.length > 0) {
    var experiencesPrice = 0;
    for(var i = 0; i < experiencePrices.length; i++)
    experiencesPrice += experiencePrices[i] * people;
    var total = getHuttPrice() + experiencesPrice;
    return total - (total * (0.73 * (people - 1) + 1.14 * experiencePrices.length) / 100);
  }
  else
    return price;
};

var getHuttPrice = function() {
  if(people < 5)
    return 1450;
  if(people < 9)
    return 2700;
  if(people < 11)
    return 2959;
  return 3900;
};

var getDiscount = function() {
  if(experiencePrices.length > 0) {
    var experiencesPrice = 0;
    for(var i = 0; i < experiencePrices.length; i++)
    experiencesPrice += experiencePrices[i] * people;
    var total = getHuttPrice() + experiencesPrice;
    return total * (0.73 * (people - 1) + 1.14 * experiencePrices.length) / 100;
  }
  else
    return 0;
};

var formatNumber = function(n) {
  return n.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1,');
}
