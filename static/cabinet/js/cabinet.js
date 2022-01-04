$("document").ready(function() {

    // Расходы за предыдщий месяц
    var OldMonthCanvas = document.getElementById("ChartOldMonth");

    var OldMonthData = {
        labels: Object.keys(GetDataOldMonth()),
        datasets: [
            {
                data: Object.values(GetDataOldMonth()),
                backgroundColor: [
                    "#FF6384",
                    "#63AA84",
                    "#79FF40",
                    "#FFFF00",
                    "#000080",
                    "#FF0000",
                    "#008080",
                    "#C0C0C0",
                    "#FF00FF",
                ]
            }]
    };

    var doughnutChart = new Chart(OldMonthCanvas, {
      type: 'doughnut',
      data: OldMonthData
    });

    // Расходы за текущий год
    var ThisYearCanvas = document.getElementById("ChartThisYear");

    var ThisYearData = {
        labels: Object.keys(GetDataThisYear()),
        datasets: [
            {
                data: Object.values(GetDataThisYear()),
                backgroundColor: [
                    "#FF6384",
                    "#63AA84",
                    "#79FF40",
                    "#FFFF00",
                    "#000080",
                    "#FF0000",
                    "#008080",
                    "#C0C0C0",
                    "#FF00FF",
                ]
            }]
    };

    var doughnutChart = new Chart(ThisYearCanvas, {
      type: 'doughnut',
      data: ThisYearData
    });

    GetDataAllYear()
    // Расходы по месяцам за год
    var AllYearCanvas = document.getElementById("ChartAllYear");

    var AllYearData = {
        labels: ['Янв.', 'Февр.', 'Март', 'Апр.', 'Май', 'Июнь', 'Июль', 'Авг.', 'Сент.','Окт.','Нояб.','Дек'],
        datasets: [
            {
                data: GetDataAllYear(),
                backgroundColor: [
                    "#0000FF",
                ]
            }]
    };

    var barChart = new Chart(AllYearCanvas, {
      type: 'bar',
      data: AllYearData
    });

});

function GetDataOldMonth(){
    var url = $("#ChartOldMonth").attr("data-oldmonth-url");
    var flat = $("#FlatID").val()

    $.ajax({
        url: url,
        data: {'flat': flat},
        async: false,
        success: function (data) {
            json = data
        }
      });

    return json
}

function GetDataThisYear(){
    var url = $("#ChartThisYear").attr("data-thisyear-url");
    var flat = $("#FlatID").val()

    $.ajax({
        url: url,
        data: {'flat': flat},
        async: false,
        success: function (data) {
            json = data
        }
      });

    return json
}

function GetDataAllYear(){
    var url = $("#ChartAllYear").attr("data-allyear-url");
    var flat = $("#FlatID").val()
    var strRate = ''

    $.ajax({
        url: url,
        data: {'flat': flat},
        async: false,
        success: function (data) {
            strRate = data
        }
      });
    var Rate = strRate.split(',')
    return Rate
}