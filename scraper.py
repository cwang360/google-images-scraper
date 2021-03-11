import requests
from bs4 import BeautifulSoup
import urllib.request
import os
from selenium import webdriver
import time


keyword = input("Search for: ")
# Maximum number of images to download
numImages = int(input("Maximum number of images: "))

url = "https://www.google.co.in/search?q="+keyword+"&source=lnms&tbm=isch"

driver = webdriver.Chrome() # Make sure webdriver is in PATH environment variable
driver.get(url)

# Scroll page to load more images
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # Scrolled to end
        break
    last_height = new_height

# get HTML from fully scrolled page
soup = BeautifulSoup(driver.page_source, 'html.parser')

links = []
# Loop through all the img elements in the page source that have the right class
for image in soup.find_all("img", attrs={"class":"rg_i", "src":True}):
    links.append(image["src"]) # Append image link to array

driver.quit()

# Make folder for photos if there isn't one already
try:
    os.mkdir(os.getcwd()+'\\photos\\')
except Exception:
    pass

# download up to numImages # of images from the links array
fileID = 0
for link in links:
    if fileID < numImages:
        print(link)
        urllib.request.urlretrieve(link, os.getcwd()+'\\photos\\'+str(fileID)+".jpg")
        fileID += 1
    else:
        break

