#!\xampp\htdocs\python_web\venv\Scripts\python

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
print("<div class='contrainer' align='center'>")
print("<div class='row' align='center'>")
form = cgi.FieldStorage()
get_Username = form.getvalue('Username')
get_Password = form.getvalue('Password')
now = datetime.datetime.now()
#get_PasswordEncode = hashlib.md5(get_Password.encode()).hexdigest()


def checkDB(sql_command):
    try:
        myDatabase = "database/practice.sqlite3"
        with (sqlite3.connect(myDatabase)) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(sql_command).fetchone()
            if(cursor):
                print("<div class='col-12' align='center'><div class='col-6 alert alert-success' role='alert'>Login Success {}</div></div>".format(cursor))
                print("<div class='col-12' align='center'><b>Your Username is</b></div>")
                print("<div class='col-12' align='center'><h1>{}</h1></div>".format(get_Username))
                print("<div class='col-12' align='center'><b>Last access {}</b></div>".format(now))
                print("<div class='col-12' align='center'>Redirect to basicmysql.py in 2 seconds</div>")
                print("<script>setTimeout(function(){window.location.href = 'basicmysql.py';},2000)</script>")
            else:
                print("<div class='col-12' align='center'><div class='col-6 alert alert-danger' role='alert'>Login Fail</div></div>")
                print("<div class='col-12' align='center'><b>Your Username or Password is wrong</b></div>")
    except:
        print("<div class='col-12'><b>Error</b></div>")

if __name__ == '__main__':

    sql_command = """SELECT username,password FROM users WHERE username = '{}' and password = '{}'""".format(get_Username,get_Password)
    checkDB(sql_command)
    print("</div>")
    print("</div>")
    print("</body>")
    print("</html>")

