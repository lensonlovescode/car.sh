$(document).ready(function () {

$.get("http://localhost:5001/api/v1/makes", function(data){
    $.each(data, function (index, make){
        let option = $('<option></option>').text(make.name)
        option.val(make.name)
        $('#make').append(option)
    })
});

$.get("http://localhost:5001/api/v1/categories", function(data){
    $.each(data, function (index, category){
        let option = $('<option></option>').text(category.name)
        option.val(category.name)
        $('#category').append(option)
    })
});

$("#make, #category").change(function () {

    $('#model').empty().append('<option value="">Model</option>');

    const Make = $('#make').val()
    const Category = $('#category').val()

    if (Make === "None" || Category === "None") {
        return;
    }

    if (Make && Category) {
        
        let url = `http://localhost:5001/api/v1/makes/${Make}/${Category}`;
        console.log(url)
        $.get(url, function (data) {
            $.each(data, function (index, model) {
                let option = $('<option></option>').text(model.name)
                option.val(model.name);
                $('#model').append(option);
                console.log(option.val())
            });
        });
    }
});

$("#open-overlay").on("click", function () {
    $("#overlay").fadeIn();
});

$("#close-overlay").on("click", function () {
    $("#overlay").fadeOut();
});

$("#overlay").on("click", function (e) {
    if ($(e.target).is("#overlay")) { 
        $(this).fadeOut();
    }
});

$('#search_button').on('click', function () {

    const Make = $('#make').val();
    const Category = $('#category').val();
    const Model = $('#model').val();

    if ($('#make').val() !== "None" || $('#category').val() !== "None")
    {
        let url = `http://localhost:5001/api/v1/makes/${Make}/${Category}`;
        $('.catalogue-grid').empty(); 
        $.get(url, function (data) {
            $.each(data, function (index, model) {

            // starts here

            let carCard = `
                    <div class="car-card">
                        <div class="car-image">
                            <img class="car-img" src="../static/images/mercedes.jpg">
                        </div>

                        <div class="car-card-contents">
                            <h4 class="car-card-title">${model.year} ${model.manufacturer}</h4>
                            <h3 class="car-description">${model.name}</h3>
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
                            <h3 class="car-card-total">$. ${model.base_price}</h3>
                            <button class="view-deal-button" id="open-overlay"><i class="fas fa-eye"></i>View deal</button>
                        </div>
                    </div>
                `;

                $('.catalogue-grid').append(carCard);

            // ends here

            });
        });
    }
});


});

