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
def createDriverInstance():
    options = webdriver.ChromeOptions()
    options.add_argument(CHROME_PROFILE_PATH)
    return webdriver.Chrome('./chromedriver',options=options)
# serverData = getDataFromDB()
# time.sleep(8)
# if str((date.today()).isoformat())==serverData['valid']:
#     print("\nYour Subscription to the service is expired, please contact to the developer of the application.\n")
#     sys.exit()

browser = createDriverInstance()
browser.get("https://web.whatsapp.com/")

# print(serverData)

time.sleep(8)


# console.log(el1.style.transform.substring(11,el1.style.transform.length - 3)); \
def prepareBrowser():
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
    browser.execute_script("document.getElementById(\"pane-side\").scroll(0,15);")
# browser.execute_script(serverData['script1'])
# browser.execute_script(serverData['script2'])
time.sleep(3)

# browser.execute_script(serverData['script3'])
def getChatList():
    # print("Work")
    try:
        return browser.execute_script("return window.list;")
    except NameError as e:
        print(">>>>>>>>>>>>>>>>>>>>>")
        print(e)
        print(">>>>>>>>>>>>>>>>>>>>>")




def sendMsg():
    elements= []
    
    def updateList():
        # print("Work Test")
        unSort_elements = getChatList()
        # print("Work Test Done")
        # print(unSort_elements)
        sort_elements = []
        visited = set()
        for key,val in unSort_elements.items():
            key = int(key)
            if key in visited:
                continue
            visited.add(key)
            sort_elements.append((key,val))
        sort_elements.sort()
        elements.extend(sort_elements)
        
    updateList()    
    # print(elements)
    count=0
    blockContactList = getBlockContactList()
    msg = getMsg()
    for key,chat in elements:
        # print(key)    
        try:
            chat.click()
        except:
            continue
        try:
            if chat.text.split('\n')[0]+'\n' not in blockContactList:
                msgBox = browser.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]")
                msgBox.click()
                # msgBox.send_keys("*Hi*")

                for line in msg.split('\n'):
                    ActionChains(browser).send_keys(line).perform()
                    ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
                
                    # ActionChains(browser).send_keys(Keys.RETURN).perform()
                # msgBox.send_keys(msg)
                time.sleep(2)        
                print(chat.text.split('\n')[0])
            browser.execute_script("return arguments[0].scrollIntoView(true);", chat)
            # print(key,"LIST")
            
        except:
            pass
        
        count +=1
        # print(count)
        if count==8:
            count=0 
            updateList()
            # print("=============")
            # elements.sort()
            # print(elements)


if __name__=="__main__":
    prepareBrowser()
    
    print("\n Message Sent Successfully To =>")
    sendMsg()

# print(func())
# updateList()
# print(elements)
# print(elements[0])
# elements['0'].click()
# blockContactList = []


# print(elements)

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


