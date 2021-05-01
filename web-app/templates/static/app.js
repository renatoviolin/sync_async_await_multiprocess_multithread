$(document).ready(function () {
    $('#btn-sync').on('click', function () {
        $.ajax({
            url: '/easy_sync',
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                sleep: $('#input-sleep').val(),
                n_requests: $('#input-requests').val()
            }),
            beforeSend: function () {
                $(".overlay").show()
            },
        }).done(function (jsondata, textStatus, jqXHR) {
            result = jsondata['result']
            time = jsondata['time']
            r = time + '<br><br>'
            for (i = 0; i < result.length; i++) {
                r += result[i] + '<br>'
            }
            $("#result-sync").html(r)
            $(".overlay").hide()
        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            $(".overlay").hide()
        });

    })

    $('#btn-async').on('click', function () {
        $.ajax({
            url: '/easy_async',
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                sleep: $('#input-sleep').val(),
                n_requests: $('#input-requests').val()
            }),
            beforeSend: function () {
                $(".overlay").show()
            },
        }).done(function (jsondata, textStatus, jqXHR) {
            result = jsondata['result']
            time = jsondata['time']

            r = time + '<br><br>'
            for (i = 0; i < result.length; i++) {
                r += result[i]['result'] + '<br>'
            }
            $("#result-async").html(r)
            $(".overlay").hide()
        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            $(".overlay").hide()
        });
    })

    $('#btn-mp').on('click', function () {
        $.ajax({
            url: '/easy_multiprocess',
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                sleep: $('#input-sleep').val(),
                n_requests: $('#input-requests').val()
            }),
            beforeSend: function () {
                $(".overlay").show()
            },
        }).done(function (jsondata, textStatus, jqXHR) {
            result = jsondata['result']
            time = jsondata['time']
            r = time + '<br><br>'
            for (i = 0; i < result.length; i++) {
                r += result[i] + '<br>'
            }
            $("#result-mp").html(r)
            $(".overlay").hide()
        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            $(".overlay").hide()
        });
    })

    $('#btn-mt').on('click', function () {
        $.ajax({
            url: '/easy_multithread',
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                sleep: $('#input-sleep').val(),
                n_requests: $('#input-requests').val()
            }),
            beforeSend: function () {
                $(".overlay").show()
            },
        }).done(function (jsondata, textStatus, jqXHR) {
            result = jsondata['result']
            time = jsondata['time']

            r = time + '<br><br>'
            for (i = 0; i < result.length; i++) {
                r += result[i] + '<br>'
            }
            $("#result-mt").html(r)
            $(".overlay").hide()
        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            $(".overlay").hide()
        });
    })


    //----------------------------- HEAVY WORKLOAD ---------------------------------
    $('#btn-heavy-single').on('click', function () {
        $.ajax({
            url: '/heavy_single',
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                n_jobs: $('#input-jobs').val()
            }),
            beforeSend: function () {
                $(".overlay").show()
            },
        }).done(function (jsondata, textStatus, jqXHR) {
            result = jsondata['result']
            time = jsondata['time']

            r = time + '<br><br>'
            for (i = 0; i < result.length; i++) {
                r += result[i] + '<br>'
            }
            $("#result-heavy-single").html(r)
            $(".overlay").hide()
        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            $(".overlay").hide()
        });
    })

    $('#btn-heavy-mp').on('click', function () {
        $.ajax({
            url: '/heavy_process',
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                n_jobs: $('#input-jobs').val()
            }),
            beforeSend: function () {
                $(".overlay").show()
            },
        }).done(function (jsondata, textStatus, jqXHR) {
            result = jsondata['result']
            time = jsondata['time']

            r = time + '<br><br>'
            for (i = 0; i < result.length; i++) {
                r += result[i] + '<br>'
            }
            $("#result-heavy-mp").html(r)
            $(".overlay").hide()
        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            $(".overlay").hide()
        });
    })

    $('#btn-heavy-mt').on('click', function () {
        $.ajax({
            url: '/heavy_thread',
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                n_jobs: $('#input-jobs').val()
            }),
            beforeSend: function () {
                $(".overlay").show()
            },
        }).done(function (jsondata, textStatus, jqXHR) {
            result = jsondata['result']
            time = jsondata['time']

            r = time + '<br><br>'
            for (i = 0; i < result.length; i++) {
                r += result[i] + '<br>'
            }
            $("#result-heavy-mt").html(r)
            $(".overlay").hide()
        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            $(".overlay").hide()
        });
    })
})