import cgi
print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1> App Page!</h1>")
form = cgi.FieldStorage()
if form.getvalue("name"):
    name = form.getvalue("name")
    print("<h1>You sent me: " +name+" and so we shall now search for the participating system</h1><br />")
    if form.getvalue("prod"):
        print("<h3>You selected Production!</h3>")
    if form.getvalue("uat"):
        print("<h3>You selected UAT bro!!</h3>")
    if form.getvalue("prodfix"):
        print("<h3>You selected ProdFix bro!!</h3>")
    if form.getvalue("sit"):
        print("<h3>You selected SIT!!</h3>")
    if form.getvalue("dev"):
        print("<h3>You selected Dev bro!!</h3>")
print("</body></html>")

print(f"F yes!! {name}")