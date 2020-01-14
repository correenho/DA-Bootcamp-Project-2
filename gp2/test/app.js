d3.csv('LBDemographics.csv').then(function(demoData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    demoData.forEach(function(data) {
      data.Total = +data.Total;
      data.African_American = +data.African_American;
	  data.America_Indian_or_Alaska_Native = +data.America_Indian_or_Alaska_Native;
	  data.Asian = +data.Asian;
	  data.Filipino = +data.Filipino;
	  data.Hispanic_or_Latino = +data.Hispanic_or_Latino;
	  data.Pacific_Islander = +data.Pacific_Islander;
	  data.White = +data.White;
	  data.Two_or_More_Races = +data.Two_or_More_Races;
	  data.Not_Reported = +data.Not_Reported;
    });
	console.log(demoData);
	
	test = demoData[0];
	console.log(test);
	console.log(demoData[0].Total);
	
	
	var data = [{
		values: [	demoData[0].African_American, 
					demoData[0].America_Indian_or_Alaska_Native,
					demoData[0].Asia,
					demoData[0].Filipino,
					demoData[0].Hispanic_or_Latino,
					demoData[0].Pacific_Islander,
					demoData[0].White,
					demoData[0].Two_or_More_Races,
					demoData[0].Not_Reported],
					
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
				text: demoData[0].Name + "<br> student total: " + demoData[0].Total,
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
				pad: 10,
			 showlegend: false
	}};
	
	


	Plotly.newPlot('student', data, layout);
	
	});
	
d3.csv('staffEdLevel.csv').then(function(staffData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    staffData.forEach(function(data) {
      data.Doctorate = +data.Doctorate;
      data.Juris_Doctor= +data.Juris_Doctor;
	  data.Masters_Degree_30 = +data.Masters_Degree_30;
	  data.Masters_Degree = +data.Masters_Degree;
	  data.Baccalaureate_Degree_30 = +data.Baccalaureate_Degree_30;
	  data.Baccalaureate_Degree = +data.Baccalaureate_Degree;
	  data.None_Reported = +data.None_Reported;
	  data.Total = +data.Total;
    });
	
	console.log(staffData[0])
	
	var data = [{
							
		x: ['Doctorate', 'Juris Doctor',
				 'Master\'s +30',
				 'Master\'s',
				 'Baccalaureate +30',
				 'Baccalaureate',
				 'Not Reported'
				 ],
		y: [	staffData[0].Doctorate, 
					staffData[0].Juris_Doctor,
					staffData[0].Masters_Degree_30,
					staffData[0].Masters_Degree,
					staffData[0].Baccalaureate_Degree_30,
					staffData[0].Baccalaureate_Degree,
					staffData[0].None_Reported
				],
		type: 'bar',

	}];
	
	var layout = {
				autosize: true,
				title: staffData[0].Name +'<br> Teacher Education Level' ,
				
			  };
	
	


	Plotly.newPlot('staff', data, layout);
	
	});

d3.csv('absentData.csv').then(function(absentData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    absentData.forEach(function(data) {
      data.Eligible_Enrollment = +data.Eligible_Enrollment;
      data.Chronic_Absenteeism_Count= +data.Chronic_Absenteeism_Count;
    });
	
	console.log(absentData[0])
	
	var trace1 = {
		  x: ['Absenteeism Count'],
		  y: [absentData[0].Eligible_Enrollment],
		  name: 'Chronic Absenteeism Eligible',
		  type: 'bar'
	};

	var trace2 = {
	  x: ['Absenteeism Count'],
	  y: [absentData[0].Chronic_Absenteeism_Count],
	  name: 'Chronically Absent',
	  type: 'bar'
	};
	
	var data = [trace2, trace1];
	
	var layout = {
				autosize: false,
				width: 500,
				height: 500,
				title: absentData[0].Name +'<br> Chronic Absenteeism' ,
				barmode: 'stack'
				
			  };
	
	


	Plotly.newPlot('absent', data, layout);
	
	});
	
d3.csv('englishData.csv').then(function(englishData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    englishData.forEach(function(data) {
      data.English_Only = +data.English_Only;
      data.Initial_Fluent_English_Proficient= +data.Initial_Fluent_English_Proficient;
	  data.English_Learner = +data.English_Learner;
	  data.Reclassified_Fluent_English_Proficient = +data.Reclassified_Fluent_English_Proficient;
	  data.To_Be_Determined = +data.To_Be_Determined;
	  data.Total = +data.Total;
	  
    });
	
	console.log(englishData[0])
	
	var data = [{
		values: [	englishData[0].English_Only, 
					englishData[0].Initial_Fluent_English_Proficient,
					englishData[0].English_Learner,
					englishData[0].Reclassified_Fluent_English_Proficient,
					englishData[0].To_Be_Determined
					],
					
		labels: ['English Only', 'Initial Fluent English Proficient',
				 'English Learner',
				 'Reclassified English Fluent',
				 'To be Determined'
				],
		type: 'pie',
		title: {
				text: englishData[0].Name + "<br> student total: " + englishData[0].Total,
				font: {
				family: 'Courier New, monospace',
				size: 24
		}},
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
				pad: 10,
			 showlegend: false
	}};
	
	


	Plotly.newPlot('english', data, layout);
	
	});
	
d3.csv('suspensionData.csv').then(function(suspensionData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    suspensionData.forEach(function(data) {
      data.Cumulative_Enrollment = +data.Cumulative_Enrollment;
      data.Total_Suspensions= +data.Total_Suspensions;
	  data.Unduplicated_Suspensions = +data.Unduplicated_Suspensions;
    });
	
	console.log(suspensionData[0])
	
	var trace1 = {
		  x: ['Suspensions'],
		  y: [suspensionData[0].Cumulative_Enrollment],
		  name: 'Total Enrollment',
		  type: 'bar'
	};

	var trace2 = {
	  x: ['Suspensions'],
	  y: [suspensionData[0].Total_Suspensions],
	  name: 'Total Suspensions',
	  type: 'bar'
	};
	
	var trace3 = {
	  x: ['Suspensions'],
	  y: [suspensionData[0].Unduplicated_Suspensions],
	  name: 'Students with one suspension',
	  type: 'bar'
	};
	
	
	var data = [trace1, trace2, trace3];
	
	var layout = {
				autosize: false,
				width: 500,
				height: 500,
				title: suspensionData[0].Name +'<br> Suspensions' ,
				barmode: 'group'
				
			  };
	
	


	Plotly.newPlot('suspension', data, layout);
	
	});