
$(document).ready(function(){
    console.log("loaded");
    $.material.init();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        })
    });

    $(document).on("submit", "#Login-form", function(e){
        e.preventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == 'error'){
                    console.log(res);
                    alert("Not able to log in")
                }else{
                    console.log("Logged in as ", res);
                    window.location.href = "/";
                    }

            }
        })
    });

    $(document).on("click", "#logout-link", function(e){
        e.preventDefault();
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(res){
                if(res == 'User logged out successfully'){
                   console.log("User logged out ", res);
                   window.location.href = "/login";
                } else{
                    alert("Something went wrong while logging out")
                }

            }
        })
    });

    $(document).on("submit", "#post-activity", function(e){
        e.preventDefault();
        form = $(this).serialize();
        console.log(form);
        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function(res){
                console.log("data has been pushed", res);
            }
        });


    });



});

