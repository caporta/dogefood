'use strict';


window.Dogefood = {};

(function() {

    Dogefood.constructors = {};

    Dogefood.constructors.PetForm = function () {
        var that = this;

        this.getForm = function (primaryKey, crudAction) {
            var action = crudAction.toLowerCase();
            $.ajax({
                url: 'pet/' + action + '/' + primaryKey,
                type: 'GET',

                success: function (data) {
                    $('#js--pet-form-target').append(data);

                    if (action == 'delete') {
                        $('#js--pet-form-target').append(data);
                        $('body').on('click', '#js--cancel-delete', function (e) {
                            $('#js--pet-form-modal').modal('hide');
                        });
                    }
                },
                error: function (xhr) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            });
        };

        this.updatePet = function (primaryKey) {
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
                    $('#js--pet-form-modal').modal('hide');
                    $('#js--pet-info-panel-' + primaryKey + ' .js--pet-name').html(
                        '<h4 class="panel-title">' + data['name'] + '</h4>'
                    );
                    $('#js--pet-info-panel-' + primaryKey + ' .js--pet-stats').html(
                        '<p class="panel-text">Breed: ' + data['breed'] + '</p>' +
                        '<p class="panel-text">Sex: ' + data['sex'] + '</p>' +
                        '<p class="panel-text">Age: ' + data['age'] + '</p>' +
                        '<p class="panel-text">Weight: ' + data['weight'] + 'lbs.</p>'
                    );
                },
                error: function (xhr) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            });
        };

        this.deletePet = function (primaryKey) {
            $.ajax({
                url: 'pet/delete/' + primaryKey,
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                },

                success: function (data) {
                    $('#js--pet-form-modal').modal('hide');
                    $('#js--pet-info-panel-' + primaryKey).hide();
                },
                error: function (xhr) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            });
        };

        this.bindGetOnClick = function (target, crudAction) {
            $('div[id^=js--pet-info-panel-]').on('click', target, function (e) {
                var pk = $(this).attr('id').split('-')[5];
                e.preventDefault();
                that.getForm(pk, crudAction);
            });
        };

        this.bindPostOnSubmit = function (target, crudAction) {
            $('body').on('submit', target, function (e) {
                e.preventDefault();
                var pk = $(this).attr('action').split('/')[2];
                if (crudAction.toLowerCase() == 'update') {
                    that.updatePet(pk);
                } else if (crudAction.toLowerCase() == 'delete') {
                    that.deletePet(pk);
                } else {
                    console.log(action + 'is invalid.');
                }
            });
        };

        this.dumpModalContents = function () {
            $('body').on('hidden.bs.modal', '.modal', function () {
                $(this).removeData('bs.modal');
            });
        };

    };

    var petForm = new Dogefood.constructors.PetForm();
    petForm.bindGetOnClick('a[id^=js--get-pet-form-]', 'update');
    petForm.bindGetOnClick('a[id^=js--delete-pet-conf-]', 'delete');
    petForm.bindPostOnSubmit('#pet-form', 'update');
    petForm.bindPostOnSubmit('#delete-pet', 'delete');
    petForm.dumpModalContents();

})();
