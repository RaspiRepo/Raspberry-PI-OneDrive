# Microsoft OneDrive access for Raspberry PI

Reason for this:
Mostly Raspberry PI connected without monitor (as headless node). To have Microsoft Onedrive storage access for Raspberry PI we need to have UI and sign-in manually to get one time access token.  This script allows RaspberryPI device authenticate itself using Onedrive RESTful service. 

#Steps:
1. Install Selenium python framework and phantomJS web driver.
2. Install Microsoft Onedrive SDK (Python Framework)
2. Download onedrive_auth.py script.
3. Modify Microsoft one drive user name and password.
4. Execute the python script which will authenticate OneDrive service and get the authentication token.
5. Using access token, Onedirve features can be accessed like store/share photo/video/documents etc.

# Things to watch

This process is partly a craking Microsoft OneDrive website (HTML page) and automatically fill userlogin name, passowrd field and invoke login button. Future if Microsoft change these HTML tag names mentioned below need to modify python code according to that.

To find name of these fields open onedrive login page and view HTML source and try to find Email/password text box names and login button name. NOTE: Chrome browser right click on textfield and choose "Inspect"

The following lines need workaround if any changes from microsoft i.e. if authentication failed to get access code

login_field = driver.find_element_by_name("loginfmt")

password_field = driver.find_element_by_name("passwd")

sign_btn = driver.find_element_by_id("idSIButton9")

element = driver.find_element_by_name('ucaccept')

Once access token retrived, same token can be used to access all Onedrive service.

Refernce links to check
https://github.com/onedrive/onedrive-sdk-python  *** This method require user need to allow access permission in the browser.

https://dev.onedrive.com/auth/msa_oauth.htm

**** Register the application and get client ID*** Important step
https://apps.dev.microsoft.com/Disambiguation?ru=https%3a%2f%2fapps.dev.microsoft.com%2f

Copy the Client ID string and secret key from app control panel.

*** Set this below value ****

client_secret = "client_secret"
client_id_str = "client_id_str
