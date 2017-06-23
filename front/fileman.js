var fs = require('fs-extra')

module.exports = {
    runList: function(callback) {
        fs.readdir('./../compute/result', function(err,files) {
            if(files==undefined) {
                callback([])
            }
            else callback(files)
        });
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
                    callback(info,input,scores)
                });
            });
        });
    }
};