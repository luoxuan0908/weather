function selectChart(type) {
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = ''; // 清空现有内容
    const myChart = echarts.init(mainContent);

    switch (type) {
        case 'bar':
            fetch('/api/bar-data') // 假设这是获取柱状图数据的后端API
                .then(response => response.json())
                .then(data => {
                    const option = {
                        xAxis: {
                            type: 'category',
                            data: data.categories
                        },
                        yAxis: {
                            type: 'value'
                        },
                        series: [{
                            data: data.values,
                            type: 'bar'
                        }]
                    };
                    myChart.setOption(option);
                });
            break;
        case 'pie':
            fetch('/api/pie-data') // 假设这是获取饼图数据的后端API
                .then(response => response.json())
                .then(data => {
                    const option = {
                        tooltip: {
                            trigger: 'item',
                            formatter: '{a} <br/>{b}: {c} ({d}%)'
                        },
                        series: [
                            {
                                name: 'Access Source',
                                type: 'pie',
                                radius: '55%',
                                data: data,
                                emphasis: {
                                    itemStyle: {
                                        shadowBlur: 10,
                                        shadowOffsetX: 0,
                                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                }
                            }
                        ]
                    };
                    myChart.setOption(option);
                });
            break;
        case 'wordCloud':
            fetch('/api/weather') // 使用实际的API来获取数据
                .then(response => response.json())
                .then(data => {
                    const formattedData = Object.keys(data).map(key => ({
                        name: key,
                        value: data[key]
                    }));
                    const option = {
                        tooltip: {
                            show: true
                        },
                        series: [{
                            type: 'wordCloud',
                            gridSize: 10,
                            sizeRange: [12, 50],
                            rotationRange: [-90, 90],
                            shape: 'pentagon',
                            drawOutOfBound: false,
                            textStyle: {
                                normal: {
                                    color: function () {
                                        return 'rgb(' + [
                                            Math.round(Math.random() * 160),
                                            Math.round(Math.random() * 160),
                                            Math.round(Math.random() * 160)
                                        ].join(',') + ')';
                                    }
                                },
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowColor: '#333'
                                }
                            },
                            data: formattedData
                        }]
                    };
                    myChart.setOption(option);
                });
            break;
    }
}

