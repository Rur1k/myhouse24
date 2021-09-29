//Переключение вкладок
//function openContent(evt, TabInfo) {
//    // Declare all variables
//    var i, tab-panel, tablinks;
//
//    // Get all elements with class="tabcontent" and hide them
//    tabcontent = document.getElementsByClassName("tab-panel");
//    for (i = 0; i < tab-panel.length; i++) {
//        tab-panel[i].style.display = "none";
//    }
//
//    // Get all elements with class="tablinks" and remove the class "active"
//    tablinks = document.getElementsByClassName("tablinks");
//    for (i = 0; i < tablinks.length; i++) {
//        tablinks[i].className = tablinks[i].className.replace(" active", "");
//    }
//
//    // Show the current tab, and add an "active" class to the button that opened the tab
//    document.getElementById(cityName).style.display = "block";
//    evt.currentTarget.className += " active";
//}

// Сортировка таблиц
document.addEventListener('DOMContentLoaded', () => {
    const getSort = ({ target }) => {
        const order = (target.dataset.order = -(target.dataset.order || -1));
        const index = [...target.parentNode.cells].indexOf(target);
        const collator = new Intl.Collator(['en', 'ru'], { numeric: true });
        const comparator = (index, order) => (a, b) => order * collator.compare(
            a.children[index].innerHTML,
            b.children[index].innerHTML
        );
        for(const tBody of target.closest('table').tBodies)
            tBody.append(...[...tBody.rows].sort(comparator(index, order)));

        for(const cell of target.parentNode.cells)
            cell.classList.toggle('sorted', cell === target);
    };
    document.querySelectorAll('.table_sort thead').forEach(tableTH => tableTH.addEventListener('click', () => getSort(event)));
});

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


// Удаление блока
$(document).on('click', '.delete-form', function(e){
    if (confirm('Удалить?')) {
        e.preventDefault();
        $(this).parent().find('input[type=checkbox]').attr('checked','checked');
        $(this).parents('.form-section, .form-floor, .form-document, .form-service, .form-image').hide();
    }
});

function confirmDelete(){
    if(confirm("Вы уверены, что хотите удалить этот элемент?")){
        return true;
    } else {
        return false;
    }
}


