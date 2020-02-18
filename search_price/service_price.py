#!\xampp\htdocs\Python_ClassWeb\venv\Scripts\python.exe

import database_connect
import json
import cgi

form = cgi.FieldStorage()
inputPrice = form.getvalue('price')
inputSort = form.getvalue('sort')
sort_select = "ASC"
if(inputSort == '1'):
    sort_select = "ASC"

elif(inputSort == '2'):
    sort_select = "DESC"


print("Content-type:text/html; charset=utf-8\n")

myDB = database_connect.connectdb()
myCursor = myDB.cursor()

if(inputPrice == None):
    sql_command = """select * from products Order by UnitPrice"""

else:
    sql_command = """select * from products where UnitPrice >= {} Order by UnitPrice {}""".format(inputPrice,sort_select)

#print(sql_command)
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
