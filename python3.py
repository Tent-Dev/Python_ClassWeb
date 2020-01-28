#!\xampp\htdocs\python_web\venv\Scripts\python
import random
print("Content-type:text/html\n")
print("<html>")
print("<head><title> My First page python </title></head>")
print("<body>")
print("<table border='1'>")
i = 1
j=1
i_end = 10
j_end = 7
while(i<=i_end):
    print("<tr>")

    if i%2 ==0:
        ccode = "teal"
    else:
        ccode = "#FFF"

    while(j<=j_end):
        ran = random.randint(1,6)
        if i==1 or i ==i_end or j==1 or j==j_end:

            print("<td align='center'><img src='images/lvp{}.JPG' width='50px' height='50px'></td>".format(ran))
        else:
            if i == j:
                atag = "<b><a href='#'>"
                etag = "</a></b>"
            else:
                atag = ""
                etag = ""
            print("<td bgcolor='{}'>{}Chutipas{}</td>".format(ccode,atag,etag))
        j+=1
    print("</tr>")
    i+=1
    j = 1
print("</table>")
print("</body>")
print("</html>")
