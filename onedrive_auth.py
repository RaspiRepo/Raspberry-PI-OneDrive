__author__ = 'RaspiRepo'
import onedrivesdk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Onedrive Access
redirect_uri = "https://login.live.com/oauth20_desktop.srf"
client_secret = "client_secret"
client_id_str = "client_id"


user_name = 'username'
password = 'your password'

client = onedrivesdk.get_default_client(client_id=client_id_str,
                                        scopes=['wl.signin',
                                                'wl.offline_access',
                                                'onedrive.readwrite'])
auth_url = client.auth_provider.get_auth_url(redirect_uri)
driver = webdriver.PhantomJS()  # 'phantomjs')

driver.set_window_size(320,240)
driver.maximize_window()

# chrome_driver = webdriver.Chrome('chromedriver')
# chrome_driver.set_window_size(2, 2)

driver.get(auth_url)
driver.implicitly_wait(8)
driver.get(auth_url)

login_field = driver.find_element_by_name("loginfmt")
login_field.send_keys(user_name)

next_btn = driver.find_element(By.ID, "idSIButton9")
next_btn.click()
time.sleep(2)

psw_field = driver.find_element_by_name("passwd")
psw_field.send_keys(password)


signin_btn = driver.find_element(By.ID, "idSIButton9")
signin_btn.click()
time.sleep(3)
driver.save_screenshot('authrization.png')

idBtn_Accept = driver.find_element(By.ID, "idBtn_Accept")
idBtn_Accept.click()
time.sleep(3)

print(driver.current_url)

# parse URL to get code and close the browser
tokens = driver.current_url.split('=')
driver.quit()

#access allow to execute all onedrive API's
access_code = tokens[1].split('&')[0]

print("access code is here ", access_code)

# authenticate the client
onedrive_conn = client.auth_provider.authenticate(access_code, redirect_uri, client_secret)
returned_item = client.item(drive='me', id='root').children['authrization.png'].upload('./authrization.png')



