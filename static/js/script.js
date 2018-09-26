function requestAmbiente() {

    console.log("Inicializando consulta!")
    if ($('#id_bloco option:selected').text() !== "Selecione Bloco") {
        $.ajax({
            url: "../requestambiente/",
            type: "POST", // http method
            data: {id_bloco: $('#id_bloco').val()},


            success: function (json) {
                console.log(json);
                $('#id_ambiente').empty();
                if (json.length>=0){
                    $('#id_ambiente').append(new Option("Selecione Ambiente", ""))}
                for (var i = 0; i <= json.length; i++) {
                    $("#id_ambiente").prepend("<option value=" + json[i.toString()].id + ">" + json[i.toString()].nome + "</option>");
                }
                console.log("success");
            },


            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>");
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    } else {
        $('#id_ambiente').empty();
        $('#id_ambiente').append(new Option("--------", ""))
        $("#controleAcesso").find('input, textarea, button, select').attr('disabled', 'disabled');
        return;
    };
};


function Menu() {
    try {
        pagina = document.getElementById("controle_menu").value;
        document.getElementById(pagina).className = 'item active';
    }
    catch (err) {
        document.getElementById("error_js").value = err.message;
    }
}


$(document).ready(function () {

    if ($('#serviceMessenger').val() !== "") {
        $('.ui.modal').modal('show')
    };

    $('#id_cpf').mask('000.000.000-00', {reverse: true});

    $('#id_turno option:contains("--------")').text('Selecione Periodo');
    $('#id_data option:contains("--------")').text('Selecione Dia(as)');
    $('#id_ambiente').change(function () {
        if($("#id_ambiente option:selected").text() !== "Selecione Ambiente" ){
            $("#controleAcesso").find('input, textarea, button, select').removeAttr('disabled')}
        else {
            $("#controleAcesso").find('input, textarea, button, select').attr('disabled', 'disabled')}
    });

 
});





