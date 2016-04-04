__author__ = 'Mariya'
import onedrivesdk
from selenium import webdriver

#Onedrive Access
redirect_uri = "https://login.live.com/oauth20_desktop.srf"
client_secret = "client_secret"
client_id_str = "client_id_str"


user_name = 'user_name@example.com'
password = 'password'

client = onedrivesdk.get_default_client(client_id=client_id_str,
                                        scopes=['wl.signin',
                                                'wl.offline_access',
                                                'onedrive.readwrite'])
auth_url = client.auth_provider.get_auth_url(redirect_uri)
driver = webdriver.PhantomJS()  # 'phantomjs')


#driver = webdriver.Chrome('chromedriver')
#driver.set_window_size(1, 1)


driver.get(auth_url)
driver.implicitly_wait(15)

login_field = driver.find_element_by_name("loginfmt")
password_field = driver.find_element_by_name("passwd")
sign_btn = driver.find_element_by_id("idSIButton9")


# Fill user name and password
login_field.send_keys(user_name)
password_field.send_keys(password)
sign_btn.click()
element = driver.find_element_by_name('ucaccept')
element.click()

# parse URL to get code and close the browser
tokens = driver.current_url.split('=')
driver.quit()

#access allow to execute all onedrive API's
access_code = tokens[1].split('&')[0]

print("access code is here ", access_code)

