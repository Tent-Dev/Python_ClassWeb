#!\xampp\htdocs\Python_ClassWeb\venv\Scripts\python.exe

import database_connect
import json
import cgi

form = cgi.FieldStorage()
inputId = form.getvalue('id')


print("Content-type:text/html; charset=utf-8\n")

myDB = database_connect.connectdb()

myCursor = myDB.cursor()
if(inputId == None):
    sql_command = """select * from products"""

else:
    sql_command = """select * from products where ProductID = {}""".format(inputId)

myCursor.execute(sql_command)

myResult = myCursor.fetchall()

myList = []
for i in myResult:
    myDic = {"id":"{}".format(i['ProductID']),"name":"{}".format(i['ProductName']),"price":"{}".format(i['UnitPrice'])}

    myList.append(myDic)

if len(myList)>0:
    print(json.dumps(myList))
else:
    print(json.dumps('no'))
