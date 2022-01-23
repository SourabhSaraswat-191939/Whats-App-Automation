import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from config import CHROME_PROFILE_PATH

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

driver = webdriver.Chrome('./chromedriver',options=options)
# driver.get("https://web.whatsapp.com/")
driver.get("https://www.google.com/")
time.sleep(4)

action = ActionChains(driver)
source = driver.find_element(By.XPATH,"//input[@type='text']")
print(source)
action.move_to_element_with_offset(source,1,10)
action.context_click(source).perform()