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

browser = webdriver.Chrome('./chromedriver',options=options)
browser.get("https://web.whatsapp.com/")
time.sleep(20)

# for i in range(12,1,-1):
#     browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[%d]"%(i)).click()
#     try:
#         input = browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]")
#         input.send_keys("Hi")
#     except:
#         continue
#


# browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[%d]"%(1)).click()
# try:
#     input = browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]")
#     input.send_keys("*Hi*")
# except:
#     pass


wait = WebDriverWait(browser, 10)
actions = ActionChains(browser)
print("Waiting Started")
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ggj6brxn")))
print("Waiting")
print("After Sleep Waiting")
all_names = browser.find_elements(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div")

visited = set()
print("Waiting After All Names")
print(type(all_names))

print("----")
print(all_names[0].text)
print(all_names[1].text)

# print(all_names)
all_names.reverse()
# print(all_names)
# while all_names:

print("----")
print(all_names[0].text)
print(all_names[1].text)
while True:
  print("-----------")
  print("Loop", len(all_names), len(visited))
  i = all_names.pop()
  i.click()
  if i in visited:
    print("Already Visited")
    # print(i.text)
    continue

  # actions.move_to_element(i).perform()
  browser.execute_script("return arguments[0].scrollIntoView(true);", i)
  time.sleep(2)
  all_names = all_names + browser.find_elements(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div")
  visited.add(i)
  print(i.text)
  # title = i.find_element(By.XPATH, "div/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]").text
  # print(title)



  #   title = i.find_element(By.XPATH,"div/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]").text
  #   print(title)