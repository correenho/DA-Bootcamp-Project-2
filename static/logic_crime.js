Plotly.d3.csv("static/Data/lbcrimedata.csv", function(c_data){
	console.log(c_data);
	var category = [];
	var crime19 = [];
	var crime18 = [];

	for (i=0; i<2; i++) {
		category.push(c_data[i].Category);
		crime19.push(c_data[i]['2019']);
		crime18.push(c_data[i]['2018']);
	}	

	console.log(category, crime18, crime19);

	var trace1 = {
		x: category,
		y: crime18,
		type: "bar",
		name: "2018"
	}

	var trace2 = {
		x: category,
		y: crime19,
		type: "bar",
		name: "2019"
	}

	var data = [trace1, trace2];

	var layout = {
		showlegend: true,
		title: "Crime Cases in Long Beach, CA"
	}

	Plotly.newPlot('plot', data, layout);
})