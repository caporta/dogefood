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
                $('#js--pet-form-target').append(data);
            },
            error: function (xhr) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    function updatePet(primaryKey) {
        $.ajax({
            url: 'pet/update/' + primaryKey,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'name': $('#id_name').val(),
                'pet_type': $('#id_pet_type').val(),
                'breed': $('#id_breed').val(),
                'sex': $('input[id^=id_sex_]:checked').val(),
                'age': $('#id_age').val(),
                'weight': $('#id_weight').val()
            },

            success: function (data) {
                console.log(data);
            },
            error: function (xhr) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    $('div[id^=js--pet-info-panel-]').on('click', 'a[id^=js--get-pet-form-]', function (e) {
        var pk = $(this).attr('id').split('-')[5];
        console.log(pk); //sanity check
        e.preventDefault();
        getPetForm(pk);
    });


    $('body').on('submit', '#pet-form', function (e) {
        e.preventDefault();
        console.log('form-submitted');
        var pk = $(this).attr('action').split('/')[2];
        updatePet(pk);
    });

    $('body').on('hidden.bs.modal', '.modal', function () {
        $(this).removeData('bs.modal');
    });

})();
