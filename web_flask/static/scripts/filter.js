let dataInOverlay = {};
let overlayOpen = false;
let data;

$(document).ready(function () {
  $.get("/api/v1/makes", function (data) {
    $.each(data, function (index, make) {
      let option = $("<option></option>").text(make.name);
      option.val(make.name);
      $("#make").append(option);
    });
  });

  $.get("/api/v1/categories", function (data) {
    $.each(data, function (index, category) {
      let option = $("<option></option>").text(category.name);
      option.val(category.name);
      $("#category").append(option);
    });
  });

  $("#make, #category").change(function () {
    $("#model").empty().append('<option value="">Model</option>');

    const Make = $("#make").val();
    const Category = $("#category").val();

    if (Make === "None" || Category === "None") {
      return;
    }

    if (Make && Category) {
      let url = `/api/v1/makes/${Make}/${Category}`;
      console.log(url);
      $.get(url, function (data) {
        $.each(data, function (index, model) {
          let option = $("<option></option>").text(model.name);
          option.val(model.name);
          $("#model").append(option);
          console.log(option.val());
        });
      });
    }
  });

  $.get("/api/v1/models", function (data) {
    data = data;
    $(".catalogue-grid").empty();

    $.each(data, function (index, model) {

      let carCard = `
            <div class="car-card">
                <div class="car-image">
                    <img class="car-img" src="${model.img_path}">
                </div>

                <div class="car-card-contents">
                    <h4 class="car-card-title"> ${model.manufacturer_name} ${model.name}</h4>
                    <h3 class="car-description">${model.year}</h3>
                    <h6 class="car-card-info">
                        <ul class="car-specs">

                            <li class="mileage"><i class="fas fa-tachometer-alt"></i> ${model.ZeroToSixty} seconds</li>
                            <li class="engine-capacity"><i class="fas fa-cogs"></i>${model.engine_capacity} cc</li>
                            <li class="transmission"><i class="fas fa-exchange-alt"></i>${model.ignition} ignition</li>
                            <li class="fuel-type"><i class="fas fa-gas-pump"></i>${model.fuel}</li>
                        </ul>
                    </h6>
                </div>
                <div class="car-card-cost">
                    <h3 class="car-card-cash">Base Price</h3>
                    <h3 class="car-card-total">&pound;${model.base_price}</h3>
                    <button class="view-deal-button" id="open-overlay_${model.id}" onclick="handleViewDeal(this)"><i class="fas fa-eye"></i>View</button>
                </div>
            </div>
        `;

      $(".catalogue-grid").append(carCard);

    });
  });

  $("#search_button").on("click", function () {
    const Make = $("#make").val();
    const Category = $("#category").val();
    const Model = $("#model").val();

    if ($("#make").val() !== "None" || $("#category").val() !== "None") {
      let url = `/api/v1/makes/${Make}/${Category}`;
      $(".catalogue-grid").empty();
      $.get(url, function (data) {
        $.each(data, function (index, model) {

          let carCard = `
                    <div class="car-card">
                        <div class="car-image">
                            <img class="car-img" src="${model.img_path}">
                        </div>
                        <div class="car-card-contents">
                            <h4 class="car-card-title">${model.name}</h4>
                            <h3 class="car-description"> ${model.manufacturer_name} ${model.year}</h3>
                            <h6 class="car-card-info">
                                <ul class="car-specs">
                                    <li class="mileage"><i class="fas fa-tachometer-alt"></i> ${model.mileage} miles</li>
                                    <li class="engine-capacity"><i class="fas fa-cogs"></i>${model.engine_capacity} cc</li>
                                    <li class="transmission"><i class="fas fa-exchange-alt"></i>${model.ignition} ignition</li>
                                    <li class="fuel-type"><i class="fas fa-gas-pump"></i>${model.fuel_type}</li>
                                </ul>
                            </h6>
                        </div>
                        <div class="car-card-cost">
                            <h3 class="car-card-cash">Base Price</h3>
                            <h3 class="car-card-total">&pound;${model.base_price}</h3>
                            <button class="view-deal-button"
                                data-model='${JSON.stringify(model).replace(/'/g, "&apos;")}' id="open-overlay_${model.id}" onclick="handleViewDeal(this)">
                            <i class="fas fa-eye"></i>View</button>
                        </div>
                    </div>
                `;

          $(".catalogue-grid").append(carCard);

        });
      });
    }
  });

 
$("#overlay").on("click", function (e) {
    if ($(e.target).is("#overlay")) {
      $(this).fadeOut();
    }
  });
  
});

async function handleViewDeal(button) {
  const car_id = button.id.split("_")[1];
  const url = `/api/v1/models`;
  const response = await fetch(url);
  const data = await response.json();
  const car = data.find((item) => item.id == car_id);

  const overlay = document.getElementById("overlay");
  const overlay_content = document.getElementById("overlay-content");
  overlay_content.innerHTML = `
            <button id="close-overlay"><i class="fas fa-times"></i></button>
            <img class="car-img" src="${car.img_path}" alt="Car Image">
            <h2 class="car-title">${car.name} - ${car.year}</h2>
            <h3 class="car-description">${car.manufacturer_name}</h3>
            
            <ul class="car-specs">
                <li><strong><i class="fas fa-tachometer-alt"></i> Zero To Sixty: </strong> <span id="mileage">${car.ZeroToSixty}</span> Seconds</li>
                <li><strong><i class="fas fa-cogs"></i> Capacity: </strong> <span id="engine">${car.engine_capacity} cc</span></li>
                <li><strong><i class="fas fa-exchange-alt"></i> Transmission: </strong> <span id="transmission">${car.transmission}</span></li>
                <li><strong><i class="fas fa-gas-pump"></i> Fuel Type: </strong> <span id="fuel-type">${car.fuel}</span></li>
            </ul>
            <div class="car-price">
                <h3 id="TheFinalPrice">Price: <span id="price">&pound;${car.base_price}</span></h3>
            </div>
            <button id="calculate-cost" car_id="${car_id}" onclick="CalculatePrice(this)"><i class="fas fa-calculator"></i> Calculate Shipping</button>
`;
  overlay.style.display = "flex";
  console.log({ car });
}

async function CalculatePrice(button) {
    

    console.log('Meee!')

    const car_id = button.getAttribute("car_id");

    const url = `/api/v1/calculate/${car_id}`


    $.get(url, function (data) {

        console.log('Here!')
        price = data.price
        base_no = `Price: Kes ${price}`
        $('#TheFinalPrice').html(base_no)
        console.log(base_no)

    })

    
}
