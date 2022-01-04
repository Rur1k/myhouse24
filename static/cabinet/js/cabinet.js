$("document").ready(function() {

    var OldMonthJson = GetDataOldMonth();

    var jsonfile = {
        "jsonarray":[OldMonthJson]
    };

    console.log(jsonfile)
    
    // Расходы за предыдщий месяц
    var OldMonthCanvas = document.getElementById("ChartOldMonth");

    var OldMonthData = {
        labels: OldMonthJson[0],
        datasets: [
            {
                data: OldMonthJson[1],
                backgroundColor: [
                    "#FF6384",
                    "#63FF84",
                    "#84FF63",
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
        labels: [
            "Вода",
            "Електроенегрия",
            "Газ",
        ],
        datasets: [
            {
                data: [133.3, 86.2, 52.2],
                backgroundColor: [
                    "#FF6384",
                    "#63FF84",
                    "#84FF63"
                ]
            }]
    };

    var doughnutChart = new Chart(ThisYearCanvas, {
      type: 'doughnut',
      data: ThisYearData
    });

});

function GetDataOldMonth(){
    var url = $("#ChartOldMonth").attr("data-oldmonth-url");
    var flat = $("#FlatID").val()
    var json = {}

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