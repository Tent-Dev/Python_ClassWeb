#!\xampp\htdocs\Python_ClassWeb\venv2\Scripts\python.exe
import pymysql

def connectdb():
    myDB = pymysql.connect(
    host = "localhost",
    port=3306,
    user = "root",
    passwd = "",
    cursorclass=pymysql.cursors.DictCursor,
    database = "py_northwind"
    )
    return myDB
