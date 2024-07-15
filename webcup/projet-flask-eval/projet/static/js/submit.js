$(document).ready(function() {
    $('#paiement').submit(function(event) {
        event.preventDefault();

        var formData = new FormData($(this)[0]);

        $.ajax({
            url: '/payer-devis',
            type: 'POST',
            dataType: 'json',
            processData: false,
            contentType:false,
            data: formData,
            success: function(response) {
                swal("Hey, Good job !!", response.message, "success")
            },
            error: function(xhr, status, error) {
                sweetAlert("Oops...", xhr.responseJSON.error, "error")
            }
        });

    });
});

