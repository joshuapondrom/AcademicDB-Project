#For all of the following queries, I used given_varname as a place holder for the actual values

#Get Person Info
SELECT *
FROM EmergencyContact E, Student S, Instructor I
WHERE (E.ID = S.ID AND S.ID = given_id) OR  (E.ID = I.ID AND I.ID = given_id)
#I think this should work /\ just replace given_id with the actual variable

#Search For a Class
SELECT *
FROM Class C
WHERE C.Course_ID = given_courseID
#This is a simple one

#Lookup Degree Progress
#Taken
Select *
FROM Takes T
WHERE T.ID = given_id
UNION   #I think this combines the two tables into one big table
Select *
FROM Requires R
WHERE R.taken = false AND R.ID = given_id
#Dont forget to display the GPA View

#Generate Student Schedule
SELECT T.Class_ID, T.Course_ID, C.DayCode, C.Time, R.Room_Number, R.Address
FROM Takes T, ClassInRoom R, Class C
WHERE T.Class_ID = R.Class_ID AND T.Course_ID = R.Course_ID AND T.Class_ID = C.Class_ID AND T.Course_ID = C.Course_ID AND R.Class_ID = C.Class_ID AND R.Course_ID = C.Course_ID

#Generate Student Schedule

#Class Sign-Up
