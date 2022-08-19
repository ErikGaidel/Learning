import cgi, html
r = cgi.FieldStorage()

a = html.escape(r.getvalue("a", ""))
b = html.escape(r.getvalue("b", ""))

message = ""
display = ''' <form name="form" style="margin: 0 auto;" action="/cgi-bin/index1.py" method="post">
<h2>Авторизация</h2> {0}
<label>Логин:</label>
<input type="text" name="a" value="" />
<br />
<br />
<label>Пароль:</label>
<input type="text" name="b" value="" />
<br />
<br />
<input type="submit" value="Войти" />
</form>'''

print("Content-type: text/html; charset=utf-8")
print()
print("<html><head><title>Заголовок</title></head><body style='text-align: center;'>")
print("<h1>Вторая Web-страница!</h1>")
if a == "Admin" and b == "123":
    print("<h1>Welcome admin</h1>")
elif a == "" and b == "":
    print(display.format(message))
else:
    message = "<p style='color: red;'>U entered bad login and/or password!</p>"
    print(display.format(message))
print("</body></html>")

