var crypto = require('crypto');
var alert = require('alert');
var moment = require('moment');
var express = require('express');
var router = express.Router();


function hashsha256(input){
    var hash = crypto.createHash('sha256');
    return hash.update(input).digest('hex');
}

/* GET testdb page. */
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

router.get('/add', function(req, res, next){
    res.render('testAdd', {title: 'Add Test'});
});

router.get('/tdir', function(req, res, next){
    res.render('h/testdir', {title: 'Add Test'});
});


router.post('/add/UserAdd', function(req, res, next) {
    var db = req.con;	
    console.log(moment(new Date()).format('YYYY-MM-DD HH:mm:ss'));
    
    var workID = Number(escape(req.body.workID));
    var name = escape(req.body.name);
    var password = hashsha256(escape(req.body.password));
    var password2 = hashsha256(escape(req.body.password2));
    var phoneNum = escape(req.body.phoneNum);
    var email = escape(req.body.email);
    var title = escape(req.body.title);
    var gender = escape(req.body.gender);
    var years = Number(escape(req.body.years));
    var attr = escape(req.body.attr);
    var pubKey = escape(req.body.pubKey);
    var hashValue =  escape(req.body.hashValue);

    if (password != password2){
    	console.log('password is different');
	alert('password is different');
        res.redirect('back');
    }else{
        var sql = {
            workID: workID,
            name: name,
            password: password,
            phoneNum: phoneNum,
	    email: email,
            title: title,
            gender: gender,
            years: years,
            attr: attr,
            pubKey: pubKey,
            hashValue: hashValue,
            createTime: moment(new Date()).format('YYYY-MM-DD HH:mm:ss'),
            modifyTime: moment(new Date()).format('YYYY-MM-DD HH:mm:ss'),
        };
        console.log('sql:');
        console.log(sql);
    
        var qur = db.query('INSERT INTO user SET ?', sql, function(err, rows) {
            if (err){
	        console.log('sql error');
                console.log(err);
            }
	    console.log(qur);
            res.setHeader('Content-Type', 'application/json');
            res.redirect('/testdb');
        });
    }
});

module.exports = router;
