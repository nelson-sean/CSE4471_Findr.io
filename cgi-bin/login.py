#!/usr/bin/env python3

import bcrypt
import cgi
import cgitb
from pageCreator import createMessagePage
from pageCreator import createSuccessPage
from databaseOps import createDatabaseConnection
from databaseOps import userExistsInDatabase
from databaseOps import getPasswdHash
from databaseOps import getUserName

def main():

    # For debugging
    cgitb.enable()

    # Create field storage object for retrieving POST parameters
    form = cgi.FieldStorage()

    # Retrieve parameters and hash password with bcrypt
    user_email = form.getvalue('email')
    user_passwd = form.getvalue('password')

    #user_email = "bort@hotmail.com"
    #user_passwd = "EatMyShorts"


    # Create database connection object and cursor
    cnx, cursor = createDatabaseConnection()

    # Check if database connection was successful
    if not cnx or not cursor:
        createMessagePage("Error connecting to database")
        return

    # If user does not exist return error message page and exit
    if not userExistsInDatabase(cursor, user_email):
        createMessagePage("Username/Password incorrect")
        return


    # Assuming user does exist retrieve passwd hash from database        
    db_hash = getPasswdHash(cursor, user_email)

    if bcrypt.checkpw(user_passwd.encode(), db_hash.encode()):
        createSuccessPage(getUserName(cursor, user_email).split()[0])
    else:
        createMessagePage("Username/Password incorrect")


# Execute main method if script is called directly
if __name__ == '__main__':
    main()
