#!/usr/bin/env python3

import bcrypt
import cgi
import cgitb
import configparser
import mysql.connector as mariadb
from pageCreator import createMessagePage
from pageCreator import createSuccessPage
from databaseOps import createDatabaseConnection
from databaseOps import userExistsInDatabase
from databaseOps import addUserToDatabase




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
    createSuccessPage(user_name.split()[0])

    

    # Cleanly close database connections
    cnx.commit()
    cursor.close()
    cnx.close()




# Execute main method if script is called directly
if __name__ == '__main__':
    main()
