// Get a reference to the form element
import("https://apis.mappls.com/advancedmaps/api/cfd59a143370d6d61bd01e37ab1a7f5f/map_sdk?v=3.0&layer=vector")
var form = document.getElementById("formap");

// Add a submit event listener to the form
form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get form field values
    var lat = document.getElementById("text_field1").value;
    var long = document.getElementById("text_field2").value;

    // Do something with the data (e.g., display or process it)
    console.log("Name: " + lat);
    console.log("Email: " + long);
    map = new mappls.Map('map', {center:{lat:28.612964,lng:77.229463} });
});
