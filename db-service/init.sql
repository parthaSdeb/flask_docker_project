CREATE DATABASE IF NOT EXISTS test_db;

# create tables here
CREATE table users(id int Not Null AUTO_INCREMENT, fullname varchar(25), email varchar(40), phone varchar(11), PRIMARY KEY (id));


# add seed data inserts here