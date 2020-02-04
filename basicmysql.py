#!\xampp\htdocs\python_web\venv\Scripts\python

import pymysql
def connectDB():
    con = pymysql.connect(host='localhost',
                          port=3306,
                          user='root',
                          password='',
                          db='py_northwind',
                          cursorclass= pymysql.cursors.DictCursor,
                          autocommit=True)
    return con

print("Content-type:text/html\n")
print("<html>")
print("""<head><title> My First page python </title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    </head>""")
print("<body>")
print("<nav class='navbar navbar-expand-lg navbar-dark bg-dark'>")
print("<a class='navbar-brand' href='#'>Python Web Class</a>")
print("<button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarNav' aria-controls='navbarNav' aria-expanded='false' aria-label='Toggle navigation'>")
print("<span class='navbar-toggler-icon'></span>")
print("</button>")
print("<div class='collapse navbar-collapse' id='navbarNav'>")
print("<ul class='navbar-nav'>")
print("<li class='nav-item active'>")
print("<a class='nav-link' href='basicmysql.py'>Home <span class='sr-only'>(current)</span></a>")
print("</li>")
print("<li class='nav-item'>")
print("<a class='nav-link' href='insert.py'>Add Product</a>")
print("</li>")
print("<li class='nav-item'>")
print("<a class='nav-link' href='#'>Pricing</a>")
print("</li>")
print("<li class='nav-item'>")
print("<a class='nav-link disabled' href='#' tabindex='-1' aria-disabled='true'>Disabled</a>")
print("</li>")
print("</ul>")
print("</div>")
print("</nav><br>")
print("<div class='contrainer' align='center'>")

#cursorclass= pymysql.cursors.DictCursor ทำให้อ้างอิงด้วยชื่อ field ได้
curr = connectDB().cursor() #เก็บข้อมูลเป็นแถวๆ
sql_command = """   select * from products
                    join suppliers on products.SupplierID = suppliers.SupplierID
                    join categories on products.CategoryID = categories.CategoryID"""

curr.execute(sql_command)
print("<div class='col-6' align='center'><h1>Product List</h1></div>")
print("<div class='col-10' align='center'>")
print("<table class='table'>")
print("<thead><tr><th scope='col'>#</th><th scope='col'>Product ID</th><th scope='col'>Product Name</th><th scope='col'>Unit Price</th><th scope='col'>Supplier Name</th><th scope='col'>Category Name</th></tr></thead><tbody>");
j = 1
for row in curr:
    print("<tr>")
    print("<td>#{}</td>".format(j))
    print("<td>{}</td>".format(row['ProductID']))
    print("<td>{}</td>".format(row['ProductName']))
    print("<td>{}</td>".format(row['UnitPrice']))
    print("<td>{}</td>".format(row['CompanyName']))
    print("<td>{}</td>".format(row['CategoryName']))
    print("</tr>")
    j+=1

print("</tbody></table>")
print("</div>")
print("</div>")
print("</div>")
print("</body>")
print("</html>")
