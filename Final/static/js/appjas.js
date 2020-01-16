function buildCharts(chartType) {
console.log('buildCharts');
  var url = '/lineChart/' + chartType;
  d3.request(url).get(function(error, data) {
  	console.log(data.response);
  	if (error) return console.warn(error);
  	var layout = {
      title: "Housing Trends in Long Beach",
      xaxis: {title: "Year: 2019"},
      width: 1200,
      height: 400,
	};
    Plotly.newPlot("line", JSON.parse(data.response), layout);
	});
}


