var fileman = require('./../fileman.js')

module.exports = function(app) {
  app.get('/',function(req,res) {
    res.render('index', {
      title: 'Hi'
    });
  });
  app.get('/run-list',function(req,res) {
    fileman.runList( function(files) {
      res.render('run-list', {
        title: '저장된 결과',
        files: files
      });
    });
  });
  app.get('/run-detail/:id',function(req,res) {
    fileman.runInfo(req.params.id, function(info,input,scores) {
      res.render('run-detail', {
        title: '상세 정보: '+req.params.id,
        id: req.params.id,
        info: info,
        input: input,
        scores: scores
      });
    });
  });
  app.get('/run-input/:id',function(req,res) {
    fileman.runInfo(req.params.id, function(info,input,scores) {
      res.render('run-input', {
        title: '입력 데이터: '+req.params.id,
        id: req.params.id,
        info: info,
        input: input,
        scores: scores
      });
    });
  });
  app.get('/run-gene/:id/:gen',function(req,res) {
    if(req.params.gen==='select') {
      fileman.runInfo(req.params.id, function(info,input,scores) {
        res.render('run-gene-select', {
          title: '세대 선택: '+req.params.id,
          id: req.params.id,
          info: info,
          input: input,
          scores: scores
        });
      });
    } else {
      fileman.genGene(req.params.id, req.params.gen, function(info) {
        fileman.runInfo(req.params.id, function(k,meta,scores) {
          res.render('run-gene', {
            title: req.params.id+'-'+req.params.gen+'세대',
            id: req.params.id,
            gen: req.params.gen,
            info: info,
            meta: meta
          });
        });
      });
    }
  }),
  app.get('/api/gene/:id/:gen',function(req,res) {
    fileman.genGene(req.params.id, req.params.gen, function(info) {
      res.json(info);
    });
  }),
  app.get('/api/input/:id',function(req,res) {
    fileman.runInfo(req.params.id, function(info,input) {
      res.json(input);
    });
  });
}