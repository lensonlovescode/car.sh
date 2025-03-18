$.get("http://localhost:5001/api/v1/makes", function(data){
    $.each(data, function (index, make){
        let option = $('<option></option>').text(make.name)
        option.val(make.name)
        $('#make').append(option)
        console.log(make.name);
    })
});
$.get("http://localhost:5001/api/v1/categories", function(data){
    $.each(data, function (index, category){
        let option = $('<option></option>').text(category.name)
        option.val(category.name)
        $('#category').append(option)
        console.log(category.name);
    })
});