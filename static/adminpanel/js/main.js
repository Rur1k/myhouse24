$("document").ready(function() {
    $('#CounterSearch').trigger('change')

    // подсчет суммы квитанции в квитанциях
    var sum = 0;
    $('.info_sum').each(function(){
        sum += parseFloat($(this).text());
    });
    $('#total_info_invoice').html(sum);

    MultiplicationInvoice()
    // Инициализация DataTable
    //FilterBase('#AccountTransactionTable', [0,1,5], [2,3,4,6], [7,8])



    var table = $('#AccountTransactionTable').DataTable();
    FilterDate(table)

    $('#min, #max').select(function () {
        table.draw();
    });
});

function FilterDate(table) {
    $.fn.dataTable.ext.search.push(
        function (settings, data, dataIndex) {
            var min = $('#min').datepicker("getDate");
            var max = $('#max').datepicker("getDate");

            console.log("Минимальное значение "+min)

            var startDate = new Date(data[1]);
            var endDate = new Date(data[1]);

            if (min == null && max == null) { return true; }
            if (min == null && endDate <= max) { return true; }
            if (max == null && startDate >= min) { return true; }
            if (startDate >= min && endDate <= max) { return true; }
                return false;
            }
    );

    $("#min").datepicker($.datepicker.regional["ru"]);
    $("#min").datepicker({
        onSelect: function () {
            table.draw();
        },
        dateFormat: 'dd.mm.yy',
        changeMonth: true,
        changeYear: true,
        regional: 'ru',
        onClose: function (date, inst) {
            //set the other dateTo the min date
            var selectedDate = $("#min").datepicker("getDate");
            var followingDate = new Date(selectedDate.getTime() + 86400000);
            followingDate.toLocaleDateString();
            $("#max").datepicker("option", "minDate", followingDate);
        }
    });
    $("#max").datepicker($.datepicker.regional["ru"]);
    $("#max").datepicker({
        onSelect: function () {
            table.draw();
        },
        dateFormat: 'dd.mm.yy',
        changeMonth: true,
        changeYear: true,
        autoclose: true,
        clearBtn: true
    });
}

//Функция фильтрации базовая на основе таблицы.
function FilterBase(Table, arr_input, arr_select, arr_empty) {
    $(Table+' thead tr')
        .clone(true)
        .addClass('filters')
        .appendTo(Table+' thead');

    var table = $(Table).DataTable({
        dom: 't',
        ordering: false,
        paging: false,
        orderCellsTop: false,
        fixedHeader: true,
        initComplete: function () {
            var api = this.api();

            // Заполнение полей путыми значениями
            api.columns(arr_empty).eq(0).each(function (colIdx) {
                    // Set the header cell to contain the input element
                    var cell = $('.filters th').eq(
                        $(api.column(colIdx).header()).index()
                    );
                    var title = $(cell).text();
                    $(cell).html('<text></text>');
            });
            // Заполнение полей input
            api.columns(arr_input).eq(0).each(function (colIdx) {
                    // Set the header cell to contain the input element
                    var cell = $('.filters th').eq(
                        $(api.column(colIdx).header()).index()
                    );
                    var title = $(cell).text();
                    $(cell).html('<input type="text" class="form-control">');
                    // On every keypress in this input
                    $(
                        'input',
                        $('.filters th').eq($(api.column(colIdx).header()).index())
                    )
                        .off('keyup change')
                        .on('keyup change', function (e) {
                            e.stopPropagation();

                            // Get the search value
                            $(this).attr('title', $(this).val());
                            var regexr = '({search})'; //$(this).parents('th').find('select').val();

                            var cursorPosition = this.selectionStart;
                            // Search the column for that value
                            api
                                .column(colIdx)
                                .search(
                                    this.value != ''
                                        ? regexr.replace('{search}', '(((' + this.value + ')))')
                                        : '',
                                    this.value != '',
                                    this.value == ''
                                )
                                .draw();
                            $(this)
                                .focus()[0]
                                .setSelectionRange(cursorPosition, cursorPosition);
                        });
                });

            //Поля select
            api.columns(arr_select).every( function () {
                var column = this;
                var select = $('<select class="form-control"><option value=""></option></select>')
                    .appendTo( $(column.header()).empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option>'+d+'</option>' )
                } );
            } );
        },
    });
}

 //Сортировка таблиц
//document.addEventListener('DOMContentLoaded', () => {
//    const getSort = ({ target }) => {
//        const order = (target.dataset.order = -(target.dataset.order || -1));
//        const index = [...target.parentNode.cells].indexOf(target);
//        const collator = new Intl.Collator(['en', 'ru'], { numeric: true });
//        const comparator = (index, order) => (a, b) => order * collator.compare(
//            a.children[index].innerHTML,
//            b.children[index].innerHTML
//        );
//        for(const tBody of target.closest('table').tBodies)
//            tBody.append(...[...tBody.rows].sort(comparator(index, order)));
//
//        for(const cell of target.parentNode.cells)
//            cell.classList.toggle('sorted', cell === target);
//    };
//    document.querySelectorAll('.table_sort thead').forEach(tableTH => tableTH.addEventListener('click', () => getSort(event)));
//});

