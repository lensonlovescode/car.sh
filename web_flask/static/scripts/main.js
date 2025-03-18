$(document).ready(function () {
    $.get('https://127.0.0.1/api/v1/status', function (data) {
        console.log(data.status);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const carCatalogue = document.getElementById("carCatalogue");
    const mainImage = document.getElementById("main-car-image");

    
    const carImagesFolder = "../static/images/";

  
    const cars = [
        { name: "Ford Explorer", img: "ford.jpg" },
        { name: "Mercedes-Benz C-Class", img: "mercedes.jpg" },
        { name: "Tesla Model S", img: "tesla.jpg" },
        { name: "BMW X5", img: "bmw.jpg" },
        { name: "Audi Q7", img: "audi.jpg" }
    ];

  
    function loadCars() {
        cars.forEach(car => {
            const carItem = document.createElement("div");
            carItem.classList.add("car-item");

            const carImg = document.createElement("img");
            carImg.src = `${carImagesFolder}${car.img}`;
            carImg.alt = car.name;
            carImg.classList.add("thumbnail");

            carImg.addEventListener("click", function () {
                mainImage.style.opacity = "0"; 
                setTimeout(() => {
                    mainImage.src = this.src;
                    mainImage.style.opacity = "1"; 
                }, 300);

                
                document.querySelectorAll(".thumbnail").forEach(img => img.classList.remove("selected"));
                this.classList.add("selected");
            });

           
            const carName = document.createElement("h3");
            carName.textContent = car.name;

            const viewDetailsButton = document.createElement("button");
            viewDetailsButton.textContent = "View Details";
            viewDetailsButton.classList.add("view-details");

          
            carItem.appendChild(carImg);
            carItem.appendChild(carName);
            carItem.appendChild(viewDetailsButton);
            carCatalogue.appendChild(carItem);
        });
    }

   
    loadCars();

   
    window.addEventListener("scroll", function () {
        const scrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
        const currentScroll = window.scrollY;

        if (currentScroll >= scrollableHeight - 100) {
            loadCars();
        }
    });
});
