var fs = require('fs-extra')

module.exports = {
    runList: function(callback) {
        var dir='./../compute/result/';
        var files = fs.readdirSync(dir)
              .map(function(v) { 
                  return { name:v,
                           time:fs.statSync(dir + v).mtime.getTime()
                         }; 
               })
               .sort(function(a, b) { return b.time-a.time; })
               .map(function(v) { return v.name; });
        callback(files)
    },
    runInfo: function(id, callback) {
        fs.readFile('./../compute/result/'+id+'/info.json', 'utf8', function (err, data) {
            if (err) throw err;
            info = JSON.parse(data);
            fs.readFile('./../compute/result/'+id+'/input.json', 'utf8', function (err, data2) {
                if (err) throw err;
                input = JSON.parse(data2);
                fs.readFile('./../compute/result/'+id+'/scores.json', 'utf8', function (err, data3) {
                    if (err) throw err;
                    scores = JSON.parse(data3);
                    callback(info,input,scores);
                });
            });
        });
    },
    genGene: function(id, gen, callback) {
        fs.readFile('./../compute/result/'+id+'/run_'+gen+'.json', 'utf8', function (err, data) {
            if (err) throw err;
            info = JSON.parse(data);
            callback(info);
        });
    }
};