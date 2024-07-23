import mysql.connector

database= mysql.connector.connect(
    host = "localhost",
    user =  "root",
    password = ""
)

objectt = database.cursor()

objectt.execute("CREATE DATABASE StudentPortal")

database.close()
