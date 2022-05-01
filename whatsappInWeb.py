from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import requests, os, time
currentPath = os.getcwd()
CHROMEDRIVER_PATH = f"{currentPath}/chromedriver" # Chrome Driver Path
CHROME_PATH = ""
# WINDOW_SIZE = "1280,800" # Screen Size
WINDOW_SIZE = "800,600" # Screen Size
chrome_options = Options()
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.add_argument("--headless")
chrome_options.binary_location = CHROME_PATH
CHROME_PATH
prefs = {'profile.managed_default_content_settings.images' : 1}
chrome_options.add_experimental_option("prefs", prefs)
# #url = "https://autoportal.com/newcars/car-finder/page/1/price/1/"
chrome_options
driver = webdriver.Chrome(
executable_path = CHROMEDRIVER_PATH,
    chrome_options = chrome_options
) # Initiate browser
# #PHANTOMDRIVER_PATH = "/Users/Abhinav/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs"
# #driver = webdriver.PhantomJS(PHANTOMDRIVER_PATH, service_args=["--load-images=no"])
# #driver.set_window_size(1280, 800)
# unused_links = []
# used_links = []
def check_exists_by_xpath(xpath): # Checking whether xpath is available
    
    try:

        driver.find_element_by_xpath(xpath)

    except:
        return False
    return True
# #//*[@id="content"]/div[2]/div[6]/div[2]/div[4]/div[1]/div[1]/div/div[2]/div[1]/div[1]/p/a


# status=True # Status of 
# count = 1
            
# #getting latest details from site
# while status:
url = "https://web.whatsapp.com"
#     request = requests.get(url) # checking whether url exists
#     if request.status_code == 200: # if  status of url is 200 then it will proceed.
driver.get(url)

# qrXpath = "/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div/canvas"

time.sleep(60)
driver.close()