#!/usr/bin/env python3

import bcrypt
import cgi
import cgitb
import configparser
import mysql.connector as mariadb


def addUserToDatabase(cursor, user_name, user_email, user_passwd):

    query = ("INSERT INTO USER VALUES( "
                "%(user_name)s, "
                "%(user_email)s, "
                "%(user_passwd)s);"
            )

    cursor.execute(
        query,
        {
            "user_name": user_name,
            "user_email": user_email,
            "user_passwd": user_passwd
        }
    )


def main():

    # For debugging
    cgitb.enable()


    # Create field storage object for retrieving POST parameters
    form = cgi.FieldStorage()

    # Retrieve parameters and hash password with bcrypt
    user_name = form.getvalue('name')
    user_email = form.getvalue('email')
    user_passwd = form.getvalue('password')
    user_passwd = bcrypt.hashpw(user_passwd.encode(), bcrypt.gensalt())

    # Create database connection object and cursor
    cnx, cursor = createDatabaseConnection()

    # If either connection object is null something has gone wrong
    if not cnx or not cursor:
        createMessagePage("Error connecting to database")
        return

    # If user already exists redirect them to login page
    if userExistsInDatabase(cursor, user_email):
        createMessagePage("User already exists")
        return

    addUserToDatabase(cursor, user_name, user_email, user_passwd)
    createMessagePage("I tried")

    # Cleanly close database connections
    cnx.commit()
    cursor.close()
    cnx.close()



def createDatabaseConnection():

    # Retrieve database credentials
    config = configparser.ConfigParser()
    config.read('/etc/apache2/cred/cred.conf')
    db_username = config.get('credentials', 'username')
    db_pass = config.get('credentials', 'password')

    # Create Database connection
    try:
        cnx = mariadb.connect(
            user=db_username,
            password=db_pass,
            host='localhost',
            database='findr'
        )

        cursor = cnx.cursor()

        return cnx, cursor

    except mariadb.Error as err:
        if err.errno == mariadb.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect username or password")
            return None, None
        elif err.errno == mariadb.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return None, None

def userExistsInDatabase(cursor, user_email):

    # Construct query to check for user email in database
    query = ("SELECT * "
                "FROM USER "
                "WHERE EMAIL = %(email)s")

    # Execute query against database
    cursor.execute(query, {"email": user_email})

    dbreturn = False

    # Retrieve rows from cursor
    for (NAME, EMAIL, PASSWD_HASH) in cursor:
        dbreturn=True
    
    return dbreturn

def createMessagePage(message):

    # Print required response header
    print("Content-type: text/html")
    print()

    page_string = '''
<!DOCTYPE html>
<html class="w3-light-grey">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="../w3.css">
        <title>Login</title>
        <style>
            body,h1,h2,h3,h4,h5 {font-family: "Poppins", sans-serif}
        </style>
    </head>
    <body>
        <header class="w3-container w3-blue w3-center">
            <form class="w3-right-align">
                Login:
                <input type="text" name="email" class="w3-margin">
                Password:
                <input type="password" name="password" class="w3-margin">
                <button class="w3-button w3-light-grey w3-medium">Login</button>
            </form>
            <h1 class="w3-jumbo" style="margin-top: -10px; margin-bottom: 50px">Findr.io</h1>
        </header>
        <div class="w3-center w3-container w3-jumbo">
'''
    print(page_string)
    print(message)
    page_string = '''
            <form action="../login.html">
                <button class="w3-button w3-blue w3-medium">Return to Login</button>
            </form>
        </div>
        <footer class="w3-container w3-padding-64 w3-center w3-blue w3-bottom">  
        </footer>
    </body>
</html>
'''
    print(page_string)

# Execute main method if script is called directly
if __name__ == '__main__':
    main()
