from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import pyautogui
import datetime
import re
from time import *
from config import CHROME_PROFILE_PATH

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
st = time()


def eta(seconds):
    sec = seconds - st
    return "ETA: " + str(datetime.timedelta(seconds=sec))

def scroll():
    for i in range(8):
        pyautogui.press('down')
        print("run")
        sleep(1)

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

driver = webdriver.Chrome('./chromedriver',options=options)
driver.get("https://web.whatsapp.com/")
sleep(13)
chats = []
print("Chrome has been automated", eta(time()))


mycon=set()
driver.find_element(By.CLASS_NAME,"_3uIPm").click()
while(True):
    # scroll()
    print("run")
    contacts = driver.find_elements_by_css_selector('._3q9s6 span')
    newcon=set([j.text for j in contacts])
    if len(newcon|mycon)==len(mycon):
        break
    else:
        mycon=newcon|mycon
    sleep(3)
contact=sorted(list(mycon),key=str.casefold)
rotate=dict()
print(len(contact),"contacts has been retrieved",eta(time()))

print(contact)