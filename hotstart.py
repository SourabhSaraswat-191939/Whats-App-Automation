import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.facebook.com")
# driver.find_element_by_id("email").send_keys("Check")
# driver.find_element_by_id("pass").send_keys("Check")
# driver.find_element_by_name("q").send_keys("Selenium")
# button = driver.find_element_by_name("btnK")
# driver.implicitly_wait(5)
# print(button.is_displayed())
# ActionChains(driver).move_to_element(button).click(button).perform()

# driver.find_element_by_name("btnI").send_keys(Keys.RETURN)

# to select any <a> take we have to use link_text with passing string of text in b/w <a> tag. Eg-> <a href="..">Gmail</a>
# driver.find_element_by_link_text("Gmail").click()

# CSS Selector  -> it is the best possible way to locate complex element. As it is fast in all web browsers.
# driver.find_element_by_css_selector("#email").send_keys("Sourabh Saraswat")

# Partial Link Text  ->  When we need to find links by a portion of the text in a Link Text element it contains.
# driver.find_element_by_partial_link_text("Create a").click()

# XPath -> It is designed to allow the navigation of XML documents, with the purpose of selecting individual elements, attributes, or some other part of an XML document for specific processing.
# Syntax ->   Xpath = //tagname[@Attribute='Value']
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[5]/a[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("Sourabh")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("Sourabh")
# driver.find_element(By.CSS_SELECTOR,"#u_4_b_91").send_keys("SOurabh")
driver.find_element_by_name("lastname").send_keys("Saraswat")
# driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/img[1]").click()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome('./chromedriver')
# browser.get("https://stackoverflow.com")
# element = browser.find_element_by_name("q")
# element.send_keys("typing")
# print(element)
# time.sleep(3)
# # browser.close()