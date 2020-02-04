#!\xampp\htdocs\python_web\venv\Scripts\python
print("Content-type:text/html\n")
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
print("<html>")
print("""<head><title> My First page python </title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <style>
        .margin-10{
            margin-bottom: 10px;
        }
    </style>
    </head>""")
print("<body>")
print("<nav class='navbar navbar-expand-lg navbar-dark bg-dark'>")
print("<a class='navbar-brand' href='#'>Python Web Class</a>")
print("<button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarNav' aria-controls='navbarNav' aria-expanded='false' aria-label='Toggle navigation'>")
print("<span class='navbar-toggler-icon'></span>")
print("</button>")
print("<div class='collapse navbar-collapse' id='navbarNav'>")
print("<ul class='navbar-nav'>")
print("<li class='nav-item'>")
print("<a class='nav-link' href='basicmysql.py'>Home</a>")
print("</li>")
print("<li class='nav-item active'>")
print("<a class='nav-link' href='insert.py'>Add Product <span class='sr-only'>(current)</span></a>")
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
print("<form class='form-group'>")
print("<div class='row'>")

print("<div class='col-12'>")
print("<h1>Add Product</h1>")
print("</div>")
#----------------Form------------------------
print("<div class='col-12 row margin-10'>")
print("<div class='col-4' align='right'>")
print("Product Name : ")
print("</div>")
print("<div class='col-4'>")
print("<input type='text' class='form-control'>")
print("</div>")
print("</div>")

print("<div class='col-12 row margin-10'>")
print("<div class='col-4' align='right'>")
print("Supplier Name : ")
print("</div>")
print("<div class='col-2'>")
curr = connectDB().cursor() #เก็บข้อมูลเป็นแถวๆ
sql_command = """select * from suppliers"""

curr.execute(sql_command)
print("<select class='custom-select mr-sm-2' id='inlineFormCustomSelect'><option selected>Choose...</option>")
for row in curr:
    print("<option value='{}'>{}</option>".format(row['SupplierID'],row['CompanyName']))
print("</select>")
print("</div>")
print("</div>")

print("<div class='col-12 row margin-10'>")
print("<div class='col-4' align='right'>")
print("Category Name : ")
print("</div>")
print("<div class='col-2'>")
curr = connectDB().cursor() #เก็บข้อมูลเป็นแถวๆ
sql_command = """select * from categories"""

curr.execute(sql_command)
print("<select class='custom-select mr-sm-2' id='inlineFormCustomSelect'><option selected>Choose...</option>")
for row in curr:
    print("<option value='{}'>{}</option>".format(row['CategoryID'],row['CategoryName']))
print("</select>")
print("</div>")
print("</div>")

print("<div class='col-12 row margin-10'>")
print("<div class='col-4' align='right'>")
print("QuantityPerUnit : ")
print("</div>")
print("<div class='col-2'>")
print("<input type='text' class='form-control'>")
print("</div>")
print("</div>")

print("<div class='col-12 row margin-10'>")
print("<div class='col-4' align='right'>")
print("Unit Price : ")
print("</div>")
print("<div class='col-2 input-group'>")
print("<input type='text' class='form-control'>")

print("<div class='input-group-prepend'><div class='input-group-text'>$</div></div>")
print("</div>")
print("</div>")

print("<div class='col-12 row margin-10'>")
print("<div class='col-4' align='right'>")
print("Unit in Stock : ")
print("</div>")
print("<div class='col-2'>")
print("<input type='text' class='form-control'>")
print("</div>")
print("</div>")

print("<div class='col-12 row margin-10'>")
print("<div class='col-4' align='right'>")
print("Unit on Order : ")
print("</div>")
print("<div class='col-2'>")
print("<input type='text' class='form-control'>")
print("</div>")
print("</div>")

print("<div class='col-12 row margin-10'>")
print("<div class='col-4' align='right'>")
print("Re Order Level : ")
print("</div>")
print("<div class='col-2'>")
print("<input type='text' class='form-control'>")
print("</div>")
print("</div>")

print("<div class='col-12 row margin-10'>")
print("<div class='col-4' align='right'>")
print("Discontinued : ")
print("</div>")
print("<div class='col-2'>")
print("<input class='form-check-input' value='0' type='checkbox' id='Discontinued'>")
print("</div>")
print("</div>")
print("<div class='col-12' align='center'><a href='insert_cmd.py'><input type='button' class='btn btn-success' value='Add Product'></a></div>")
#-----------------end Form-----------------------
print("</div>")
print("</form>")
print("</div>")
print("</body>")
print("""<script>
    $('#Discontinued').on('click',function(){
    if($(this).val() == 0){
        $(this).val(1)
    }else{
        $(this).val(0)
    }
    });
</script>""")
print("</html>")
