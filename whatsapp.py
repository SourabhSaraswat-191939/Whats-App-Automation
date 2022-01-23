# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from config import CHROME_PROFILE_PATH

# options = webdriver.ChromeOptions()
# options.add_argument(CHROME_PROFILE_PATH)

# browser = webdriver.Chrome('./chromedriver',options=options)
# browser.get("https://web.whatsapp.com/")
# time.sleep(20)

# # for i in range(12,1,-1):
# #     browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[%d]"%(i)).click()
# #     try:
# #         input = browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]")
# #         input.send_keys("Hi")
# #     except:
# #         continue
# #


# # browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[%d]"%(1)).click()
# # try:
# #     input = browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]")
# #     input.send_keys("*Hi*")
# # except:
# #     pass


# wait = WebDriverWait(browser, 10)
# actions = ActionChains(browser)
# print("Waiting Started")
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ggj6brxn")))
# print("Waiting")
# print("After Sleep Waiting")
# all_names = browser.find_elements(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div")

# visited = set()
# print("Waiting After All Names")
# print(type(all_names))

# print("----")
# print(all_names[0].text)
# print(all_names[1].text)

# # print(all_names)
# all_names.reverse()
# # print(all_names)
# # while all_names:

# print("----")
# print(all_names[0].text)
# print(all_names[1].text)
# while True:
#   print("-----------")
#   print("Loop", len(all_names), len(visited))
#   i = all_names.pop()
#   i.click()
#   if i in visited:
#     print("Already Visited")
#     # print(i.text)
#     continue

#   # actions.move_to_element(i).perform()
#   browser.execute_script("return arguments[0].scrollIntoView(true);", i)
#   time.sleep(2)
#   all_names = all_names + browser.find_elements(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div")
#   visited.add(i)
#   print(i.text)
#   # title = i.find_element(By.XPATH, "div/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]").text
#   # print(title)



#   #   title = i.find_element(By.XPATH,"div/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]").text
#   #   print(title)






















from http import server
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from config import CHROME_PROFILE_PATH
from fileHandling import *
# from firebase import getDataFromDB
from datetime import date, timedelta
# from webdriver_manager.firefox import GeckoDriverManager

# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)
browser = webdriver.Chrome('./chromedriver',options=options)
# serverData = getDataFromDB()
# time.sleep(8)
# if str((date.today()).isoformat())==serverData['valid']:
#     print("\nYour Subscription to the service is expired, please contact to the developer of the application.\n")
#     sys.exit()

browser.get("https://web.whatsapp.com/")

# print(serverData)
# browser.get("https://www.google.com/")
time.sleep(8)


# console.log(el1.style.transform.substring(11,el1.style.transform.length - 3)); \
browser.execute_script("let comp=(el1,el2)=>{ \
                return el1.style.transform.substring(11,el1.style.transform.length - 3) - el2.style.transform.substring(11,el2.style.transform.length - 3)};\
                elSorted=()=>{ \
                    const els=document.getElementsByClassName(\"_3uIPm WYyr1\")[0].children; \
                    return Object.values(els); \
                    }")

browser.execute_script("""window.list = new Object(); \
                    document.getElementById(\"pane-side\").addEventListener(\"scroll\", \
                        ()=>{ \
                            elSorted().forEach(function(item){\
                                const currentKey=item.style.transform.substring(11,item.style.transform.length - 3); \
                                window.list[currentKey]=item;\
                                    }); \
                            console.log(\"working\",window.list); \
                            })""")

# browser.exe   cute_script(serverData['script1'])
# browser.execute_script(serverData['script2'])
time.sleep(3)
browser.execute_script("document.getElementById(\"pane-side\").scroll(0,15);")
# browser.execute_script(serverData['script3'])

elements= []
visited = set()
def func():
    # print("Work")
    try:
        return browser.execute_script("return list;")
    except NameError as e:
        print(">>>>>>>>>>>>>>>>>>>>>")
        print(e)
        print(">>>>>>>>>>>>>>>>>>>>>")

def updateList():
    # print("Work Test")
    unSort_elements = func()
    # print("Work Test Done")
    print(unSort_elements)
    sort_elements = []
    for key,val in unSort_elements.items():
        key = int(key)
        if key in visited:
            continue
        visited.add(key)
        sort_elements.append((key,val))
        sort_elements.sort()
    if sort_elements!=[]:
        elements.extend(sort_elements)

# print(func())
updateList()
# print(elements)
# print(elements[0])
# elements['0'].click()
blockContactList = getBlockContactList()
# blockContactList = []
count=0
msg = getMsg()
sent = set()
print("\n Message Sent Successfully To =>")
for key,chat in elements:
    if key in sent:
        continue
    # print(key)    
    try:
        chat.click()
    except:
        continue
    try:
        if chat.text.split('\n')[0]+'\n' not in blockContactList :
            msgBox = browser.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]")
            msgBox.click()
            # msgBox.send_keys("*Hi*")
            for line in msg.split('\n'):
                ActionChains(browser).send_keys(line).perform()
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
                # ActionChains(browser).send_keys(Keys.RETURN).perform()
            time.sleep(2)        
            print(chat.text.split('\n')[0])
            sent.add(key)
        browser.execute_script("return arguments[0].scrollIntoView(true);", chat)
        # print(key,"LIST")
        
    except:
        pass
    
    count +=1
    elements.extend([])
    # print(count)
    if count==5:
        count=0
        updateList()
        # print("=============")
        # elements.sort()
        # print(elements)

print(elements)

while True:
    pass










# let comp=(el1,el2)=>{
# return el1.getBoundingClientRect().y - el2.getBoundingClientRect().y
# }
# elSorted=()=>{
# const els=document.getElementsByClassName("_3uIPm WYyr1")[0].children
# return Object.values(els).sort(comp)
# }


# document.getElementById("pane-side").addEventListener("scroll",()=>{
#     console.log(elSorted())
# })


