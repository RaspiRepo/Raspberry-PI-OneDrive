__author__ = 'Mariya'
"""
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
"""

###OCR ********
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '5dc49991cbc14e819c18342cfa54c51c',
}

params = urllib.parse.urlencode({
    # Request parameters
    #'url': "captchac_image.jpg",
    'language': 'unk',
    'detectOrientation ': 'true',
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1.0/ocr?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################


