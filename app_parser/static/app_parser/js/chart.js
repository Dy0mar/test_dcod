/**
 * Created by kurt on 22.06.17.
 */
function new_chart(name) {
    $.ajax({
        url: '/ajax/change_region/',
        data: {
            'name': name
        },
        dataType: 'json',
        success: function (dataProvider) {
            var chart = AmCharts.makeChart("chartdiv", {
                "type": "serial",
                "theme": "light",
                "dataProvider": dataProvider['lst'],
                "titles": [{
                    "text": dataProvider['title'],
                    "size": 15
                }],
                "valueAxes": [{
                    "gridColor": "#FFFFFF",
                    "gridAlpha": 0.2,
                    "dashLength": 0
                }],
                "gridAboveGraphs": true,
                "startDuration": 1,
                "graphs": [{
                    "balloonText": "[[category]]: <b>[[value]]</b>",
                    "fillAlphas": 0.8,
                    "lineAlpha": 0.2,
                    "type": "column",
                    "valueField": "value"
                }],
                "chartCursor": {
                    "categoryBalloonEnabled": false,
                    "cursorAlpha": 0,
                    "zoomable": false
                },
                "categoryField": "city",
                "categoryAxis": {
                    "labelRotation": 45,
                    "gridPosition": "start",
                    "gridAlpha": 0,
                    "tickPosition": "start",
                    "tickLength": 20
                },
                "autoResize": true,
                "export": {
                    "enabled": false
                }

            });
        }
    })
}