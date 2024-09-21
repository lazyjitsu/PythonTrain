
import cgi
print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1>Welcome to my System Design App12</h1>")

form = cgi.FieldStorage()

if form.getvalue("name"):
    name = form.getvalue("name")
    print("<h1>Hello" +name+"! Thanks for using me!!</h1><br />")

if form.getvalue("happy"):
    print("<p> Yah I'm happy!! </p>")
if form.getvalue("sad"):
    print("<p> oh no u are sad</p>")
me='salad bo!!'
print("<form method='post' action='z.py'>")
print("<p>Object Name: <input type='text' name='name'/></p>")
print("<input type='checkbox' name='prod' /> Production")
print("<input type='checkbox' name='uat' /> UAT")
print("<input type='checkbox' name='prodfix' /> ProdFix")
print("<input type='checkbox' name='sit' /> SIT")
print("<input type='checkbox' name='dev' /> Dev")
print("<input type='submit' value='Submit Me' />")
print("</form>")
print("</body></html>")