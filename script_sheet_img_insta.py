# from email.mime import image
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from googleapiclient.discovery import build
# from google.oauth2 import service_account
# from googleapiclient.http import MediaFileUpload
import json

# scope = [
#     "https://spreadsheets.google.com/feeds",
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive",
# ]

# creds = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scope)

# client = gspread.authorize(creds)

# sheet = client.open("Copy of Dos Santos 1-1000 Image Fix - Subhankar Roy").sheet1  # Open the spreadhseet

# links=sheet.col_values(4)
# data=[]
# i=2
# for item in links[1:]:
#     data.append({i:item})
#     i+=1
# with open('modified_json_dump.json','w') as modified_json_file:
#     json.dump(data,modified_json_file,indent=2)

with open('modified_json_dump.json') as json_file:
    data=json.load(json_file)

# for item in data['states']:
#     del item['area_codes']


from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import csv

driver_path = r"C:/chromedriver"
opt = Options()
opt.add_argument("--disable-notifications")
ser = Service(driver_path)
driver = webdriver.Chrome(service=ser, options=opt)

driver.get("https://www.instagram.com/accounts/login/")
sleep(2)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("salehasultana1996")
sleep(2)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("@Sk@As1f@Iqba1@")
sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(5)
# Open a new window
driver.execute_script("window.open('');")
# Switch to the new window 
driver.switch_to.window(driver.window_handles[1])
sleep(5)

new_data=[]
i=2
for item in data:
    try:
        img_link=''
        yt_link=item[f"{i}"]
        driver.get(yt_link)
        sleep(5)
        image=driver.find_elements(By.XPATH,"//img[@class='_aadp']")#private   in public no
        sleep(2)
        if image==[]:
            image=driver.find_elements(By.XPATH,"//img[@class='_aa8j']")[-1]
            sleep(2)
        else:
            image=image[0]
        sleep(3)
        img_link=image.get_attribute('src')   
    except:
        img_link='NA' 
    new_data.append({i:img_link})
    i+=1

with open('new_modified_json_dump.json','w') as modified_json_file:
    json.dump(new_data,modified_json_file,indent=2)
driver.close()





# print()
# url='test_2'
# sheet.update_cell(2,1,url)
# sheet.insert_cols(1,[['name','email']])



