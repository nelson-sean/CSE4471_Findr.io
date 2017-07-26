#!/usr/bin/env python3

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
            <form action="../cgi-bin/login.py" method="post" class="w3-right-align">
                Login:
                <input type="text" name="email" class="w3-margin">
                Password:
                <input type="password" name="password" class="w3-margin">
                <button type="submit" class="w3-button w3-light-grey w3-medium">Login</button>
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


def createSuccessPage(user_name):
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
            <form action="../cgi-bin/login.py" method="post" class="w3-right-align">
                Login:
                <input type="text" name="email" class="w3-margin">
                Password:
                <input type="password" name="password" class="w3-margin">
                <button type="submit" class="w3-button w3-light-grey w3-medium">Login</button>
            </form>
            <h1 class="w3-jumbo" style="margin-top: -10px; margin-bottom: 50px">Findr.io</h1>
        </header>
        <div class="w3-center w3-container w3-jumbo">
'''
    print(page_string)
    print("Welcome {}!".format(user_name))
    page_string = '''
            <form action="../feed.html">
                <button class="w3-button w3-blue w3-medium">Go to your feed</button>
            </form>
        </div>
        <footer class="w3-container w3-padding-64 w3-center w3-blue w3-bottom">  
        </footer>
    </body>
</html>
'''
    print(page_string)
