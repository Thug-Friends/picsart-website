$(document).ready(function () {
    var album_remove_handler = function () { // Click Event on jpf
        var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        r = confirm('Êtes-vous sur de vouloir supprimer l\'album ?');
        if (r == false) {
            return false;
        }
        post_data = {
            'album_id': $(this).attr("value"),
            'csrftoken': csrftoken
        }
        $.ajax({ // Ajax request
            url: "/backoffice/album/delete/",
            type: 'POST',
            data: post_data,
            crossDomain: false,
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }).done(function (data) {
            data = JSON.parse(data);
            if (data.success) {
                $('#album_' + data.album_id).remove();
                $.notify("Album supprimé", "success");
            } else {
                $.notify(data.message, "error");
            }
        }).fail(function (data) {
            $.notify("An error occured.", "error");
        });
        return false;
    };

    $('.album_delete').off('click').on('click', album_remove_handler);
    $('.album_edit').off('click').on('click', function() {document.location.href="/backoffice/album/edit/"+$(this).attr("value")});
})