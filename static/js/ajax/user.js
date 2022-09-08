"use strict";
const UserCreate = (function () {
    let user_form;
    return {
        init: function () {
            user_form = document.querySelector("#user_form");
            const submitButton = document.getElementById('admin_submit');
            const password = document.querySelector('input[name=password]');
            const retype_password = document.querySelector('input[name=retype_password]');

            if (confirm.value === password.value) {
                confirm.setCustomValidity('');
                submitButton.addEventListener('click', function (e) {
                    e.preventDefault();
                    let form = $('#user_form')[0];
                    let formData = new FormData(form);
                    $.ajax({
                        type: "POST",
                        url: 'create',
                        data: formData,
                        datatype: 'json',
                        processData: false,
                        contentType: false,
                        success: function (response) {
                            if (response.send === 1) {
                                $("#user_form").trigger("reset");
                            } else {
                                alert(response.message);
                            }
                        }
                    });
                });
            } else {
                confirm.setCustomValidity('Passwords do not match');
            }
        }
    }
});


kp.onDOMContentLoaded = function () {
    UserCreate.init();
}