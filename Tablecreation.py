import mysql.connector

database= mysql.connector.connect(
    host = "localhost",
    user =  "root",
    password = "",
    database = "StudentPortal"
)

objectt = database.cursor()

sql = """CREATE TABLE Students(
          StudentID INT AUTO_INCREMENT PRIMARY KEY,
          Name VARCHAR(100),
          AdmissionNumber VARCHAR(20),
          DateOfBirth DATE,
          Email VARCHAR(100),
          Course VARCHAR(100)
         ) """

objectt.execute(sql)

database.close()
