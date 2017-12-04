import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE Student('
               '    ID INTEGER PRIMARY KEY,'
               '    Address VARCHAR(100),'
               '    Name VARCHAR(30),'
               '    Year INTEGER'
               ')')
connection.commit()
cursor.execute('CREATE TABLE Building('
               '    Address VARCHAR(30) PRIMARY KEY,'
               '    Name VARCHAR(30),'
               '    Abbr VARCHAR(5)'
               ')')
cursor.execute('CREATE TABLE Instructor('
               '    ID INTEGER PRIMARY KEY,'
               '    Address VARCHAR(100),'
               '    Name VARCHAR(30),'
               '    Dept VARCHAR(30),'
               '    FOREIGN KEY(Dept) REFERENCES Department(Program)'
               ')')
connection.commit()
cursor.execute('CREATE TABLE Located('
               '    Program VARCHAR(30),'
               '    Address VARCHAR(100),'
               '    PRIMARY KEY(Program,Address),'
               '    FOREIGN KEY(Program) REFERENCES Department(Program),'
               '    FOREIGN KEY(Address) REFERENCES Building(address)'
               ')')
connection.commit()
cursor.execute('CREATE TABLE Room('
               '    Type VARCHAR (20),'
               '    Room_Number INTEGER,'
               '    Address VARCHAR(100),'
               '    PRIMARY KEY(Room_Number, Address),'
               '    FOREIGN KEY(Address) REFERENCES Building(address)'
               ')')
connection.commit()
cursor.execute('CREATE TABLE Class('
               '    Class_ID CHAR(5),'
               '    DayCode CHAR(5),'
               '    Time INTEGER,'
               '    Course_ID VARCHAR(15),'
               '    PRIMARY KEY(Course_ID, Class_ID),'
               '    FOREIGN KEY(Course_ID) REFERENCES Course(Course_ID)'
               ')')
connection.commit()
cursor.execute('CREATE TABLE Course('
               '    Course_ID VARCHAR(15) PRIMARY KEY,'
               '    Major VARCHAR(30),'
               '    Credit_Hourse INTEGER'
               ')')
connection.commit()
cursor.execute('CREATE TABLE Takes('
               '    ID INTEGER,'
               '    Class_ID CHAR(5),'
               '    Course_ID VARCHAR(15),'
               '    Grade FLOAT,'
               '    PRIMARY KEY(ID, Class_ID, Course_ID),'
               '    FOREIGN KEY(ID) REFERENCES Student(ID),'
               '    FOREIGN KEY(Class_ID) REFERENCES Class(Class_ID),'
               '    FOREIGN KEY(Course_ID) REFERENCES Course(Course_ID)'
               ')')
connection.commit()
cursor.execute('CREATE TABLE ClassInRoom('
               '    Course_ID VARCHAR(15),'
               '    Class_ID CHAR(5),'
               '    Room_Number INTEGER,'
               '    Address VARCHAR(100),'
               '    PRIMARY KEY(Course_ID, Class_ID, Room_Number, Address),'
               '    FOREIGN KEY(Course_ID) REFERENCES Course(Course_ID),'
               '    FOREIGN KEY(Class_ID) REFERENCES Class(Class_ID),'
               '    FOREIGN KEY(Room_Number) REFERENCES Room(Room_Number),'
               '    FOREIGN KEY(Address) REFERENCES Building(address)'
               ')')
connection.commit()
cursor.execute('CREATE TABLE TaughtBy('
               '    ID INTEGER,'
               '    Class_ID CHAR(5),'
               '    Course_ID VARCHAR(15),'
               '    PRIMARY KEY(ID, Class_ID, Course_ID),'
               '    FOREIGN KEY(ID) REFERENCES Instructor(ID),'
               '    FOREIGN KEY(Class_ID) REFERENCES Class(Class_ID),'
               '    FOREIGN KEY(Course_ID) REFERENCES Course(Course_ID)'
               ')')
connection.commit()
cursor.execute('CREATE TABLE Requires('
               '    ID INTEGER,'
               '    Course_ID VARCHAR(15),'
               '    PRIMARY KEY(ID, Course_ID),'
               '    FOREIGN KEY(ID) REFERENCES Student(ID),'
               '    FOREIGN KEY(Course_ID) REFERENCES Course(Course_ID)'
               ')')
connection.commit()
cursor.execute('CREATE TABLE EmergencyContact('
               '    Phone_Number CHAR(10),'
               '    Address VARCHAR(100),'
               '    Name VARCHAR(30),'
               '    Relation VARCHAR(30),'
               '    ID INTEGER,'
               '    PRIMARY KEY(ID, Name)'
               ')')
connection.commit()
cursor.execute('CREATE TABLE Department('
               '    Program VARCHAR(30) PRIMARY KEY'
               ')')
connection.commit()
cursor.close()
