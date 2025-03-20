// $(document).ready(function () {
//     $.get('http://localhost:5001/api/v1/status', function (data) {
//         console.log(data.status);
//     });
// });

// document.addEventListener('DOMContentLoaded', function() {
//     document.getElementById('overlay').style.display = 'none';

//     const openOverlayBtn = document.getElementById('open-overlay');
//     if (openOverlayBtn) {
//         const newBtn = openOverlayBtn.cloneNode(true);
//         openOverlayBtn.parentNode.replaceChild(newBtn, openOverlayBtn);
//     }
// });

// document.querySelector('.menu-toggle').addEventListener('click', function() {
//     document.querySelector('.nav-links').classList.toggle('active');
// });

// document.addEventListener('DOMContentLoaded', function() {
//     const viewDealButtons = document.querySelectorAll('.view-deal-button');

//     const overlay = document.getElementById('overlay');
//     const closeOverlayButton = document.getElementById('close-overlay');

//     viewDealButtons.forEach(button => {
//         button.addEventListener('click', function() {
//             const carCard = this.closest('.car-card');

//             const title = carCard.querySelector('.car-card-title').textContent;
//             const description = carCard.querySelector('.car-description').textContent;
//             const mileage = carCard.querySelector('.mileage').textContent.match(/\d+/)[0];
//             const engine = carCard.querySelector('.engine-capacity').textContent.match(/[\d\.]+/)[0];
//             const transmission = carCard.querySelector('.transmission').textContent.replace(/.*\s/, '');
//             const fuelType = carCard.querySelector('.fuel-type').textContent.replace(/.*\s/, '');
//             const price = carCard.querySelector('.car-card-total').textContent.replace('Ksh. ', '');
//             const imgSrc = carCard.querySelector('.car-img').src;

//             overlay.querySelector('.car-img').src = imgSrc;
//             overlay.querySelector('.car-title').textContent = title;
//             overlay.querySelector('.car-description').textContent = description;
//             document.getElementById('mileage').textContent = mileage;
//             document.getElementById('engine').textContent = engine;
//             document.getElementById('transmission').textContent = transmission;
//             document.getElementById('fuel-type').textContent = fuelType;
//             document.getElementById('price').textContent = 'Ksh. ' + price;

//             overlay.style.display = 'flex';
//         });
//     });

//     closeOverlayButton.addEventListener('click', function() {
//         overlay.style.display = 'none';
//     });

//     overlay.addEventListener('click', function(e) {
//         if (e.target === overlay) {
//             overlay.style.display = 'none';
//         }
//     });
// });
