var fs = require('fs')
var spawn = require("child_process").spawn;
let { PythonShell } = require('python-shell');

module.exports = {
  generateFortune : function (ipAddress){
      let runPy = new Promise(function(resolve, reject){
      console.log("utterances --js--- ", ipAddress);
      PythonShell.run("generators/markovify_sample.py", { pythonPath: '/usr/local/bin/python', args: [ipAddress]},  function (err, results) {
          if (err) reject(err);
          console.log('markovify_sample results: %j',results, results[results.length - 1]);
          resolve({message: results[results.length - 1]});
        });
      });
      return runPy;
  }
}
