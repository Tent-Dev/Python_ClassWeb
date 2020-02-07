#!\xampp\htdocs\Python_ClassWeb\venv2\Scripts\python.exe
import pymysql
import cgi
import csv
from datetime import datetime

# Static Variable
form = cgi.FieldStorage()
conn = None
debugging = True
DatabaseName = "py_northwind"


# HTML Render
def renderHTML():
    renderHeader()
    renderBody()
    renderFooter()

def renderHeader():
    print("<head>")
    print("""<head><title> My First page python </title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/js/all.min.js" integrity="sha256-MAgcygDRahs+F/Nk5Vz387whB4kSK9NXlDN3w58LLq0=" crossorigin="anonymous"></script>
            </head>""")
    renderCSS()
    renderJS()
    print("</head>")

def renderBody():
    print("<body>")
    print("<nav class='navbar navbar-expand-lg navbar-dark bg-dark'>")
    print("<a class='navbar-brand' href='#'>Python Web Class</a>")
    print(
        "<button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarNav' aria-controls='navbarNav' aria-expanded='false' aria-label='Toggle navigation'>")
    print("<span class='navbar-toggler-icon'></span>")
    print("</button>")
    print("<div class='collapse navbar-collapse' id='navbarNav'>")
    print("<ul class='navbar-nav'>")
    print("<li class='nav-item'>")
    print("<a class='nav-link' href='basicmysql.py'>Home <span class='sr-only'>(current)</span></a>")
    print("</li>")
    print("<li class='nav-item'>")
    print("<a class='nav-link' href='insert.py'>Add Product</a>")
    print("</li>")
    print("<li class='nav-item active'>")
    print("<a class='nav-link' href='CUID.py'>Customer Management</a>")
    print("</li>")
    print("<li class='nav-item'>")
    print("<a class='nav-link disabled' href='#' tabindex='-1' aria-disabled='true'>Disabled</a>")
    print("</li>")
    print("</ul>")
    print("</div>")
    print("</nav><br>")
    print("<div class='contrainer' align='center'>")
    if(string(form.getvalue("updid")) != "" and string(form.getvalue("updid")) != "None"):
        #print("{}".format(form.getvalue("updid")))
        renderUpdateForm()
    else:
        print("<h1>Home</h1>")
        renderPcountryuctForm()
    renderPcountryuctTable()
    print("</div>")
    print("</body>")

def renderFooter():
    print("<foot>")
    print("</foot>")

def renderJS():
    # Java Script confirm before update / delete
    print("""
        <script>
            function delPcountryuct(el){
                pname = el.attributes["pname"].value
                if(!confirm("Do you really want to delete " + pname + " ?"))
                    return false
            }
            function updatePcountryuct(el){
                pname = el.attributes["pname"].value
                if(!confirm("Do you want to update " + pname + " ?"))
                    return false
            }
        </script>
    """)

def renderCSS():
    print("""
        <style>
            #pcountryuct-table{
                width: 800px;
            }
            #pcountryuct-table th{
                background-color: #8A1F1F;
                color: #FFF;
            }
            #pcountryuct-table tr:nth-child(odd) td{
                background-color: #FF08080;
            }
            #pcountryuct-table tr:nth-child(even) td{
                background-color: #FCA6A6;
            }
        </style>
    """)

# Error HTML Render
def renderError(e):
    print("<title>ERROR</title>")
    print("<h1>Server Error</h1>")
    print("<p>{0}</p>".format(e))

# HTML Form Render

def renderPcountryuctForm():
    with open('Country/customers.csv',mode='r') as f:
        result = f.read().splitlines()

    print("""
        <form action="CUID.py" method="post" class='form-group'>
            <table>
                <tr>
                    <td>Company Name</td>
                    <td><input type="text" name="company_name" class="form-control"></td>
                </tr>
                 <tr>
                    <td>Contact Name</td>
                    <td><input type="text" name="contact_name" class="form-control"></td>
                </tr>
                <tr>
                    <td>Contact Title</td>
                    <td><input type="text" name="contact_title" class="form-control"></td>
                </tr>
                <tr>
                    <td>Address</td>
                    <td><input type="text" name="address" class="form-control"></td>
                </tr>
                 <tr>
                    <td>City</td>
                    <td><input type="text" name="city" class="form-control"></td>
                </tr>
                 <tr>
                    <td>Region</td>
                    <td><input type="text" name="region" class="form-control"></td>
                </tr>
                <tr>
                    <td>Postal Code</td>
                    <td><input type="text" name="postal_code" class="form-control"></td>
                </tr>
                <tr>
                    <td>Country</td>
                    <td>
                        <select name="country" class="form-control">
    """)
    for row in result:
        print("""<option value="{0}">{1}</option>""".format(row,row))
    print("""
                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Phone</td>
                    <td><input type="text" name="phone" class="form-control"></td>
                </tr>
                <tr>
                    <td>Fax</td>
                    <td><input type="text" name="fax" class="form-control"></td>
                </tr>
                <tr>
                    <input type="hidden" name="status" value="create">
                    <td><div class='col-12' align='center'><input type="submit" value="Add CUSTOMER" class="btn btn-success"></input></div></td>
                </tr>
            </table>
        </form>
    """)
