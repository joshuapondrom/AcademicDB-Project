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

@app.route('/stupersonalid')
def stupersonalid():
    return render_template('stupersonalid.html')

@app.route('/professor')
def professor():
    return render_template('professor.html')

@app.route('/profpersonalid')
def profpersonalid():
    return render_template('profpersonalid.html')

@app.route('/stupersonal', methods=['post'])
def stupersonal():
    db = sql.connect('data.db')
    db.row_factory = sql.Row

    given_id = request.form['given_id']
    curr = db.cursor()
    curr.execute('''
      SELECT *
      FROM Student S
      WHERE S.ID = %s
    ''' %(given_id))

    rows = curr.fetchall();
    return render_template("stupersonal.html", rows = rows)


@app.route('/profpersonal', methods=['post'])
def profpersonal():
    db = sql.connect('data.db')
    db.row_factory = sql.Row

    given_id = request.form['given_id']
    curr = db.cursor()
    curr.execute('''
      SELECT *
      FROM Instructor I
      WHERE I.ID = %s
    ''' %(given_id))

    rows = curr.fetchall();
    return render_template("profpersonal.html", rows = rows)

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

@app.route('/schedule', methods=['post'])
def schedule():
    db = sql.connect('data.db')
    db.row_factory = sql.Row

    given_id = request.form['given_id']
    curr = db.cursor()
    curr.execute('''
      SELECT T.Class_ID, T.Course_ID, C.DayCode, C.Time, R.Room_Number, R.Address
      FROM Takes T, ClassInRoom R, Class C
      WHERE T.ID = %s AND T.Class_ID = R.Class_ID AND T.Course_ID = R.Course_ID AND T.Class_ID = C.Class_ID AND T.Course_ID = C.Course_ID AND R.Class_ID = C.Class_ID AND R.Course_ID = C.Course_ID
    ''' %(given_id))

    rows = curr.fetchall();
    return render_template("schedule.html", rows = rows)

@app.route('/profschedule', methods=['post'])
def profschedule():
    db = sql.connect('data.db')
    db.row_factory = sql.Row

    given_id = request.form['given_id']
    curr = db.cursor()
    curr.execute('''
      SELECT T.Class_ID, T.Course_ID, C.DayCode, C.Time, R.Room_Number, R.Address
      FROM TaughtBy T, ClassInRoom R, Class C
      WHERE T.ID = %s AND T.Class_ID = R.Class_ID AND T.Course_ID = R.Course_ID AND T.Class_ID = C.Class_ID AND T.Course_ID = C.Course_ID AND R.Class_ID = C.Class_ID AND R.Course_ID = C.Course_ID
    ''' %(given_id))

    rows = curr.fetchall();
    return render_template("schedule.html", rows = rows)

@app.route('/prof_id')
def prof_id():
    return render_template("professorid.html")

@app.route('/student_id')
def student_id():
    return render_template("studentid.html")

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

@app.route('/delclass',methods = ['POST', 'GET'])
def delclass():
    if request.method == 'POST':
      try:
         Class_ID = request.form['Class_ID']

         with sql.connect("data.db") as db:
            curr = db.cursor()

            curr.execute("""DELETE FROM Class
                            WHERE Class.Class_ID = %s""" % (Class_ID))

            db.commit()
            msg = "Class deleted!"
      except:
         db.rollback()
         msg = "Error with class deletion, try again"

      finally:
         return render_template("result.html",msg = msg)

@app.route('/deleteclass')
def delc():
    return render_template('del.html')

@app.route('/delstudent',methods = ['POST', 'GET'])
def delstudent():
    if request.method == 'POST':
      try:
         ID = request.form['ID']

         with sql.connect("data.db") as db:
            curr = db.cursor()

            curr.execute("""DELETE FROM Student
                            WHERE Student.ID = %s""" % (ID))

            db.commit()
            msg = "Student deleted!"
      except:
         db.rollback()
         msg = "Error with student deletion, try again"

      finally:
         return render_template("result.html",msg = msg)

@app.route('/deletestudent')
def dels():
    return render_template('dels.html')

@app.route('/addstudent',methods = ['POST', 'GET'])
def addstudent():
   if request.method == 'POST':
      try:
         ID = request.form['ID']
         Address = request.form['Address']
         Name = request.form['Name']
         Year = request.form['Year']

         with sql.connect("data.db") as db:
            curr = db.cursor()

            curr.execute("""INSERT INTO Student(ID,Address,Name,Year)
               VALUES (?,?,?,?)""",(ID,Address,Name,Year) )

            db.commit()
            msg = "Student successfully added!"
      except:
         db.rollback()
         msg = "Error with student information, try again"

      finally:
         return render_template("result.html",msg = msg)
         db.close()

@app.route('/enterstudent')
def enterstudent():
    return render_template('addstudent.html')

@app.route('/enroll')
def enroll():
    return render_template('enroll.html')

@app.route('/enrollclass', methods = ['POST', 'GET'])
def enrollclass():
    if request.method == 'POST':
        try:
            ID = request.form['ID']
            Course_ID = request.form['Course_ID']

            with sql.connect("data.db") as db:
                curr = db.cursor()

                curr.execute(
                  '''
                  SELECT C.Class_ID
                  FROM Class C
                  WHERE C.Course_ID = Course_ID AND EXISTS ((SELECT K.Course_ID, K.Class_ID
                                                             FROM Class K)
                                                             MINUS
                                                            (SELECT T.Course_ID, T.Class_ID
                                                             FROM Takes T
                                                             WHERE T.ID = ID))
                  '''
                )
                Class_ID = curr.fetchone()
                db.commit()

                msg = "Enrolled successfully!"
        except:
            db.rollback()
            msg = "Error with entry, try again"

        finally:
            return render_template("result.html", msg = msg)
            db.close()

@app.route('/degree', methods=['post'])
def degree():
    db = sql.connect('data.db')
    db.row_factory = sql.Row

    ID = request.form['ID']
    curr = db.cursor()
    curr.execute('''
                 SELECT *
                 FROM Requires R
                 WHERE R.ID = %s AND NOT EXIST((SELECT Q.Course_ID
                                                FROM Requires Q
                                                WHERE Q.ID = %s)
                                                MINUS
                                               (SELECT Course_ID
                                                FROM Takes T
                                                WHERE T.ID = %s))
 
    ''' %(ID, ID, ID))

    rows = curr.fetchall();
    return render_template("degree.html", rows = rows)

@app.route('/degreeid')
def degreeid():
    return render_template('degreeid.html')
