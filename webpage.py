from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import sqlite3 as sql
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/professor')
def professor():
    return render_template('professor.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/searchclass', methods=['POST'])
def searchclass():
    given_courseID = request.form['form-field']
    cursor = connection.cursor()
    cursor.execute(
        'SELECT *'
        'FROM Class C'
        'WHERE C.Course_ID = given_courseID'
    )
    rows = cursor.fetchall()
    return render_template(
        'list.html',
        rows = rows
    )

@app.route('/students')
def students():
    db = sql.connect('data.db')
    db.row_factory = sql.Row

    curr = db.cursor()
    curr.execute("Select * from Student")

    rows = curr.fetchall();
    return render_template("students.html", rows = rows)

@app.route('/schedule')
def schedule():
    db = sql.connect('data.db')
    db.row_factory = sql.Row

    given_id = 1
    curr = db.cursor()
    curr.execute('''
      SELECT T.Class_ID, T.Course_ID, C.DayCode, C.Time, R.Room_Number, R.Address
      FROM Takes T, ClassInRoom R, Class C
      WHERE T.ID = %d AND T.Class_ID = R.Class_ID AND T.Course_ID = R.Course_ID AND T.Class_ID = C.Class_ID AND T.Course_ID = C.Course_ID AND R.Class_ID = C.Class_ID AND R.Course_ID = C.Course_ID
    ''' %(given_id))

    rows = curr.fetchall();
    return render_template("schedule.html", rows = rows)

@app.route('/classes')
def classes():
    db = sql.connect('data.db')
    db.row_factory = sql.Row

    curr = db.cursor()
    curr.execute("Select * from Class")

    rows = curr.fetchall();
    return render_template("classes.html", rows = rows)

@app.route('/enterclass')
def enterclass():
    return render_template('addclass.html')

@app.route('/sql')
def sqlcom():
    return render_template('sql.html')

@app.route('/addclass',methods = ['POST', 'GET'])
def addclass():
   if request.method == 'POST':
      try:
         Class_ID = request.form['Class_ID']
         DayCode = request.form['DayCode']
         Time = request.form['Time']
         Course_ID = request.form['Course_ID']

         with sql.connect("data.db") as db:
            curr = db.cursor()

            curr.execute("""INSERT INTO Class(Class_ID,DayCode,Time,Course_ID)
               VALUES (?,?,?,?)""",(Class_ID,DayCode,Time,Course_ID) )

            db.commit()
            msg = "Class successfully added!"
      except:
         db.rollback()
         msg = "Error with class information, try again"

      finally:
         return render_template("result.html",msg = msg)
         db.close()

@app.route('/sendsql',methods = ['POST','GET'])
def sendsql():
   if request.method == 'POST':
      try:
         command = request.form['sqlcom']

         with sql.connect("data.db") as db:
            curr = db.cursor()

            curr.execute(command)

            db.commit()
            msg = "Command executed successfully!"
      except:
         db.rollback()
         msg = "Error with command, try again"
      finally:
         return render_template("result.html",msg = msg)
         db.close()
