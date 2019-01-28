var express = require('express');
var fs = require('fs');
var cors = require('cors');
var bodyParser = require('body-parser');
var utterances = require('./utterance');

var app = express();
app.use(cors());
app.use(express.static('assets'));
app.use(bodyParser.json({extended: false}));

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});


app.get('/geo_fortune', function(req, res){
    // var ipAddress = req.headers['x-forwarded-for'] || req.connection.remoteAddress;

    var ipAddress = "95.90.239.37"
    var fortunePromise = utterances.generateFortune(ipAddress);
    fortunePromise.then(function(data){
      console.log("fortuen promised", data, typeof data);
      var predictedText = data.toString();
      res.json(predictedText);
    });
});


var listerner = app.listen(process.env.PORT || 8888, function() {
	console.log("Listening on port %d", listerner.address().port);
});
