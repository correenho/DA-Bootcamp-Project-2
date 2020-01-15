

function makeGraphs(schoolSelect){

var s = schoolSelect;

	
d3.json('/project2/lbdemographics').then(function(demoData) {
	
	console.log(demoData[s]);

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    demoData.forEach(function(data) {
      data["Total"] = +data["Total"];
      data["African_American"] = +data["African_American"];
	  data["America_Indian_or_Alaska_Native"] = +data["America_Indian_or_Alaska_Native"];
	  data["Asian"] = +data["Asian"];
	  data["Filipino"] = +data["Filipino"];
	  data["Hispanic_or_Latino"] = +data["Hispanic_or_Latino"];
	  data["Pacific_Islander"] = +data["Pacific_Islander"];
	  data["White"] = +data["White"];
	  data["Two_or_More_Races"] = +data["Two_or_More_Races"];
	  data["Not_Reported"] = +data["Not_Reported"];
    });
	console.log(demoData);
	
		
	var data = [{
		values: [	demoData[s]["African_American"] ,
					demoData[s]["America_Indian_or_Alaska_Native"],
					demoData[s]["Asia"],
					demoData[s]["Filipino"],
					demoData[s]["Hispanic_or_Latino"],
					demoData[s]["Pacific_Islander"],
					demoData[s]["White"],
					demoData[s]["Two_or_More_Races"],
					demoData[s]["Not_Reported"]],
					
		labels: ['African American', 'American Indian or Alaska Native',
				 'Asia',
				 'Filipino',
				 'Hispanic or Latino',
				 'Pacific Islander',
				 'White',
				 'Two or More Races',
				 'Not Reported'],
		type: 'pie',
		title: {
				text: demoData[s]["Name"] +"<br> Student Demographics",
				font: {
				family: 'Courier New, monospace',
				size: 24
		}},
	}];
		var layout = {
			  autosize: false,
			  width: 500,
			  height: 500,
			  margin: {
				l: 50,
				r: 50,
				b: 100,
				t: 100,
				pad: 100,
			 showlegend: false
	}};
	
	


	Plotly.newPlot('student', data, layout);
	
	});
	
	d3.json('/project2/absent').then(function(absentData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    absentData.forEach(function(data) {
      data["Eligible_Enrollment"] = +data["Eligible_Enrollment"];
      data["Chronic_Absenteeism_Count"]= +data["Chronic_Absenteeism_Count"];
    });
	
	console.log(absentData)
	
	var trace1 = {
		  x: ['Absenteeism Count'],
		  y: [absentData[s]["Eligible_Enrollment"]],
		  name: 'Chronic Absenteeism Eligible',
		  type: 'bar'
	};

	var trace2 = {
	  x: ['Absenteeism Count'],
	  y: [absentData[s]["Chronic_Absenteeism_Count"]],
	  name: 'Chronically Absent',
	  type: 'bar'
	};
	
	var data = [trace2, trace1];
	
	var layout = {
				autosize: false,
				width: 500,
				height: 500,
				title: absentData[s]["Name"] +'<br> Chronic Absenteeism' ,
				barmode: 'stack'
				
			  };
	
	


	Plotly.newPlot('absent', data, layout);
	
	});
	
d3.json('project2/english').then(function(englishData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    englishData.forEach(function(data) {
      data["English_Only"] = +data["English_Only"];
      data["Initial_Fluent_English_Proficient"]= +data["Initial_Fluent_English_Proficient"];
	  data["English_Learner"] = +data["English_Learner"];
	  data["Reclassified_Fluent_English_Proficient"] = +data["Reclassified_Fluent_English_Proficient"];
	  data["To_Be_Determined"] = +data["To_Be_Determined"];
	  data["Total"] = +data["Total"];
	  
    });
	
	console.log(englishData)
	
	var data = [{
		values: [	englishData[s]["English_Only"], 
					englishData[s]["Initial_Fluent_English_Proficient"],
					englishData[s]["English_Learner'"],
					englishData[s]["Reclassified_Fluent_English_Proficient"],
					englishData[s]["To_Be_Determined"]
					],
					
		labels: ['English Only', 'Initial Fluent English Proficient',
				 'English Learner',
				 'Reclassified English Fluent',
				 'To be Determined'
				],
		type: 'pie',
		title:  englishData[s]["Name"] + "<br>English Data ",
	}];
	
	var layout = {
			  autosize: true,
			  width: 500,
			  height: 500,
			  margin: {
				l: 50,
				r: 50,
				b: 100,
				t: 100,
				pad: 100,
			 showlegend: false
	}};
	
	


	Plotly.newPlot('english', data, layout);
	
	});
	
d3.json('project2/staff').then(function(staffData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    staffData.forEach(function(data) {
      data["Doctorate"] = +data["Doctorate"];
      data["Juris_Doctor"]= +data["Juris_Doctor"];
	  data["Masters_Degree_3s"] = +data["Masters_Degree_3s"];
	  data["Masters_Degree"] = +data["Masters_Degree"];
	  data["Baccalaureate_Degree_3s"] = +data["Baccalaureate_Degree_3s"];
	  data["Baccalaureate_Degree"] = +data["Baccalaureate_Degree"];
	  data["None_Reported"] = +data["None_Reported"];
	  data["Total"] = +data["Total"];
    });
	
	console.log(staffData[s])
	
	var data = [{
							
		x: ['Doctorate', 'Juris Doctor',
				 'Master\'s +3s',
				 'Master\'s',
				 'Baccalaureate +3s',
				 'Baccalaureate',
				 'Not Reported'
				 ],
		y: [	staffData[s]["Doctorate"], 
					staffData[s]["Juris_Doctor"],
					staffData[s]["Masters_Degree_3s"],
					staffData[s]["Masters_Degree"],
					staffData[s]["Baccalaureate_Degree_3s"],
					staffData[s]["Baccalaureate_Degree"],
					staffData[s]["None_Reported"]
				],
		type: 'bar',

	}];
	
	var layout = {
				autosize: true,
				title: staffData[s]["Name"] +'<br> Teacher Education Level' ,
				
			  };
	
	


	Plotly.newPlot('staff', data, layout);
	
	});

d3.json('project2/suspension').then(function(suspensionData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    suspensionData.forEach(function(data) {
      data["Cumulative_Enrollment"] = +data["Cumulative_Enrollment"];
      data["Total_Suspensions"] = +data["Total_Suspensions"];
	  data["Unduplicated_Suspensions"] = +data["Unduplicated_Suspensions"];
    });
	
	console.log(suspensionData)
	
	var trace1 = {
		  x: ['Suspensions'],
		  y: [suspensionData[s]["Cumulative_Enrollment"]],
		  name: 'Total Enrollment',
		  type: 'bar'
	};

	var trace2 = {
	  x: ['Suspensions'],
	  y: [suspensionData[s]["Total_Suspensions"]],
	  name: 'Total Suspensions',
	  type: 'bar'
	};
	
	var trace3 = {
	  x: ['Suspensions'],
	  y: [suspensionData[s]["Unduplicated_Suspensions"]],
	  name: 'Students with one suspension',
	  type: 'bar'
	};
	
	
	var data = [trace1, trace2, trace3];
	
	var layout = {
				autosize: false,
				width: 500,
				height: 500,
				title: suspensionData[s].Name +'<br> Suspensions' ,
				barmode: 'group'
				
			  };
	
	


	Plotly.newPlot('suspension', data, layout);
	
	});
};


makeGraphs();
