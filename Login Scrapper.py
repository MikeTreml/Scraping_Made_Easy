import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install())

urlLogin = "https://www.amazon.com"


driver.get(urlLogin)
time.sleep(2)
driver.find_element_by_xpath("""//*[@id="username"]""").send_keys('')
driver.find_element_by_xpath("""//*[@id="password"]""").send_keys('')
time.sleep(2)
driver.find_element_by_xpath("""//*[@id="modalLogin"]/div/div/div[2]/form/button""").click()
