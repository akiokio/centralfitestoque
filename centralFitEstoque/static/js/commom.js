/**
 * Created with PyCharm.
 * User: akiokio
 * Date: 17/06/13
 * Time: 14:17
 * To change this template use File | Settings | File Templates.
 */

var common = (function () {

  return {
    init: function () {
        common.datepickerInit();
        common.filtrarFaturamento();
    },
    datepickerInit: function(){
        $('#dataInicio').datepicker();
        $('#dataFim').datepicker();
    },

    filtrarFaturamento: function(){
        $('#importarProdutos').on('click', function(){
            if ($('#dataInicio').val() == 'Insira a data' || $('#dataInicio').val() == 'Insira a data'){
                alert('Insira uma data');
                return false;
            }
            var postData = {
                'dataInicio': $('#dataInicio').val(),
                'dataFim': $('#dataFim').val()
            }
            $("#Loading").fadeIn(); //show when submitting
            $('#tabela_faturamento tbody').empty();
            $.post('/filtrar/faturamento/', postData, function(data){
                var parsedData = $.parseJSON(data);

                for(var i=0; i < parsedData.length; i++){
                    data_string = '<tr class="">';
                    for(var j=0; j < parsedData[i].length; j++){
                        data_string += '<td>' + parsedData[i][j] + '</td>';
                    };
                    data_string += '</tr>';
//                    Append a linha na tabela
                    $('#tabela_faturamento tbody').append(data_string);
                    $("#Loading").fadeOut('slow'); //hide when data's ready
                }
            });
        });
    }
  };

})();

$(document).ready(common.init);