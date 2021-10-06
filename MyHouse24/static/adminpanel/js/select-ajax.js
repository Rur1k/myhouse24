//$("#id_setting_tariff_service-0-service").change(function () {
//      var url = $("#TariffCreateForm").attr("data-unit-url");  // get the url of the load_cities view
//      var serviceId = $(this).val();  // get the selected country ID from the HTML input
//
//      $.ajax({                       // initialize an AJAX request
//        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
//        data: {
//          'service': serviceId       // add the country id to the GET parameters
//        },
//        success: function (data) {   // data is the return of the load_cities view function
//          $("#id_setting_tariff_service-0-unit_service").html(data);  // replace the contents of the city input with the data that came from the server
//        }
//      });
//    });

function SelectServiceUnit(select){
    var url = $("#TariffCreateForm").attr("data-unit-url");  // get the url of the load_cities view
      var serviceId = $(select).val();  // get the selected country ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'service': serviceId       // add the country id to the GET parameters
        },
        success: function (data) {   // data is the return of the load_cities view function
          $(select).closest(".form-setting_tariff_service").children(".select-service-unit").find("select").html(data);  // replace the contents of the city input with the data that came from the server
        }
      });
}


