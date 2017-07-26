#!/usr/bin/env python3

import bcrypt
import cgi
import cgitb
from pageCreator import createMessagePage
from pageCreator import createSuccessPage
from pageCreator import createBusinessSuccessPage
from databaseOps import createDatabaseConnection
from databaseOps import userExistsInDatabase
from databaseOps import businessExistsInDatabase
from databaseOps import getPasswdHash
from databaseOps import getBusinessPasswdHash
from databaseOps import getUserName
from databaseOps import getBusinessName
from databaseOps import getBusinessURL

def main():

    # For debugging
    cgitb.enable()

    # Create field storage object for retrieving POST parameters
    form = cgi.FieldStorage()

    # Retrieve parameters and hash password with bcrypt
    email = form.getvalue('email')
    passwd = form.getvalue('password')

    #email = "betsydonuts@comcast.net"
    #passwd = "WowThatsGood"

    #email = "bort@hotmail.com"
    #passwd = "EatMyShorts"


    # Create database connection object and cursor
    cnx, cursor = createDatabaseConnection()

    # Check if database connection was successful
    if not cnx or not cursor:
        createMessagePage("Error connecting to database")
        return

    # If user exists in database attempt to authenticate
    if userExistsInDatabase(cursor, email):

        # Assuming user does exist retrieve passwd hash from database        
        db_hash = getPasswdHash(cursor, email)

        # Check given password against hash from database
        if bcrypt.checkpw(passwd.encode(), db_hash.encode()):
            createSuccessPage(getUserName(email).split()[0])
            return
        else:
            createMessagePage("Username/Password incorrect")
            return

    # If business exists in database attempt to authenticate
    elif businessExistsInDatabase(cursor, email):

        # Assuming user does exist retrieve passwd hash from database        
        db_hash = getBusinessPasswdHash(cursor, email)

        # Check given password against hash from database
        if bcrypt.checkpw(passwd.encode(), db_hash.encode()):
            createBusinessSuccessPage(getBusinessName(email), getBusinessURL(email))
            return
        else:
            createMessagePage("Username/Password incorrect")
            return




# Execute main method if script is called directly
if __name__ == '__main__':
    main()
