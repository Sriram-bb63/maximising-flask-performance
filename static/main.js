window.onload = function () {

    var dps = []; // dataPoints
    var i1_dps = [];
    var i2_dps = [];
    var i3_dps = [];
    var i4_dps = [];
    var i5_dps = [];

    var req_per_sec_graph = new CanvasJS.Chart("req-per-sec", {
        // title: {
        //     text: "Number of requests per second"
        // },
        data: [{
            type: "line",
            dataPoints: dps
        }]
    });

    var i1_req_per_sec_graph = new CanvasJS.Chart("req-per-sec-i1", {
        // title: {
        //     text: "i1"
        // },
        data: [{
            type: "line",
            dataPoints: i1_dps
        }]
    });

    var i2_req_per_sec_graph = new CanvasJS.Chart("req-per-sec-i2", {
        // title: {
        //     text: "i2"
        // },
        data: [{
            type: "line",
            dataPoints: i2_dps
        }]
    });

    var i3_req_per_sec_graph = new CanvasJS.Chart("req-per-sec-i3", {
        // title: {
        //     text: "i3"
        // },
        data: [{
            type: "line",
            dataPoints: i3_dps
        }]
    });

    var i4_req_per_sec_graph = new CanvasJS.Chart("req-per-sec-i4", {
        // title: {
        //     text: "i4"
        // },
        data: [{
            type: "line",
            dataPoints: i4_dps
        }]
    });

    var i5_req_per_sec_graph = new CanvasJS.Chart("req-per-sec-i5", {
        // title: {
        //     text: "i5"
        // },
        data: [{
            type: "line",
            dataPoints: i5_dps
        }]
    });

    var xVal = 0;
    var updateInterval = 1000;
    var dataLength = 10; // number of dataPoints visible at any point

    var updateChart = function (count) {

        count = count || 1;

        for (var j = 0; j < count; j++) {
            fetch("http://127.0.0.1:5000/dashboard/req-per-sec")
                .then(res => res.json())
                .then(data => {
                    dps.push({
                        x: xVal,
                        y: data.total
                    });
                    i1_dps.push({
                        x: xVal,
                        y: data.i1
                    });
                    i2_dps.push({
                        x: xVal,
                        y: data.i2
                    });
                    i3_dps.push({
                        x: xVal,
                        y: data.i3
                    });
                    i4_dps.push({
                        x: xVal,
                        y: data.i4
                    });
                    i5_dps.push({
                        x: xVal,
                        y: data.i5
                    });
                })
            xVal++;
        }

        if (dps.length > dataLength) {
            dps.shift();
        }
        if (i1_dps.length > dataLength) {
            i1_dps.shift();
        }
        if (i2_dps.length > dataLength) {
            i2_dps.shift();
        }
        if (i3_dps.length > dataLength) {
            i3_dps.shift();
        }
        if (i4_dps.length > dataLength) {
            i4_dps.shift();
        }
        if (i5_dps.length > dataLength) {
            i5_dps.shift();
        }

        req_per_sec_graph.render();
        i1_req_per_sec_graph.render();
        i2_req_per_sec_graph.render();
        i3_req_per_sec_graph.render();
        i4_req_per_sec_graph.render();
        i5_req_per_sec_graph.render();

    };

    updateChart(dataLength);
    setInterval(function () { updateChart() }, updateInterval);

}