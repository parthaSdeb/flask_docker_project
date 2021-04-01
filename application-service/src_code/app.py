from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
# import mysql.connector
import os


app = Flask(__name__)

# @app.route("/")
# def home():
#     return "hello flask project"

#configure db
app.config['MYSQL_HOST']=os.environ['MYSQL_HOST']
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DB']='test_db'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # fetch the form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        phone = userDetails['phone']

        cur = mysql.connection.cursor()
        cur.execute("insert into users(fullname, email, phone) values(%s,%s,%s)",(name, email, phone))
        mysql.connection.commit()
        cur.close()

        return redirect('/users')

    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("select * from users;")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)