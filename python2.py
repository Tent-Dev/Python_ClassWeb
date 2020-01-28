#!\xampp\htdocs\python_web\venv\Scripts\python
print("Context-type:text/html\n")
print("<html>")
print("<head><title> My First page python </title></head>")
print("<body>")
i = 1
while(i<=6):
    print("<i><h{}>Python <u>on</u> web</h{}><i>".format(i,i))
    i+=1
print("</body>")
print("</html>")
