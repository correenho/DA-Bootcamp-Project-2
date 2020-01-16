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

	var data1 = [trace1, trace2];

	var layout1 = {
		showlegend: true,
		title: "Crime Cases in Long Beach, CA"
	}

	Plotly.newPlot('plot1', data1, layout1);

    var subcategory1 = [];
    var vcrime19=[];
    var vcrime18=[];

    for (i=4; i<8; i++) {
		subcategory1.push(c_data[i].Category);
		vcrime19.push(c_data[i]['2019']);
		vcrime18.push(c_data[i]['2018']);
	}	

	var trace3={
		values: vcrime19,
		labels: subcategory1,
		type: "pie"
	}

	var data2 = [trace3];

	var layout2 = {
		showlegend: true,
		title: "Violent Crimes in Long Beach, CA 2019"
	}

	Plotly.newPlot('plot2', data2, layout2);

	var trace4={
		values:vcrime18,
		labels: subcategory1,
		type: "pie"
	}

	var data3 = [trace4];

	var layout3 = {
		showlegend: true,
		title: "Violent Crimes in Long Beach, CA 2018"
	}

	Plotly.newPlot('plot3', data3, layout3);

})