# OneDrive access for RaspberryPi using Python

Getting One Drive access token using python without Web Browser UI on headless node like Raspberry PI.

Install Selenium python framework and phontomJS web driver to automate Onedrive authentication process without involve user or web browser UI.

This allow any IoT devices like Raspberry PI to authenticate itself with OneDrive storage and do any other automated process like take photos and upload, sharing photo albums once picture upload done or file back backup service.

Drawback of this code is dependency with Onedrive login page (website) HTML fields like where user enter email address, passowrd and login button names. Future if Microsoft change these HTML tag names this python code wont work.  Need to find exact field name again to workaround this issue.

To find name of these fields open one drive login page and view HTML source and try to find Email/password text box names and login button name. 

