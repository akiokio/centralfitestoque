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

        common.setLoadings();
    },
    datepickerInit: function(){
        $('#dataInicio').datepicker();
        $('#dataFim').datepicker();
    }
  };

})();

$(document).ready(common.init);