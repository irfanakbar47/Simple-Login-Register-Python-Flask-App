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
(1,‘name’,‘password’,‘email@email.com’);

