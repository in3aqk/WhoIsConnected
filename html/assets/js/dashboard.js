/**
 * Who is connected
 *
 * Remoterig who is connected
 ** This is not a free software please read the licence!!
 * @package		WhoIsConneccted
 * @author		Mattiolo Paolo
 * @copyright	Copyright (c) 2020, Mattiolo Paolo 
 */

var dialog_delete;
var dialog_update;
var head_id;


/**
 * When all starts
 */
$(document).ready(function () {

    dialog_update = $("#dialog_edit_head").dialog({
        autoOpen: false,
        height: "auto",
        width: "auto",
        modal: true,
        buttons: {
            "Modify User": function () {
                do_modify_head(head_id);
                $(this).dialog("close");
            },
            Cancel: function () {
                $(this).dialog("close");
            }
        }
    });

    dialog_update.dialog("close");


    dialog_delete = $("#dialog").dialog({
        resizable: false,
        height: "auto",
        width: "auto",
        modal: true,
        buttons: {
            "Delete user": function () {
                $(this).dialog("close");
                do_delete_head(head_id)
            },
            Cancel: function () {
                $(this).dialog("close");
            }
        }
    });

    dialog_delete.dialog("close");

    set_dialog_delete();

});


function set_dialog_delete() {
    dialog_txt = '<p><span class=\"ui-icon ui-icon-alert\" style="float:left; margin:12px 12px 20px 0;\">' +
        '</span>Delete remote rig user. Are you sure?</p>'
    $("#dialog").html(dialog_txt);

}

function delete_head(id) {
    head_id = id;
    dialog_delete.dialog("open");
}

function modify_head(id, name) {    
    head_id = id;
    $('#name').val(name);
    dialog_update.dialog("open");
}


function do_delete_head(id) {
    $.ajax({
        url: '/delete/' + id,
        cache: false,
        dataType: 'html',
        success: function (result) {
            console.log(result);
            location.reload();
        },
        error: function (error) {
            alert('Error deleting Head');
        }
    });
}


function do_modify_head(id) {
    new_name = $('#name').val();
    if(new_name){
        $.ajax({
            url: '/update/' + id + '/' + new_name.toUpperCase(),
            cache: false,
            dataType: 'html',
            success: function (result) {
                console.log(result);
                location.reload();
            },
            error: function (error) {
                alert('Error deleting Head');
            }
        });

    }

}

