var fileman = require('./../fileman.js')

module.exports = function(app) {
  app.get('/',function(req,res) {
    fileman.runList( function(files) {
      res.render('index', {
        title: 'Hi',
        files: files
      });
    });
  });
  app.get('/run-detail/:id',function(req,res) {
    fileman.runInfo(req.params.id, function(info,input,scores) {
      res.render('run-detail', {
        title: 'Run detail: '+req.params.id,
        info: info,
        input: input,
        scores: scores
      });
    });
  });
}