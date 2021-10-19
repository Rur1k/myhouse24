


$("#id-house-flat").change(function () {
      var url_section = $("#FlatCreateForm").attr("data-section-url");
      var url_floor = $("#FlatCreateForm").attr("data-floor-url");
      var houseId = $(this).val();

      $.ajax({
        url: url_section,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-section-flat").html(data);
        }
      });
      $.ajax({
        url: url_floor,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-floor-flat").html(data);
        }
      });
    });

$("#HouseSearch").change(function () {
      var url_section = $("#FlatTable").attr("data-section-url");
      var url_floor = $("#FlatTable").attr("data-floor-url");
      var houseId = $(this).val();

      $.ajax({
        url: url_section,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#SectionSearch").html(data);
        }
      });
      $.ajax({
        url: url_floor,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#FloorSearch").html(data);
        }
      });
    });



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