// Поиск по таблицам
function searchTable(idSearch, idTable, classField) {
    var input, filter, found, table, tr, td, i, j;
    input = document.getElementById(idSearch);
    filter = input.value.toUpperCase();
    table = document.getElementById(idTable);
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByClassName(classField);
        for (j = 0; j < td.length; j++) {
            if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
                found = true;
            }
        }
        if (found) {
            tr[i].style.display = "";
            found = false;
        } else {
            tr[i].style.display = "none";
        }
    }
}


// Добавление секций дома
$('#add_section').click(function() {
        var form_idx = $('#id_section-TOTAL_FORMS').val();
        $('#form_set_section').append($('#empty_form_section').html().replace(/prefix/g, form_idx));
        $('#id_section-TOTAL_FORMS').val(parseInt(form_idx) + 1);
        $('#form_set_section').find('#id_section-__'+parseInt(form_idx)+'__-name').attr('name', 'section-'+parseInt(form_idx)+'-name');
        $('#form_set_section').find('#id_section-__'+parseInt(form_idx)+'__-DELETE').attr('name', 'section-'+parseInt(form_idx)+'-DELETE');
        $('#form_set_section').find('div#id_form_section_').attr('id', 'id_form_section_'+ parseInt(form_idx));
    });

// Добавление этажей дома
$('#add_floor').click(function() {
        var form_idx = $('#id_floor-TOTAL_FORMS').val();
        $('#form_set_floor').append($('#empty_form_floor').html().replace(/prefix/g, form_idx));
        $('#id_floor-TOTAL_FORMS').val(parseInt(form_idx) + 1);
        $('#form_set_floor').find('#id_floor-__'+parseInt(form_idx)+'__-name').attr('name', 'floor-'+parseInt(form_idx)+'-name');
        $('#form_set_floor').find('#id_floor-__'+parseInt(form_idx)+'__-DELETE').attr('name', 'floor-'+parseInt(form_idx)+'-DELETE');
        $('#form_set_floor').find('div#id_form_floor_').attr('id', 'id_form_floor_'+ parseInt(form_idx));
    });

// Добавление новых документов
$('#add_document').click(function() {
        var form_idx = $('#id_document-TOTAL_FORMS').val();
        $('#form_set_document').append($('#empty_form_document').html().replace(/prefix/g, form_idx));
        $('#id_document-TOTAL_FORMS').val(parseInt(form_idx) + 1);
        $('#form_set_document').find('#id_document-__'+parseInt(form_idx)+'__-doc_name').attr('name', 'document-'+parseInt(form_idx)+'-doc_name');
        $('#form_set_document').find('#id_document-__'+parseInt(form_idx)+'__-DELETE').attr('name', 'document-'+parseInt(form_idx)+'-DELETE');
        $('#form_set_document').find('#id_document-__'+parseInt(form_idx)+'__-document').attr('name', 'document-'+parseInt(form_idx)+'-document');
        $('#form_set_document').find('div#id_form_document_').attr('id', 'id_form_document_'+ parseInt(form_idx));
    });

// Добавление новых услуг
$('#add_service').click(function() {
        var form_idx = $('#id_service-TOTAL_FORMS').val();
        $('#form_set_service').append($('#empty_form_service').html().replace(/prefix/g, form_idx));
        $('#id_service-TOTAL_FORMS').val(parseInt(form_idx) + 1);
        $('#form_set_service').find('#id_service-__'+parseInt(form_idx)+'__-name').attr('name', 'service-'+parseInt(form_idx)+'-name');
        $('#form_set_service').find('#id_service-__'+parseInt(form_idx)+'__-DELETE').attr('name', 'service-'+parseInt(form_idx)+'-DELETE');
        $('#form_set_service').find('#id_service-__'+parseInt(form_idx)+'__-description').attr('name', 'service-'+parseInt(form_idx)+'-description');
        $('#form_set_service').find('#id_service-__'+parseInt(form_idx)+'__-image').attr('name', 'service-'+parseInt(form_idx)+'-image');
        $('#form_set_service').find('div#id_form_service_').attr('id', 'id_form_service_'+ parseInt(form_idx));
    });

