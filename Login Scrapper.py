import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install())

urlLogin = "https://www.amazon.com/ap/signin?clientContext=131-0211287-5980619&openid.return_to=https%3A%2F%2Fwww.audible.com%2F&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=audible_shared_web_us&openid.mode=checkid_setup&marketPlaceId=AF2M0KC94RCEA&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_audible_bc_us&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"


driver.get(urlLogin)
time.sleep(2)
driver.find_element_by_xpath("""//*[@id="ap_email"]""").send_keys('sample@test.com')#login id
driver.find_element_by_xpath("""//*[@id="ap_password"]""").send_keys('sample password')# password
time.sleep(2)
driver.find_element_by_xpath("""//*[@id="signInSubmit"]""").click()
