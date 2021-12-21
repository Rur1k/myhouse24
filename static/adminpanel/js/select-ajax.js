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

// Выбор всех услуг по ТП.
$('#add_service_on_tariff').click(function() {
    var id_tariff = $("#id_tariff").val();
    var url = $("#InvoiceCreateForm").attr("data-tariff-url");
    if (id_tariff) {
        $.ajax({
            url: url,
            data: {
                'id_tariff': id_tariff
            },
            success: function(data){
                $('#formset_service_invoice').html(data);
                var service_count = $('#formset_service_invoice').children('.form-service-invoice').length;
                $('#id_service_invoice-TOTAL_FORMS').val(service_count);
            }
        });

    } else {
        alert('Тарифный план не выбран');
    }
});

$('#add_counter_data_inv').click(function() {
    var url_counter = $("#InvoiceCreateForm").attr("data-counter-inv-url");
    var url_id_counter = $("#InvoiceCreateForm").attr("data-counter-id-url");
    var flat = $("#id-flat-invoice").val();
    var counter_count = $('#id_service_invoice-TOTAL_FORMS').val();
    var array = []

    for (var i=0; i<counter_count; i++){
        var service = $('#id_service_invoice-'+i+'-service').val()
        $.ajax({
            url: url_counter,
            async: false,
            data: {
                'counter': service,
                'flat': flat,
            },
            success: function(data){
                $('#id_service_invoice-'+(i)+'-consumption').val(data);
                MultiplicationInvoice()
            }
        });
        $.ajax({
            url: url_id_counter,
            async: false,
            data: {
                'counter': service,
                'flat': flat,
            },
            success: function(data){
                array.push(data);
            }
        });
    }
    $('#list_counter_id').val(array);
});

// Квартиры по пользователю
$("#id-master-owner").change(function () {
      var url = $("#RequestCreateForm").attr("data-flat-master-url");
      var ownerId = $(this).val();

      $.ajax({
        url: url,
        data: {
          'owner': ownerId
        },
        success: function (data) {
          $("#id-master-flat").html(data);
          $("#id-master-flat").selectpicker("refresh");
        }
      });
    });

// Отбор пользователей для отправки сообщений
// Отбор по дому всего
$("#id-message-house").change(function () {
      var url_section = $("#MessageCreateForm").attr("data-section-url");
      var url_floor = $("#MessageCreateForm").attr("data-floor-url");
      var url_flat = $("#MessageCreateForm").attr("data-flat-url");
      var houseId = $(this).val();

      $.ajax({
        url: url_section,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-message-section").html(data);
        }
      });
      $.ajax({
        url: url_floor,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-message-floor").html(data);
        }
      });
      $.ajax({
        url: url_flat,
        data: {
          'house': houseId
        },
        success: function (data) {
          $("#id-message-flat").html(data);
        }
      });
    });

$("#id-message-section").change(function () {
      var url_flat = $("#MessageCreateForm").attr("data-flat-url-section");
      var sectionId = $(this).val();

      $.ajax({
        url: url_flat,
        data: {
          'section': sectionId
        },
        success: function (data) {
          $("#id-message-flat").html(data);
        }
      });
    });

$("#id-message-floor").change(function () {
      var url_flat = $("#MessageCreateForm").attr("data-flat-url-floor");
      var floorId = $(this).val();

      $.ajax({
        url: url_flat,
        data: {
          'floor': floorId
        },
        success: function (data) {
          $("#id-message-flat").html(data);
        }
      });
    });

// Вытягивание Роли по пользователю
function SelectPersonalRole(select){
    var url = $("#HouseCreateForm").attr("url-personal-role");
        var userId = $(select).val();

        $.ajax({
          url: url,
          data: {
            'user': userId
          },
          success: function (data) {
            $(select).closest(".form-personal").find("input[type='text']").val(data);
          }
        });
};
