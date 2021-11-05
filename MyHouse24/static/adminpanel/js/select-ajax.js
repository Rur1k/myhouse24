// Связные списки для создания объекта квартиры
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

// Связные списки для создания объекта ЛС
$("#id-house-account").change(function () {
      var url_section = $("#AccountCreateForm").attr("data-section-url");
      var url_flat = $("#AccountCreateForm").attr("data-flat-url");
      var houseId = $(this).val();

      $.ajax({
        url: url_section,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-section-account").html(data);
        }
      });
      $.ajax({
        url: url_flat,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-flat-account").html(data);
        }
      });
    });

// Сортировка квартиры по секции
$("#id-section-account").change(function () {
      var url = $("#AccountCreateForm").attr("data-order-flat-url");
      var sectionId = $(this).val();

      $.ajax({
        url: url,
        data: {
          'section': sectionId
        },
        success: function (data) {
          $("#id-flat-account").html(data);
        }
      });
    });

// Вытягивает владельца и номер телефона по квартире
$("#id-flat-account").change(function () {
      var url_username = $("#AccountCreateForm").attr("data-username-url");
      var url_phone = $("#AccountCreateForm").attr("data-phone-url");
      var flatId = $(this).val();

      $.ajax({
        url: url_username,
        data: {
          'flat': flatId
        },
        success: function (data) {
          $("#user-fullname").html(data);
        }
      });
      $.ajax({
        url: url_phone,
        data: {
          'flat': flatId
        },
        success: function (data) {
          $("#user-phone").html(data);
        }
      });
    });

// Вытягивает владельца и номер телефона по квартире
$("#id-flat-invoice").change(function () {
      var url_username = $("#InvoiceCreateForm").attr("data-username-url");
      var url_phone = $("#InvoiceCreateForm").attr("data-phone-url");
      var url_account = $("#InvoiceCreateForm").attr("data-account-url");
      var flatId = $(this).val();

      $.ajax({
        url: url_username,
        data: {
          'flat': flatId
        },
        success: function (data) {
          $("#user-fullname").html(data);
        }
      });
      $.ajax({
        url: url_phone,
        data: {
          'flat': flatId
        },
        success: function (data) {
          $("#user-phone").html(data);
        }
      });
      $.ajax({
        url: url_account,
        data: {
          'flat': flatId
        },
        success: function (data) {
            console.log('Бла бла бла')
          $("#id-account-invoice").val(data);
        }
      });
    });


// Сортировка для поиска по таблице квартир
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


// Вытягивает показатель еденицы измирения
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

function SelectServiceUnitIsInvoice(select){
    var url = $("#InvoiceCreateForm").attr("data-unit-url");  // get the url of the load_cities view
      var serviceId = $(select).val();  // get the selected country ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'service': serviceId       // add the country id to the GET parameters
        },
        success: function (data) {   // data is the return of the load_cities view function
          $(select).closest(".form-service-invoice").children(".select-invoice-unit").find("select").html(data);  // replace the contents of the city input with the data that came from the server
        }
      });
}

// Выбор ЛС по пользователю в "Касса" - создание прихода
$("#id-owner-trans").change(function () {
      var url = $("#AccountTransactionCreateForm").attr("data-account-url");
      var ownerId = $(this).val();

      $.ajax({
        url: url,
        data: {
          'owner': ownerId
        },
        success: function (data) {
            $("#id-account-trans").html(data);
            $("#id-account-trans").selectpicker("refresh");
            console.log(data);
        }
      });
    });

// Связные списки для создания объекта показания счетчика
$("#id-house-counter").change(function () {
      var url_section = $("#CounterDataCreateForm").attr("data-section-url");
      var url_flat = $("#CounterDataCreateForm").attr("data-flat-url");
      var houseId = $(this).val();

      $.ajax({
        url: url_section,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-section-counter").html(data);
        }
      });
      $.ajax({
        url: url_flat,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-flat-counter").html(data);
        }
      });
    });

// Связные списки для создания объекта показания счетчика
$("#id-house-invoice").change(function () {
      var url_section = $("#InvoiceCreateForm").attr("data-section-url");
      var url_flat = $("#InvoiceCreateForm").attr("data-flat-url");
      var houseId = $(this).val();

      $.ajax({
        url: url_section,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-section-invoice").html(data);
        }
      });
      $.ajax({
        url: url_flat,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-flat-invoice").html(data);
        }
      });
    });

// Сортировка квартиры по секции
$("#id-section-counter").change(function () {
      var url = $("#CounterDataCreateForm").attr("data-order-flat-url");
      var sectionId = $(this).val();

      $.ajax({
        url: url,
        data: {
          'section': sectionId
        },
        success: function (data) {
          $("#id-flat-counter").html(data);
        }
      });
    });

$("#id-section-invoice").change(function () {
      var url = $("#InvoiceCreateForm").attr("data-order-flat-url");
      var sectionId = $(this).val();

      $.ajax({
        url: url,
        data: {
          'section': sectionId
        },
        success: function (data) {
          $("#id-flat-invoice").html(data);
        }
      });
    });


