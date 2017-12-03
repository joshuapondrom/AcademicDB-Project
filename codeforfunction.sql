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
#Don't forget to display the GPA View

#Generate Instructor Schedule
SELECT 
FROM TaughtBy T, Class C, Room R
WHERE 

#Generate Student Schedule

#Class Sign-Up

