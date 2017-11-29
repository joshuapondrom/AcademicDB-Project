from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/professor')
def professor():
    return render_template('professor.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
