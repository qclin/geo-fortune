var fs = require('fs')
var spawn = require("child_process").spawn;
let { PythonShell } = require('python-shell');

module.exports = {
  generateFortune : function (ipAddress){
      let runPy = new Promise(function(resolve, reject){
      console.log("utterances --js--- ", ipAddress);

      PythonShell.run("markovify_sample.py", { pythonPath: '/usr/bin/python', pythonOptions: ['-u'], scriptPath: 'generators/' args: [ipAddress]},  function (err, results) {
          if (err) console.log(err); // reject(err);
          console.log('markovify_sample results: %j',results);
          resolve({message: results[results.length - 1]});
        });
      });
      return runPy;
  }
}
