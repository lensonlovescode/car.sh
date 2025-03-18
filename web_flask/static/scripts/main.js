$(document).ready(function () {
    $.get('https://127.0.0.1/api/v1/status', function (data) {
        console.log(data.status);
    });
});
