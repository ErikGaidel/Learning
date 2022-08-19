import cgi, http.cookies, os, html

message = ""
display = ''' <form name="form" style="margin: 0 auto;" action="/cgi-bin/cookie.py" method="post">
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

r = cgi.FieldStorage()

a = html.escape(r.getvalue("a", ""))
b = html.escape(r.getvalue("b", ""))


print("Content-type: text/html; charset=utf-8")
print()
print("<html><head><title>Заголовок</title></head><body style='text-align: center;'>")
print("<h1>Третья  Web-страница!</h1>")

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
log = cookie.get('log')
password = cookie.get("password")

if log == "Admin" and password == "123":
    print("<h1>Welcome admin</h1>")
elif a == "Admin" and b == "123":
    print("<h1>Welcome admin</h1>")
    print("<a Set-cookie: log=" + a + "</a>")
    print("<a Set-cookie: password=" + b + "</a>")
elif a == "" and b == "":
    print(display.format(message))
else:
    message = "<p style='color: blue;'>U entered bad login and/or password!</p>"
    print(display.format(message))

print("</body></html>")

