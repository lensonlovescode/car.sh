$(document).ready(function () {
    $.get('http://localhost:5001/api/v1/status', function (data) {
        console.log(data.status);
    });
});
