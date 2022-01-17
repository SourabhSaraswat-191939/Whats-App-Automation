# import web driver from selenium for automate the WhatsApp message
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import time for waiting  the message to get typed in the message box and to avoid execeptions
import time

# 1.creating an obect to open chrome, 2.And paste the path of chrome driver
driver = webdriver.Chrome('./chromedriver')

# passing the url
driver.get('https://web.whatsapp.com/')

# getting data from user
# name = input('enter the name of user:')
# msg = input('enter your message:')
name = 'Tiwary CSE'
msg = 'Hi'
count =5
# count = int(input("enter the count:"))
input('enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]")

for i in range(count):
    msg_box.send_keys(msg)
    # msg_box.send_keys(Keys.RETURN)
    time.sleep(2)
    # button = driver.find_element_by_class_name('_1E0Oz')
    # button.click()