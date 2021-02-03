# onebyteproject
Python Web App Login Registration
First of all requirements

install python 3.x
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update

installing pip3 for application package manager
$ sudo apt-get -y install python3-pip

install mysql 5.7
$ wget http://repo.mysql.com/mysql-apt-config_0.8.9-1_all.deb
$ sudo dpkg -i mysql-apt-config_0.8.9-1_all.deb

MySQL
Creating database
CREATE DATABASE pythonlogin;
use pythonlogin;

Creating table
CREATE TABLE accounts (
id int NOT NULL AUTO_INCREMENT,
username varchar(50) NOT NULL,
password varchar(255) NOT NULL,
email varchar(100) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
Inserting Values
insert into user(id,username,password,email) values
(1,‘haan’,‘haan’,‘haan@email.com’);

app.py
Contains all the modules like login, register and logout.

code login: Main page is Login module will ask user login if existing or you can click to register and the login. login if exist in database if id doesn’t exist it will show error,

    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))

    account = cursor.fetchone()
    if account:

        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']
        msg = 'Logged in successfully !'

        return render_template('index.html', msg = msg)
    else:
        msg = 'Incorrect username / password !'
return render_template('login.html', msg = msg)
logged-out code: redirecting to login page after logged out

session.pop('loggedin', None)
session.pop('id', None)
session.pop('username', None)
return redirect(url_for('login'))
Registration Form User will request username, password and email address. After registration data is saved in database and after that user can login. it also check if user already exist, email validation, username must only contain alphabets or numbers and if anything is missing in form it will ask to fill the form.

    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
    account = cursor.fetchone()

    if account:
        msg = 'Account already exists !'
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        msg = 'Invalid email address !'
    elif not re.match(r'[A-Za-z0-9]+', username):
        msg = 'Username must contain only characters and numbers !'
    elif not username or not password or not email:
        msg = 'Please fill out the form !'

    else:
        cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
        mysql.connection.commit()
        msg = 'You have successfully registered !'
elif request.method == 'POST':
    msg = 'Please fill out the form !'
return render_template('register.html', msg = msg)
testlogin.py
For Testing using unittesting library. Here testing only content type and response from the server is 200.

class FlaskTest(unittest.TestCase):
 def test_index1(self):
            tester1 = app.test_client(self)
            response = tester1.get('/login', content_type='html/text')
            self.assertEqual(response.status_code, 200)
Dockerfile First installing python3-dev and pip3 in docker image with pip update. copying app folder in docker image. Running pip3 to install requirements for application. Exposing port 5000. with also running the application python3 app.py

	FROM python:3.8.5-alpine
	RUN apk add --no-cache python3-dev
	RUN apk add py3-pip \
	&& pip3 install --upgrade pip


	WORKDIR /app
	COPY . /app

	RUN pip3 --no-cache-dir install -r requirements.txt

	EXPOSE 5000

	ENTRYPOINT ["python3"]
	CMD ["app.py"]
#####

Diagram

connects with Database
WebApi Login, Lgout, Registeration
DB
Browser