// Добавление новых изображений
$('#add_tariff').click(function() {
        var form_idx = $('#id_image-TOTAL_FORMS').val();
        $('#form_set_image').append($('#empty_form_image').html().replace(/prefix/g, form_idx));
        $('#id_image-TOTAL_FORMS').val(parseInt(form_idx) + 1);
        $('#form_set_image').find('#id_image-__'+parseInt(form_idx)+'__-file').attr('name', 'image-'+parseInt(form_idx)+'-file');
        $('#form_set_image').find('#id_image-__'+parseInt(form_idx)+'__-DELETE').attr('name', 'image-'+parseInt(form_idx)+'-DELETE');
        $('#form_set_image').find('#id_image-__'+parseInt(form_idx)+'__-signature').attr('name', 'image-'+parseInt(form_idx)+'-signature');
        $('#form_set_image').find('div#id_form_image_').attr('id', 'id_form_image_'+ parseInt(form_idx));
    });

// Добавление новых единиц измерения
$('#add_serviceunit').click(function() {
        var form_idx = $('#id_serviceunit-TOTAL_FORMS').val();
        $('#form_set_serviceunit').append($('#empty_form_serviceunit').html().replace(/prefix/g, form_idx));
        $('#id_serviceunit-TOTAL_FORMS').val(parseInt(form_idx) + 1);
        $('#form_set_serviceunit').find('#id_serviceunit-__'+parseInt(form_idx)+'__-unit').attr('name', 'serviceunit-'+parseInt(form_idx)+'-unit');
        $('#form_set_serviceunit').find('#id_serviceunit-__'+parseInt(form_idx)+'__-DELETE').attr('name', 'serviceunit-'+parseInt(form_idx)+'-DELETE');
        $('#form_set_serviceunit').find('div#id_form_serviceunit_').attr('id', 'id_form_serviceunit_'+ parseInt(form_idx));
    });

// Добавление новых услуг
$('#add_setting_service').click(function() {
        var form_idx = $('#id_setting_service-TOTAL_FORMS').val();
        $('#form_set_setting_service').append($('#empty_form_setting_service').html().replace(/prefix/g, form_idx));
        $('#id_setting_service-TOTAL_FORMS').val(parseInt(form_idx) + 1);
        $('#form_set_setting_service').find('#id_setting_service-__'+parseInt(form_idx)+'__-unit').attr('name', 'setting_service-'+parseInt(form_idx)+'-unit');
        $('#form_set_setting_service').find('#id_setting_service-__'+parseInt(form_idx)+'__-name').attr('name', 'setting_service-'+parseInt(form_idx)+'-name');
        $('#form_set_setting_service').find('#id_setting_service-__'+parseInt(form_idx)+'__-is_counter').attr('name', 'setting_service-'+parseInt(form_idx)+'-is_counter');
        $('#form_set_setting_service').find('#id_setting_service-__'+parseInt(form_idx)+'__-DELETE').attr('name', 'setting_service-'+parseInt(form_idx)+'-DELETE');
        $('#form_set_setting_service').find('div#id_form_setting_service_').attr('id', 'id_form_setting_service_'+ parseInt(form_idx));
    });

// Добавление услуг к тарифу
$('#add_service_to_tariff').click(function() {
        var form_idx = $('#id_setting_tariff_service-TOTAL_FORMS').val();
        $('#form_set_setting_tariff_service').append($('#empty_form_setting_tariff_service').html().replace(/prefix/g, form_idx));
        $('#id_setting_tariff_service-TOTAL_FORMS').val(parseInt(form_idx) + 1);
        $('#form_set_setting_tariff_service').find('#id_setting_tariff_service-__'+parseInt(form_idx)+'__-service').attr('name', 'setting_tariff_service-'+parseInt(form_idx)+'-service');
        $('#form_set_setting_tariff_service').find('#id_setting_tariff_service-__'+parseInt(form_idx)+'__-price').attr('name', 'setting_tariff_service-'+parseInt(form_idx)+'-price');
        $('#form_set_setting_tariff_service').find('#id_setting_tariff_service-__'+parseInt(form_idx)+'__-currency').attr('name', 'setting_tariff_service-'+parseInt(form_idx)+'-currency');
        $('#form_set_setting_tariff_service').find('#id_setting_tariff_service-__'+parseInt(form_idx)+'__-unit_service').attr('name', 'setting_tariff_service-'+parseInt(form_idx)+'-unit_service');
        $('#form_set_setting_tariff_service').find('#id_setting_tariff_service-__'+parseInt(form_idx)+'__-DELETE').attr('name', 'setting_tariff_service-'+parseInt(form_idx)+'-DELETE');
        $('#form_set_setting_tariff_service').find('div#id_form_setting_tariff_service_').attr('id', 'id_form_setting_tariff_service_'+ parseInt(form_idx));
    });

