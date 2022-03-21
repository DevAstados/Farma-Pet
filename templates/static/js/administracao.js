/*$(document).ready(function() {
  $('.nav-link-collapse').on('click', function() {
    $('.nav-link-collapse').not(this).removeClass('nav-link-show');
    $(this).toggleClass('nav-link-show');
  });
});*/

// Exibe criação de uma nova categoria

function onClickNovaCategoria(element) {
    if (element == 'toggle-control-categoria') {
        $("#categoria-nome").show();
        $("#categoria-select").hide();
        $(".toggle-control-categoria").hide();
        $(".toggle-control-categoria-cancel").show();

    } else {
        $("#categoria-nome").hide();
        $("#categoria-select").show();
        $(".toggle-control-categoria").show();
        $(".toggle-control-categoria-cancel").hide();
    }
}

function onClickNovaMarca(element) {
    if (element == 'toggle-control-marca') {
        $("#marca-nome").show();
        $("#marca-select").hide();
        $(".toggle-control-marca").hide();
        $(".toggle-control-marca-cancel").show();

    } else {
        $("#marca-nome").hide();
        $("#marca-select").show();
        $(".toggle-control-marca").show();
        $(".toggle-control-marca-cancel").hide();
    }
}


function onClickAlterarCategoriaMarca(element) {
    if (element == 'toggle-control-marca') {
        $("#marca-nome").show();
        $("#marca-select").hide();
        $(".toggle-control-marca").hide();
        $(".toggle-control-marca-cancel").show();

    } else {
        $("#marca-nome").hide();
        $("#marca-select").show();
        $(".toggle-control-marca").show();
        $(".toggle-control-marca-cancel").hide();
    }
}

