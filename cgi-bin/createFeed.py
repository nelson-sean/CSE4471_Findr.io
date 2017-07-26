#!/usr/bin/env python3

import cgi
import cgitb
import pageCreator
import databaseOps

def main():

    # For debugging
    cgitb.enable()

    pageCreator.printFeedStart("Your Feed")

    cnx, cursor = databaseOps.createDatabaseConnection()

    databaseOps.queryForPosts(cursor)

    for (email, time, text) in cursor:
        pageCreator.printFeedItem(databaseOps.getUserName(email), text)

    print("</div>")
    print("</div>")
    print("</body>")
    print("</html>")

if __name__ == '__main__':
    main()
