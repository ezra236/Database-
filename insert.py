import mysql.connector

database= mysql.connector.connect(
    host = "localhost",
    user =  "root",
    password = "",
    database = "StudentPortal"
)

objectt = database.cursor()

sql = "INSERT INTO Students (Name, AdmissionNumber, DateOfBirth, Email, Course) VALUES (%s, %s, %s, %s, %s)"
val = [("John Doe", "A12345", "2000-05-15", "john.doe@example.com", "Computer Science"),
       ("Jane Smith", "A12346", "1999-11-22", "jane.smith@example.com", "Mathematics"),
       ("Emily Johnson", "A12348", "2000-07-30", "michael.brown@example.com", "Biology")]

objectt.executemany(sql, val)
database.commit()

database.close()
