#!/usr/bin/env python3

import bcrypt
import cgi
import cgitb
import configparser
import base64
import mysql.connector as mariadb
from pageCreator import createMessagePage
from pageCreator import createBusinessSuccessPage
from pageCreator import createNewBusinessProfile
from databaseOps import createDatabaseConnection
from databaseOps import businessExistsInDatabase
from databaseOps import addBusinessToDatabase




def main():

    # For debugging
    cgitb.enable()


    # Create field storage object for retrieving POST parameters
    form = cgi.FieldStorage()

    # Retrieve parameters and hash password with bcrypt
    bus_name = form.getvalue('name')
    bus_email = form.getvalue('email')
    bus_passwd = form.getvalue('password')
    bus_passwd = bcrypt.hashpw(bus_passwd.encode(), bcrypt.gensalt())

    #bus_name   = "ASDF"
    #bus_email  = "ASDFASDF"
    #bus_passwd = "ASDF"
    #bus_passwd = bcrypt.hashpw(bus_passwd.encode(), bcrypt.gensalt())

    # Create profile URL by base64 encoding email
    prof_url = "{}.html".format(base64.b64encode(bus_email.encode()).decode())
    

    # Create database connection object and cursor
    cnx, cursor = createDatabaseConnection()

    # If either connection object is null something has gone wrong
    if not cnx or not cursor:
        createMessagePage("Error connecting to database")
        return

    # If user already exists redirect them to login page
    if businessExistsInDatabase(cursor, bus_email):
        createMessagePage("An account with this email already exists")
        return


    # Add new account to database
    addBusinessToDatabase(cursor, bus_name, bus_email, bus_passwd, prof_url)


    # Create new profile page
    createNewBusinessProfile(bus_name, prof_url)

    # Go to success page
    createBusinessSuccessPage(bus_name, prof_url)
    

    # Cleanly close database connections
    cnx.commit()
    cursor.close()
    cnx.close()




# Execute main method if script is called directly
if __name__ == '__main__':
    main()
