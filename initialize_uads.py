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
               '    Credit_Hours INTEGER'
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
cursor.execute('CREATE TABLE Department('
               '    Program VARCHAR(30) PRIMARY KEY'
               ')')
connection.commit()
cursor.execute('INSERT INTO Student VALUES (1, "123 Road", "Jack", 1)')
connection.commit()
cursor.execute('INSERT INTO Student VALUES (2, "456 Lane", "Jill", 2)')
connection.commit()
cursor.execute('INSERT INTO Student VALUES (3, "999 Way", "Fred", 3)')
connection.commit()

cursor.execute('INSERT INTO Instructor VALUES (7, "333 Blvd", "Larry", CompSci)')
connection.commit()
cursor.execute('INSERT INTO Instructor VALUES (8, "444 Lane", "Suzzy", MechEng)')
connection.commit()

cursor.execute('INSERT INTO Building VALUES ("12 Miner", "Computer Science Building", "CSB")')
connection.commit()
cursor.execute('INSERT INTO Building VALUES ("13 Miner", "Mechanical Eng Building", "MEB")')
connection.commit()

cursor.execute('INSERT INTO Located VALUES ("CompSci", "12 Miner")')
connection.commit()
cursor.execute('INSERT INTO Located VALUES ("MechEng", "13 Miner")')
connection.commit()

cursor.execute('INSERT INTO Course VALUES ("CS2300", "CompSci", 3)')
connection.commit()
cursor.execute('INSERT INTO Course VALUES ("MCE1120", "MechEng", 3)')
connection.commit()

cursor.execute('INSERT INTO Class VALUES ("L0305", "10101",2,"CS2300")')
connection.commit()
cursor.execute('INSERT INTO Class VALUES ("Y0306", "01010",3,"MCE1120")')
connection.commit()

cursor.execute('INSERT INTO Requires VALUES (1, "CS2300")')
connection.commit()
cursor.execute('INSERT INTO Requires VALUES (2, "MCE1120")')
connection.commit()
cursor.execute('INSERT INTO Requires VALUES (3, "CS2300")')
connection.commit()
cursor.execute('INSERT INTO Requires VALUES (3, "MCE1120")')
connection.commit()

cursor.execute('INSERT INTO TaughtBy VALUES (7, "L0305", "CS2300")')
connection.commit()
cursor.execute('INSERT INTO TaughtBy VALUES (8, "Y0306", "MCE1120")')
connection.commit()

cursor.execute('INSERT INTO Room VALUES ("Classroom", 101, "12 Mines")')
connection.commit()
cursor.execute('INSERT INTO Room VALUES ("Classroom", 101, "13 Mines")')
connection.commit()

cursor.execute('INSERT INTO Takes VALUES (1, "L0305", "CS2300", 3.8)')
connection.commit()
cursor.execute('INSERT INTO Takes VALUES (2, "Y0306", "MCE1120", 4.0)')
connection.commit()
cursor.execute('INSERT INTO Takes VALUES (3, "L0305", "CS2300", 4.0)')
connection.commit()

cursor.execute('INSERT INTO ClassInRoom VALUES ("CS2300", "L0305", 101, "12 Mines")')
connection.commit()
cursor.execute('INSERT INTO ClassInRoom VALUES ("MCE1120", "Y0306", 101, "13 Mines")')
connection.commit()
cursor.close()
