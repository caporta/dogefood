'use strict';


window.Dogefood = {};

(function() {

    Dogefood.constructors = {};
    console.log("Hello World!"); //sanity check

    function getPetForm(primaryKey) {
        $.ajax({
            url: 'pet/update/' + primaryKey,
            type: 'GET',

            success: function (data) {
                $('#js--pet-form-target').empty().append(data);
            }
        });
    }

    $('div[id^=js--pet-info-panel-]').on('click', 'a[id^=js--get-pet-form-]', function (e) {
        var pk = $(this).attr('id').split('-')[5];
        console.log(pk); //sanity check
        e.preventDefault();
        getPetForm(pk);
    });

    $('body').on('hidden.bs.modal', '.modal', function () {
        $(this).removeData('bs.modal');
    });

})();