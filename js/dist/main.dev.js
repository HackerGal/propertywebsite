"use strict";

// Initialize and add the map
function initMap() {
  // Your location
  var loc = {
    lat: 42.361145,
    lng: -71.057083
  }; // Centered map on location

  var map = new google.maps.Map(document.querySelector('.map'), {
    zoom: 14,
    center: loc
  }); // The marker, positioned at location

  var marker = new google.maps.Marker({
    position: loc,
    map: map
  });
} // Sticky menu background


window.addEventListener('scroll', function () {
  if (window.scrollY > 150) {
    document.querySelector('#navbar').style.opacity = 0.9;
  } else {
    document.querySelector('#navbar').style.opacity = 1;
  }
}); // Smooth Scrolling

$('#navbar a').on('click', function (event) {
  if (this.hash !== '') {
    event.preventDefault();
    var hash = this.hash;
    $('html, body').animate({
      scrollTop: $(hash).offset().top - 100
    }, 800);
  }
});