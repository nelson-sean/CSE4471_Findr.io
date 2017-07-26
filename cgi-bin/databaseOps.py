#!/usr/bin/env python3

import configparser
import mysql.connector as mariadb


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
                "FROM CUSTOMER "
                "WHERE EMAIL = %(email)s")

    # Execute query against database
    cursor.execute(query, {"email": user_email})

    dbreturn = False

    # Retrieve rows from cursor
    for (NAME, EMAIL, PASSWD_HASH) in cursor:
        dbreturn=True
    
    return dbreturn

def businessExistsInDatabase(cursor, bus_email):

    # Construct query to check for user email in database
    query = ("SELECT * "
                "FROM BUSINESS "
                "WHERE EMAIL = %(email)s")

    # Execute query against database
    cursor.execute(query, {"email": bus_email})

    dbreturn = False

    # Retrieve rows from cursor
    for (NAME, EMAIL, PASSWD_HASH, PROFILE_URL) in cursor:
        dbreturn=True
    
    return dbreturn

def addUserToDatabase(cursor, user_name, user_email, user_passwd):

    # Construct insert query
    query = ("INSERT INTO CUSTOMER VALUES( "
                "%(user_name)s, "
                "%(user_email)s, "
                "%(user_passwd)s);"
            )

    # Execute query with provided values
    cursor.execute(
        query,
        {
            "user_name": user_name,
            "user_email": user_email,
            "user_passwd": user_passwd
        }
    )

def addBusinessToDatabase(cursor, bus_name, bus_email, bus_passwd, prof_url):

    # Construct insert query
    query = ("INSERT INTO BUSINESS VALUES( "
                "%(bus_name)s, "
                "%(bus_email)s, "
                "%(bus_passwd)s, "
                "%(prof_url)s);"
            )

    # Execute query with provided values
    cursor.execute(
        query,
        {
            "bus_name": bus_name,
            "bus_email": bus_email,
            "bus_passwd": bus_passwd,
            "prof_url": prof_url
        }
    )

def getPasswdHash(cursor, user_email):

    query = (
        "SELECT PASSWD_HASH "
        "FROM CUSTOMER "
        "WHERE EMAIL=%(user_email)s"
    )

    cursor.execute(
        query,
        {"user_email": user_email}
    )

    for (PASSWD_HASH) in cursor:
        return PASSWD_HASH[0]

def getBusinessPasswdHash(cursor, bus_email):

    query = (
        "SELECT PASSWD_HASH "
        "FROM BUSINESS "
        "WHERE EMAIL=%(bus_email)s"
    )

    cursor.execute(
        query,
        {"bus_email": bus_email}
    )

    for (PASSWD_HASH) in cursor:
        return PASSWD_HASH[0]


def getUserName(user_email):

    cnx, cursor = createDatabaseConnection()

    query = (
        "SELECT * "
        "FROM CUSTOMER "
        "WHERE EMAIL=%(user_email)s"
    )

    cursor.execute(
        query,
        {"user_email": user_email}
    )

    for (NAME) in cursor:
        return NAME[0]

    cursor.close()
    cnx.close()

def getBusinessName(email):

    cnx, cursor = createDatabaseConnection()

    query = (
        "SELECT * "
        "FROM BUSINESS "
        "WHERE EMAIL=%(email)s"
    )

    cursor.execute(
        query,
        {"email": email}
    )

    for (NAME) in cursor:
        return NAME[0]

    cursor.close()
    cnx.close()

def getBusinessURL(email):

    cnx, cursor = createDatabaseConnection()

    query = (
        "SELECT PROFILE_URL "
        "FROM BUSINESS "
        "WHERE EMAIL=%(email)s"
    )

    cursor.execute(
        query,
        {"email": email}
    )

    for (NAME) in cursor:
        return NAME[0]

    cursor.close()
    cnx.close()


def queryForPosts(cursor):

    query = (
        "SELECT * "
        "FROM POST"
    )

    cursor.execute(query)
