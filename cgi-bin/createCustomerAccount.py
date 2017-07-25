#!/usr/bin/env python3

import bcrypt
import cgi
import cgitb
import mysql.connector as mariadb

cgitb.enable()

form = cgi.FieldStorage()

name = form.getvalue('name')
email = form.getvalue('email')
passwd = form.getvalue('password')
passwd = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

print("Content-type: text/html")
print()

site_string = '''
<html>
    <head>
        <title>Testing testing</title>
    </head>
    <body>
        Hello there {}</br>
        Email: {}</br>
        Hashed Password: {}
    </body>
</html>
'''.format(name, email, passwd)

print(site_string)
