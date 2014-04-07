$(document).ready(function () {
    var event_remove_handler = function () { // Click Event on jpf
        var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        r = confirm('Êtes-vous sur de vouloir supprimer l\'évenement ?\n(Attention tous les albums associés seront supprimés !)');
        if (r == false) {
            return false;
        }
        post_data = {
            'event_id': $(this).attr("value"),
            'csrftoken': csrftoken
        }
        $.ajax({ // Ajax request
            url: "/backoffice/event/delete/",
            type: 'POST',
            data: post_data,
            crossDomain: false,
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }).done(function (data) {
            data = JSON.parse(data);
            if (data.success) {
                $('#event_' + data.event_id).remove();
                $.notify("Event supprimé", "success");
            } else {
                $.notify(data.message, "error");
            }
        }).fail(function (data) {
            $.notify("An error occured.", "error");
        });
        return false;
    };

    $('.event_delete').off('click').on('click', event_remove_handler);
    $('.event_edit').off('click').on('click', function() {document.location.href="/backoffice/event/edit/"+$(this).attr("value")});
})