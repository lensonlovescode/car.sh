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
$('button #search_button').on('click', function () {
    console.log("Workin!")
    console.log($('#make').val());
    console.log($('#category').val());
    if ($('#make').val() !== "None" || $('#category').val() !== "None")
    {
        const Make = $('#make').val()
        const Category = $('#category').val()

        const url = "http://localhost:5001/api/v1/models/" + "Make/" + "Category"

        $.get(url, function (data) {
            $.each(data, function (index, model) {

            })
        })

    }
});
