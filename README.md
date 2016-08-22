# RaspberryPi Getting access Toekn from  Microsoft OneDrive SDK

Reason for this:
Mostly Raspberry PI connected without monitor (as headless node). To have Microsoft Onedrive storage access for Raspberry PI need UI and need to sign-in manually to get one time access token.  This script allows RaspberryPI device authenticate itself using Onedrive RESTful service. 

#Steps:
1. Install Selenium python framework and phontomJS web driver.
2. Install Microsoft Onedrive SDK (Python Framework)
2. Download script.
3. Modify Microsoft one drice user name and password.
4. Excute the python script which will authenticate OneDrive service and get the authentication token.
5. Using access token many Onedirve features can be accessed like store/share photo/video/documents or anything stored into OneDrive. 

#Things to watch

This process is partly a craking Microsoft OneDrive website (HTML page) and automate using login name and passowrd field invoke login button by script. Future if Microsoft change these HTML tag names mentioned below this python code wont work.  Need to find exact field name again.

To find name of these fields open one drive login page and view HTML source and try to find Email/password text box names and login button name. 

The following script need workaround if any changes from microsoft i.e. if authentication failed to get access code

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


