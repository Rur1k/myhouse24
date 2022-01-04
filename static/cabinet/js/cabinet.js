$("document").ready(function() {
    // chart Диаграмма раходов для ЛК
    const ctx2 = document.getElementById('barChart2').getContext('2d');
    const myChart2 = new Chart(ctx2, {
        data: {
            labels: ['Янв.', 'Февр.', 'Март', 'Апр.', 'Май', 'Июнь', 'Июль', 'Авг.', 'Сент.','Окт.','Нояб.','Дек'],
            datasets: [
            {
                type: 'bar',
                label: 'Приход',
                data: getComing(),
                backgroundColor:  'rgba(0, 255, 0, 0.7)',
            },
            {
                type: 'bar',
                label: 'Расход',
                data: getExp(),
                backgroundColor:  'rgba(255, 99, 71, 1)',
            }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});