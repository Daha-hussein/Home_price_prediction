function getBathroomsValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i = 0; i < uiBathrooms.length; i++) {
    if (uiBathrooms[i].checked) {
      return parseInt(uiBathrooms[i].value);
    }
  }
  return -1; // Invalid Value
}

function getbedroomsValue() {
  var uibdrm = document.getElementsByName("uibdrm");
  for (var i = 0; i < uibdrm.length; i++) {
    if (uibdrm[i].checked) {
      return parseInt(uibdrm[i].value);
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var area = document.getElementById("uiSqft");
  var bedrooms = getBedroomsValue();
  var bathrooms = getBathroomsValue();
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:8040/predict_home_price"

  $.post(
    url,
    {
      area: parseFloat(area.value),
      bedrooms: bedrooms,
      bathrooms: bathrooms,
    },
    function (data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " dollar</h2>";
      console.log(status);
    }
  );
}

window.onload = function () {
  console.log("document loaded");
};