// Добавление услуг к квитанциям
$('#add_service_is_invoice').click(function() {
        var form_idx = $('#id_service_invoice-TOTAL_FORMS').val();
        $('#formset_service_invoice').append('<tr id="id_form_service_invoice_" class="form-service-invoice"></tr>')
        $('#id_form_service_invoice_').append($('#empty_form_service_invoice').html().replace(/prefix/g, form_idx));
        $('#id_service_invoice-TOTAL_FORMS').val(parseInt(form_idx) + 1);
        $('#formset_service_invoice').find('#id_service_invoice-__'+parseInt(form_idx)+'__-service').attr('name', 'service_invoice-'+parseInt(form_idx)+'-service');
        $('#formset_service_invoice').find('#id_service_invoice-__'+parseInt(form_idx)+'__-consumption').attr('name', 'service_invoice-'+parseInt(form_idx)+'-consumption');
        $('#formset_service_invoice').find('#id_service_invoice-__'+parseInt(form_idx)+'__-price').attr('name', 'service_invoice-'+parseInt(form_idx)+'-price');
        $('#formset_service_invoice').find('#id_service_invoice-__'+parseInt(form_idx)+'__-sum').attr('name', 'service_invoice-'+parseInt(form_idx)+'-sum');

        $('#formset_service_invoice').find('#id_service_invoice-__'+parseInt(form_idx)+'__-service').attr('id', 'id_service_invoice-'+parseInt(form_idx)+'-service');
        $('#formset_service_invoice').find('#id_service_invoice-__'+parseInt(form_idx)+'__-consumption').attr('id', 'id_service_invoice-'+parseInt(form_idx)+'-consumption');
        $('#formset_service_invoice').find('#id_service_invoice-__'+parseInt(form_idx)+'__-price').attr('id', 'id_service_invoice-'+parseInt(form_idx)+'-price');
        $('#formset_service_invoice').find('#id_service_invoice-__'+parseInt(form_idx)+'__-sum').attr('id', 'id_service_invoice-'+parseInt(form_idx)+'-sum');

        $('#formset_service_invoice').find('#id_service_invoice-__'+parseInt(form_idx)+'__-DELETE').attr('name', 'service_invoice-'+parseInt(form_idx)+'-DELETE');
        $('#id_form_service_invoice_').attr('id', 'id_form_service_invoice-'+ parseInt(form_idx));
    });

//Произведение показателей на стоимость
function MultiplicationInvoice(){
    var form_idx = $('#id_service_invoice-TOTAL_FORMS').val();
    var TotalSum = 0
    for (var i = 0; i < form_idx; i++){
        var result = $('#id_service_invoice-'+i+'-consumption').val() * $('#id_service_invoice-'+i+'-price').val();
        $('#id_service_invoice-'+i+'-sum').val(result);
        TotalSum = TotalSum + result;
    }
    $('#invoice-total-sum').html(TotalSum);
}

// Удаление блока
$(document).on('click', '.delete-form', function(e){
    if (confirm('Удалить?')) {
        e.preventDefault();
        $(this).parent().find('input[type=checkbox]').attr('checked','checked');
        $(this).parents('.form-section, .form-floor, .form-document, .form-service, .form-image, .form-serviceunit, .form-setting-service, .form-setting_tariff_service, .form-service-invoice').hide();
    }
});



function confirmDelete(){
    if(confirm("Вы уверены, что хотите удалить этот элемент?")){
        return true;
    } else {
        return false;
    }
}

//Генерация пароля
function gen_password(){
    var new_password = Math.random().toString(36).slice(3)
    var password = document.getElementById("password")
    var password2 = document.getElementById("password2")

    password.value = new_password
    password2.value = new_password
}

$('#showPass').click(function() {
    var password = document.getElementById("password")
    var password2 = document.getElementById("password2")

    if(password.type == "password"){
        password.type = "text"
        password2.type = "text"
    } else {
        password.type = "password"
        password2.type = "password"
    }
});

// Выбор и передача выбраного ЛС в поле внутри квартир
$("#id-select-account-flat").change(function () {
      var accountNumber = this.options[this.selectedIndex].text;
      var accountReturn = document.getElementById('id-personal-account-flat');
      accountReturn.value = accountNumber;
      $(this).val("");

    });

//// Фильтры для таблиц новые
$('.table-filters input').on('input', function () {
    filterTableInput($(this).parents('table'));
});



function filterTableInput($table) {
    var $filters = $table.find('.table-filters td');
    var $rows = $table.find('.table-data');
    $rows.each(function (rowIndex) {
        var valid = true;
        $(this).find('td').each(function (colIndex) {
            if ($filters.eq(colIndex).find('input').val()) {
                if ($(this).html().toLowerCase().indexOf(
                $filters.eq(colIndex).find('input').val().toLowerCase()) == -1) {
                    valid = valid && false;
                }
            }
        });
        if (valid === true) {
            $(this).css('display', '');
        } else {
            $(this).css('display', 'none');
        }
    });
}