def renderUpdateForm():
    pid = string(form.getvalue("updid"),"")
    if(pid == 0):
        return
    sql = """
        SELECT *
        FROM customers
        WHERE CustomerID = '{0}'
    """.format(pid)
    result = executeSQL(sql)
    if(result[0] == 0):
        return
    pcountryuct = result[1].fetchone()

    with open('Country/customers.csv',mode='r') as f:
        result = f.read().splitlines()

    print("""
        <h1>Update Customers</h1>
        <form action="CUID.py" method="post" class='form-group'>
            <table>
                <tr>
                    <td>Company Name</td>
                    <td><input type="text" name="company_name" value="{0}" class='form-control'></td>
                </tr>
                 <tr>
                    <td>Contact Name</td>
                    <td><input type="text" name="contact_name" value="{1}" class='form-control'></td>
                </tr>
                <tr>
                    <td>Contact Title</td>
                    <td><input type="text" name="contact_title" value="{2}" class='form-control'></td>
                </tr>
                <tr>
                    <td>Address</td>
                    <td><input type="text" name="address" value="{3}" class='form-control'></td>
                </tr>
                 <tr>
                    <td>City</td>
                    <td><input type="text" name="city" value="{4}" class='form-control'></td>
                </tr>
                 <tr>
                    <td>Region</td>
                    <td><input type="text" name="region" value="{5}" class='form-control'></td>
                </tr>
                <tr>
                    <td>Postal Code</td>
                    <td><input type="text" name="postal_code" value="{6}" class='form-control'></td>
                </tr>
                <tr>
                        <td>Country</td>
                    <td>
                        <select name="country" class='form-control'>
    """.format(pcountryuct[1], pcountryuct[2], pcountryuct[3], pcountryuct[4], pcountryuct[5], pcountryuct[6], pcountryuct[7]))
    for row in result:
        isDefault = ""
        if(row == pcountryuct[8]):
            isDefault = "selected"
        print("""<option value="{0}" {2}>{1}</option>""".format(row,row,isDefault))
    print("""
                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Phone</td>
                    <td><input type="text" name="phone" value="{0}" class='form-control'></td>
                </tr>
                <tr>
                    <td>Fax</td>
                    <td><input type="text" name="fax" value="{1}" class='form-control'></td>
                </tr>
                <tr>
                    <td>
                        <input type="hidden" name="status" value="update">
                        <input type="hidden" name="updid" value="{2}">
                        <input type="submit" value="SAVE PcountryUCT" class='btn btn-warning'>
                    </td>
                </tr>
            </table>
        </form>
    """.format(pcountryuct[9], pcountryuct[10], pid))

# HTML Output render
def renderPcountryuctTable():
    sql = """
        SELECT *
        FROM customers
    """
    result = executeSQL(sql)
    print("Result: {0} record(s)".format(result[0]))
    if(result[0] > 0):
        print("""
        <div class="col-9">
            <table class="table table-striped table-dark" id="" cellspacing="0" cellpadding="0" style="font-size: 0.75em;">
                <thead>
                    <tr>
                    <th width="10%">No.</th>
                    <th>Company Name</th>
                    <th>Contact Name</th>
                    <th>Contact Title</th>
                    <th>Address</th>
                    <th>City</th>
                    <th>Region</th>
                    <th>Postal Code</th>
                    <th>Country</th>
                    <th>Phone</th>
                    <th>Fax</th>
                    <th></th>
                    <th></th>
                    </tr>
                </thead>
        """)
        for i,row in enumerate(result[1]):
            print("""
                <tr>
                    <td align="center">{0}</td>
                    <td>{1}</td>
                    <td>{2}</td>
                    <td>{3}</td>
                    <td>{4}</td>
                    <td>{5}</td>
                    <td>{6}</td>
                    <td>{7}</td>
                    <td>{8}</td>
                    <td>{9}</td>
                    <td>{10}</td>
                    <td><a href="CUID.py?delid={11}" onclick="return delPcountryuct(this)" pname="{1}"><button class='btn btn-danger'><i class="fas fa-trash-alt"></i></button</a></td>
                    <td><a href="CUID.py?updid={11}"><button class='btn btn-warning'><i class="fas fa-pen"></i></button></a></td>
                </tr>
            """.format(i+1,row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[0]))
        print("</table><div class='col-12'>")

