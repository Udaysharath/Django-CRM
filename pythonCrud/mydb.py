import mysql.connector;

dataBase = mysql.connector.Connect(
    host = 'localhost',
    user = 'udaysharath',
    passwd = 'pythonCRUD',
)

# prepare cursorObject
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE pythonCrud")

print("All done!")