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


$('#search_button').on('click', function () {

    const Make = $('#make').val();
    const Category = $('#category').val();
    const Model = $('#model').val();

    if ($('#make').val() !== "None" || $('#category').val() !== "None")
    {
        let url = `http://localhost:5001/api/v1/makes/${Make}/${Category}`;
        $('.global-catalogue-container').empty(); 
        $.get(url, function (data) {
            $.each(data, function (index, model) {

            // starts here

            let carCard = `
                    <div class="car-card">
                        <img class="car-img" src="../static/images/default.jpg">
                        <div class="car-card-contents">
                            <h4 class="car-card-title">${model.year} ${model.manufacturer}</h4>
                            <h3 class="car-description">${model.name}</h3>
                            <h6 class="car-card-info">
                                <ul class="car-specs">
                                    <li class="engine-capacity">${model.engine_capacity} litres</li>
                                    <li class="transmission">${model.ignition}</li>
                                    <li class="fuel-type">${model.fuel_type}</li>
                                </ul>
                            </h6>
                        </div>
                        <div class="car-card-cost">
                            <h3 class="car-card-cash">Base Price</h3>
                            <h3 class="car-card-total">Ksh. ${model.base_price}</h3>
                            <button class="view-deal-button">View deal</button>
                        </div>
                    </div>
                `;

                $('.global-catalogue-container').append(carCard);

            // ends here

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

});

