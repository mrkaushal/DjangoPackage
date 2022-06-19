"use strict";
const UserCreate = (function () {
    let user_form, i;
    return {
        init: function () {
            user_form = document.querySelector("#user_form");
            const submitButton = document.getElementById('admin_submit');
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
                        if (response.status === 1) {
                            window.location.href = '/cbvApp/list';
                        } else {
                            alert(response.message);
                        }
                    }
                });
            });
        }
    }
});


kp.onDOMContentLoaded = function () {
    UserCreate.init();
}