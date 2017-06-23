'use strict';

var express           = require('express');
var session           = require('express-session');
var cookieParser      = require('cookie-parser');
var bodyParser        = require('body-parser');
var path              = require('path');
var fs                = require('fs-extra');
var app               = express();
let PORT = 10925

String.prototype.escapeSpecialChars = function() {
    return this.replace(/\\n/g, "\\n")
                .replace(/\\'/g, "\\'")
                .replace(/\\"/g, '\\"')
                .replace(/\\&/g, "\\&")
                .replace(/\\r/g, "\\r")
                .replace(/\\t/g, "\\t")
                .replace(/\\b/g, "\\b")
                .replace(/\\f/g, "\\f");
};

const cookieKey='@ruby';
app.set('views',path.resolve(__dirname,'views'));
app.set('view engine','ejs');
app.use('/static',express.static('public'));
app.use(cookieParser());

app.engine('html',require('ejs').renderFile);

var router_main = require('./routes/main')(app);

app.listen(PORT, function() {
    console.log('Listening at port '+PORT)
});