console.log("Working")

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
      } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
      }
    });
  }

// let city = localStorage.getItem('city')

// if (city == null) {
//     city = "Malappuram"
// }

// let form = document.getElementById('search-form');

// form.addEventListener('submit', function() {
//     let city = document.getElementById('city').value;
//     if (city == null) {
//       city = 'Malappuram'
//     }
//     localStorage.setItem('city', city);
// })

// window.onload = function() {
//   formSubmit(city)
// }

// function formSubmit(city) {
//     let form = document.getElementById('search-form');
//     document.getElementById('city').value = city;
//     form.submit();
// }