# CUD Pcountryuct
def insertPcountryuct():
    saved = False
    if(string(form.getvalue("status")) != "create"):
        return saved
    # reqData = {"company_name","contact_name","contact_title","address","city","region","postal_code","country"}
    # if(not reqData.issubset(form.keys())):
    #     return saved
    customer_id = string(form.getvalue("company_name")[:5],"NULL").upper()
    company_name = string(form.getvalue("company_name"),"NULL")
    contact_name = string(form.getvalue("contact_name"),"NULL")
    contact_title = string(form.getvalue("contact_title"),"NULL")
    address = string(form.getvalue("address"),"NULL")
    city = string(form.getvalue("city"),"NULL")
    region = string(form.getvalue("region"),"NULL")
    postal_code = string(form.getvalue("postal_code"),"NULL")
    country = string(form.getvalue("country"),"NULL")
    phone = string(form.getvalue("phone"),"NULL")
    fax = string(form.getvalue("fax"), "NULL")

    sql = """
        INSERT INTO customers (CustomerID, CompanyName,ContactName,ContactTitle,Address,City,Region,PostalCode,Country,Phone,Fax) 
        VALUES ({10},"{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}")
    """.format(company_name,contact_name,contact_title,address,city,region,postal_code,country,phone,fax,customer_id)
    result = executeInsertSQL(sql)
    if(result[0] == 1):
        saved = True
        actionLog("I",result[1])
    return saved
def updatePcountryuct():
    saved = False
    if(string(form.getvalue("status")) != "update"):
        return saved
    reqData = {"updid"}
    if(not reqData.issubset(form.keys())):
        return saved
    pid = string(form.getvalue("updid"))
    if(pid == ""):
        return saved
    company_name = string(form.getvalue("company_name"))
    contact_name = string(form.getvalue("contact_name"),"NULL")
    contact_title = string(form.getvalue("contact_title"),"NULL")
    address = string(form.getvalue("address"),"NULL")
    city = string(form.getvalue("city"),"NULL")
    region = string(form.getvalue("region"),"NULL")
    postal_code = string(form.getvalue("postal_code"),"NULL")
    country = string(form.getvalue("country"),"NULL")
    phone = string(form.getvalue("phone"),"NULL")
    fax = string(form.getvalue("fax"), "NULL")
    sql = """
        UPDATE customers 
        SET CompanyName = "{0}",ContactName="{1}",ContactTitle="{2}",Address="{3}",City="{4}",Region="{5}",PostalCode="{6}",Country="{7}",Phone="{8}",Fax="{10}"
        WHERE CustomerID = "{9}"
    """.format(company_name,contact_name,contact_title,address,city,region,postal_code,country,phone,pid,fax)
    result = executeNonQuerySQL(sql)
    if(result == 1):
        saved = True
        actionLog("U",pid)
    return saved

def deletePcountryuct():
    deleted = False
    delid = string(form.getvalue("delid"))
    if(delid != 0):
        sql = """
            DELETE FROM customers
            WHERE CustomerID = '{0}'
        """.format(form.getvalue("delid"))
        result = executeNonQuerySQL(sql)
        if(result == 1):
            deleted = True
            actionLog("D",delid)
    return deleted

# Database
def connectDB():
    global conn
    if(conn is None):
        conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db=DatabaseName)
    return conn

def closeDBConnect():
    if(conn != None):
        conn.close()

def executeSQL(sql):
    conn = connectDB()
    cur = conn.cursor()
    count = cur.execute(sql)
    cur.close()
    return (count,cur)

def executeNonQuerySQL(sql):
    conn = connectDB()
    cur = conn.cursor()
    count = cur.execute(sql)
    conn.commit()
    cur.close()
    return count

def executeInsertSQL(sql):
    conn = connectDB()
    cur = conn.cursor()
    count = cur.execute(sql)
    sqlGetInsertedID = """
        SELECT LAST_INSERT_ID()
    """
    cur.execute(sqlGetInsertedID)
    insertedID = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return (count,insertedID)

# Logging
def actionLog(action,target):
    existAction = {"I","U","D"}
    if(action not in existAction):
        return
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    row = [action,time,target]
    with open("./LogData/data.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

def errorLog(error):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [time,error]
    try:
        with open("./LogData/error.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(row)
    except Exception:
        print("Fatal Error: cannot log error.")

# Miscellaneous
def string(s,default=""):
    try:
        return str(s)
    except Exception:
        return default

def integer(i,default=0):
    try:
        return int(i)
    except TypeError:
        return default
    except ValueError:
        return default

def parseFloat(f,default=0):
    try:
        return float(f)
    except TypeError:
        return default
    except ValueError:
        return default

# Main
if __name__ == "__main__":
    print("Content-type:text/html\n")
    try:
        insertPcountryuct()
        updatePcountryuct()
        deletePcountryuct()
        renderHTML()
    except Exception as e:
        errorLog(e)
        if(debugging):
            renderError(e)
        else:
            renderError("Contact admin for more detail.")
    closeDBConnect()
