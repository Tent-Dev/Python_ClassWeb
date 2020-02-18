#!\xampp\htdocs\Python_ClassWeb\venv\Scripts\python

import cgi
import hashlib
import sqlite3
import datetime

print("Content-type:text/html\n")
print("<html>")
print("""<head><title> My First page python </title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    </head>""")
print("<body>")
print("<div class='contrainer'>")
print("<div class='row' align='center'>")
form = cgi.FieldStorage()
#รับค่าจาก HTML form อ้างอิง name attribute

get_ProductName = form.getvalue('ProductName')
get_SupplierID = form.getvalue('SupplierID')
get_CategoryID = form.getvalue('CategoryID')
get_QuantityPerUnit = form.getvalue('QuantityPerUnit')
get_UnitPrice = form.getvalue('UnitPrice')
get_UnitsInStock = form.getvalue('UnitsInStock')
get_UnitsOnOrder = form.getvalue('UnitsOnOrder')
get_ReorderLevel = form.getvalue('UnitsOnOrder')
get_Discontinued = form.getvalue('Discontinued')
#now = datetime.datetime.now()
#get_PasswordEncode = hashlib.md5(get_Password.encode()).hexdigest()

def insertDB(sql_command):
    try:
        myDatabase = "database/practice.sqlite3"
        with (sqlite3.connect(myDatabase)) as conn:
            conn.row_factory = sqlite3.Row
            conn.executescript(sql_command)
            print("<div class='col-12'><b>Add Success</b></div>")
            print("<script>setTimeout(function(){window.location.href = 'basicmysql.py';},1000)</script>")


    except:
        print("<div class='col-12'><b>Error</b></div>")

if __name__ == '__main__':

    sql_command = """BEGIN;
                         INSERT INTO products (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
                         VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');
                         COMMIT;""".format(get_ProductName,get_SupplierID,get_CategoryID,get_QuantityPerUnit,get_UnitPrice,get_UnitsInStock,get_UnitsOnOrder,get_ReorderLevel,get_Discontinued)


    insertDB(sql_command)
    print("</div>")
    print("</div>")
    print("</body>")
    print("</html>")
