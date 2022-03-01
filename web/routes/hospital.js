var alert = require('alert');
var moment = require('moment');
var express = require('express');
var router = express.Router();

/* GET testdb page. */
/*
router.get('/', function(req, res, next) {

    var db = req.con;
    var data = "";
    //res.send('respond with a test');

    db.query('SELECT * FROM user', function(err, rows) {
        if (err) {
	    console.log('this is test db error');
            console.log(err);
        }
        var data = rows;

        // use index.ejs
        res.render('testdb', { title: 'Test', data: data});
    });
   
});
*/
router.get('/login', function(req, res, next){
    res.render('hospital/h_login', {title: 'Add Test'});
});

router.get('/register', function(req, res, next){
    res.render('hospital/h_register', {title: 'Add Test'});
});


module.exports = router;
