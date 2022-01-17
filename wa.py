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
time.sleep(8)

# count=11
# while True: 
#     element = browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div["+str(count)+"]/div[1]/div[1]/div[2]")
#     # query = "div[style='z-index:269']"
#     # element = browser.find_element_by_css_selector(query)
#     element.click()
#     try:
#         msgBox = browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]")
#         msgBox.click()
#         msgBox.send_keys("**Hi**")
#     except:
#         pass
#     time.sleep(2)
    
#     browser.execute_script("return arguments[0].scrollIntoView(true);", element)
#     count-=1
#     if count==1:
#         count=11
#     # if count==11:
#     #     count=1
#     # if count==279:
#     #     count = 261


# body.web.dark:nth-child(2) div._1ADa8._3Nsgw.app-wrapper-web.font-fix.os-mac:nth-child(1) div._1XkO3.two:nth-child(6) div.ldL67._2i3T7._191H_:nth-child(3) div._1KDb8 div._3Bc7H._20c87 div._3uIPm.WYyr1 div._3m_Xw:nth-child(11) div:nth-child(1) div._2nY6U.vq6sj > div._3OvU8
# 279 262


browser.execute_script("let comp=(el1,el2)=>{return el1.getBoundingClientRect().y - el2.getBoundingClientRect().y}")
browser.execute_script("elSorted=()=>{const els=document.getElementsByClassName(\"_3uIPm WYyr1\")[0].childrenreturn Object.values(els).sort(comp)}")
browser.execute_script("document.getElementById(\"pane-side\").addEventListener(\"scroll\",()=>{console.log(elSorted())})")

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


