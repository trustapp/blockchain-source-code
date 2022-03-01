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
/*router.get('/', function(req, res, next) {

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
router.get('/medcase', function(req, res, next){
    res.render('care/medcase', {title: 'Add Test'});
});


router.get('/login', function(req, res, next){
    res.render('care/c_login', {title: 'Add Test'});
});

router.post('/logining',function(req, res, next){
    var db = req.con;
    var workID = Number(escape(req.body.workID));
    var pw = hashsha256(escape(req.body.password1));
    
    var qur = db.query('Select workID, password, name from user where workID = ?', workID, function(err, rows) {
        if (err){
	    console.log('sql error');
            console.log(err);
	    res.redirect('back');
        }else{
	    if(rows == false){
	       console.log('account error');
	       alert('account error');
	       res.redirect('back');
	    }else{
	        dbpw = rows[0].password;
		if(dbpw == pw){
	            res.setHeader('Content-Type', 'application/json');
        	    res.redirect('medcase');
		}else{
		    console.log('wrong password');
		    alert('wrong password');
		    res.redirect('back');
		}
	    }
	}

    });
});


router.get('/register', function(req, res, next){
    res.render('care/c_register', {title: 'Add Test'});
});


router.post('/addUser', function(req, res, next) {
    var db = req.con;	
    console.log(moment(new Date()).format('YYYY-MM-DD HH:mm:ss'));
    
    var workID = Number(escape(req.body.workID));
    var resname = escape(req.body.name);
    var name = resname.replace('%20',' ');
    var password = hashsha256(escape(req.body.password1));
    var password2 = hashsha256(escape(req.body.password2));
    var phoneNum = escape(req.body.phoneNum);
    var email = escape(req.body.email);
    var restitle = escape(req.body.title);
    console.log(restitle);
    var title = restitle.replace('%2C',',');
    var gender = escape(req.body.gender);
    var years = Number(escape(req.body.years));
    var attr = gender + ',' + years + ',' + title;
    var pubKey = '';
    var hashValue =  '';
    
    if (password != password2){
    	console.log('password is different');
	alert('password is different');
        res.redirect('back');
    }else{
	console.log('password correct');
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
            res.redirect('/login');
        });
    }
});

module.exports = router;
