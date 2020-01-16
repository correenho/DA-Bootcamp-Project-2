Plotly.d3.csv("static/Data/buy_full_list.csv", function(b_data){
    var b_lat = [];
    var b_lng = [];
    var b_price =[];
    var b_details = [];

    for (var i=0; i<b_data.length; i++) {
        b_lat.push(b_data[i].latitude);
        b_lng.push(b_data[i].longitude);
        b_price.push(b_data[i].price);
        b_details.push([b_data[i].details, b_data[i].address, b_data[i].link]);
        }

    Plotly.d3.csv("static/Data/rent_full_list.csv", function(r_data){
            var r_lat = [];
            var r_lng = [];
            var r_price = [];
            var r_details = [];
            
            for (var j=0; j<r_data.length; j++) {
                r_lat.push(r_data[j].lat);
                r_lng.push(r_data[j].lng);
                r_price.push(r_data[j].price);
                r_details.push([r_data[j].details,r_data[j].address, r_data[j].link])
        }
        
 
    var trace1 = {
        type: "scattermapbox", 
        opacity: 0.7,
        lon: b_lng, 
        lat: b_lat, 
        text: b_price,
        customdata: b_details,
        name:"Buy", 
        hovertemplate: "<b>%{text}</b><br>" + "%{customdata[0]}<br>" + "%{customdata[1]}<br>" + "<a href=>%{customdata[2]}</a>" + "<extra></extra>"
    };
    
    var trace2 = {
        type: "scattermapbox", 
        opacity: 0.6,
        lon: r_lng, 
        lat: r_lat, 
        text: r_price,
        customdata: r_details,
        name: "Rent", 
        hovertemplate: "<b>%{text}</b><br>" + "%{customdata[0]}<br>" + "%{customdata[1]}<br>" + "<a href=>%{customdata[2]}</a>" + "<extra></extra>"
    };
  
    var data = [trace1, trace2];

     
  var layout = {
      dragmode: "zoom",
      mapbox: { style: "dark", zoom: 11.5, center: { lon: -118.136500, lat: 33.809060 } },
      margin: { t: 0, b: 0 },
      hovermode: "closest",
      hoverlabel: { bgcolor: "#FFF" },
      showlegend:true,
      legend: {
        x: -0.01,
        xanchor: 'right',
        y: 1
    }
  };

  var config = {
    mapboxAccessToken: accessMapboxToken,
    responsive: true
  };

    Plotly.newPlot('map', data, layout, config);
        
  })
})