#!/usr/bin/env python3

def printFeedStart(title):

    # Print required response header
    print("Content-type: text/html")
    print()

    page_string = '''
<!DOCTYPE html>
<html>
    <title>{}</title>
'''
    print(page_string.format(title))

    page_string = '''
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins">
    <style>
        body,h1,h2,h3,h4,h5 {font-family: "Poppins", sans-serif}
        body {font-size:16px;}
        .w3-half img{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}
        .w3-half img:hover{opacity:1}
    </style>
    <body>

        <!-- Sidebar/menu -->
        <nav class="w3-sidebar w3-blue w3-collapse w3-top w3-large w3-padding" style="z-index:3;width:300px;font-weight:bold;" id="mySidebar"><br>
          <a href="javascript:void(0)" onclick="w3_close()" class="w3-button w3-hide-large w3-display-topleft" style="width:100%;font-size:22px">Close Menu</a>
          <div class="w3-container">
            <h3 class="w3-padding-64"><b>Findr.io</b></h3>
          </div>
          <div class="w3-bar-block">
            <a href="#" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Feed</a> 
            <a href="#" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Search</a> 
            <a href="#" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Preferences</a> 
            <a href="../login.html" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Logout</a> 
          </div>
        </nav>

        <!-- Overlay effect when opening sidebar on small screens -->
        <div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

        <!-- !PAGE CONTENT! -->
        <div class="w3-main" style="margin-left:340px;margin-right:40px">

          <!-- Feed -->
          <div class="w3-container" id="services" style="margin-top:75px">
            <h1 class="w3-xxxlarge w3-text-dark-grey"><b>Welcome to your feed</b></h1>
            <hr style="width:50px;border:5px solid blue" class="w3-round">
'''
    print(page_string)

def printFeedItem(name, text):

    item_string = '''
            <div class="w3-container w3-grey w3-margin-bottom">
                <h2 class="w3-xxlarge w3-text-dark-grey">{}</h2>
                <p>{}</p>
                <hr style="width:15px;border:2px solid black" class="w3-round">
                <form>
                    <input type="text" name="comment" placeholder="got a comment?" class="w3-margin" style="width:500px;height:50px">
                    <button type="submit" class="w3-button w3-blue">Comment</button>
                </form>
            </div>
'''
    print(item_string.format(name, text))


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
            <form action="../cgi-bin/createFeed.py">
                <button type="submit" class="w3-button w3-blue w3-medium">Go to your feed</button>
            </form>
        </div>
        <footer class="w3-container w3-padding-64 w3-center w3-blue w3-bottom">  
        </footer>
    </body>
</html>
'''
    print(page_string)

def createBusinessSuccessPage(bus_name, prof_url):
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
    print("Welcome {}!".format(bus_name))
    page_string = '''
            <form action="../{}">
                <button type="submit" class="w3-button w3-blue w3-medium">Go to your profile</button>
            </form>
        </div>
        <footer class="w3-container w3-padding-64 w3-center w3-blue w3-bottom">  
        </footer>
    </body>
</html>
'''
    print(page_string.format(prof_url))

def createNewBusinessProfile(bus_name, prof_url):

    # Open new file for writing
    profile = open("/var/www/html/{}".format(prof_url), "w+")

    page_string = '''
<!DOCTYPE html>
<html>
    <title>Profile</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins">
    <style>
        body,h1,h2,h3,h4,h5 {font-family: "Poppins", sans-serif}
        body {font-size:16px;}
        .w3-half img{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}
        .w3-half img:hover{opacity:1}
    </style>
    <body>

        <!-- Sidebar/menu -->
        <nav class="w3-sidebar w3-blue w3-collapse w3-top w3-large w3-padding" style="z-index:3;width:300px;font-weight:bold;" id="mySidebar"><br>
          <a href="javascript:void(0)" onclick="w3_close()" class="w3-button w3-hide-large w3-display-topleft" style="width:100%;font-size:22px">Close Menu</a>
          <div class="w3-container">
            <h3 class="w3-padding-64"><b>Findr.io</b></h3>
          </div>
          <div class="w3-bar-block">
            <a href="#" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Home</a> 
            <a href="#" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Search</a> 
            <a href="#" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Preferences</a> 
            <a href="login.html" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Logout</a> 
          </div>
        </nav>

        <!-- Overlay effect when opening sidebar on small screens -->
        <div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

        <!-- !PAGE CONTENT! -->
        <div class="w3-main" style="margin-left:340px;margin-right:40px">

          <!-- Services -->
          <div class="w3-container" id="services" style="margin-top:75px">
'''
    profile.write(page_string)
    profile.write('<h1 class="w3-xxxlarge w3-text-blue"><b>{}</b></h1>'.format(bus_name))
    page_string = '''
            <hr style="width:50px;border:5px solid blue" class="w3-round">
            <p>Some text about our services - what we do and what we offer. We are lorem ipsum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
            dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor
            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            </p>
          </div>

            <!-- Photo grid (modal) -->
            <div class="w3-row-padding">
                <h1 class="w3-xxxlarge w3-text-blue">Portfolio</h1>
                <hr style="width:50px;border:5px solid blue" class="w3-round">
                <div class="w3-half">
                </div>

                <div class="w3-half">
                </div>
                <button class="w3-button w3-blue w3-margin">Add Photos</button>
            </div>
          

          <!-- Contact -->
          <div class="w3-container" id="contact" style="margin-top:75px">
            <h1 class="w3-xxxlarge w3-text-blue"><b>Contact.</b></h1>
            <hr style="width:50px;border:5px solid blue" class="w3-round">
            <form action="" target="_blank">
              <div class="w3-section">
                <label>Name</label>
                <input class="w3-input w3-border" type="text" name="Name" required>
              </div>
              <div class="w3-section">
                <label>Email</label>
                <input class="w3-input w3-border" type="text" name="Email" required>
              </div>
              <div class="w3-section">
                <label>Message</label>
                <input class="w3-input w3-border" type="text" name="Message" required>
              </div>
              <button type="submit" class="w3-button w3-block w3-padding-large w3-blue w3-margin-bottom">Send Message</button>
            </form>  
          </div>

        <!-- End page content -->
        </div>

        <!-- W3.CSS Container -->
        <div class="w3-light-grey w3-container w3-padding-32" style="margin-top:75px;padding-right:58px"><p class="w3-right">Powered by <a href="https://www.w3schools.com/w3css/default.asp" title="W3.CSS" target="_blank" class="w3-hover-opacity">w3.css</a></p></div>

        <script>
            // Script to open and close sidebar
            function w3_open() {
                document.getElementById("mySidebar").style.display = "block";
                document.getElementById("myOverlay").style.display = "block";
            }
             
            function w3_close() {
                document.getElementById("mySidebar").style.display = "none";
                document.getElementById("myOverlay").style.display = "none";
            }

            // Modal Image Gallery
            function onClick(element) {
              document.getElementById("img01").src = element.src;
              document.getElementById("modal01").style.display = "block";
              var captionText = document.getElementById("caption");
              captionText.innerHTML = element.alt;
            }
        </script>
    </body>
</html>
'''
    profile.write(page_string)
