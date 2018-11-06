# pip install selenium
import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Window size
chrome_options.add_argument("--window-size=900,700")

chrome_driver_path = "/path/to/chromedriver"

# 木崎階段前、加江田、こどものくに、青島
urlList = ["http://www.ii-nami.com/gt-kisakihama", "http://www.ii-nami.com/gt-kisakihd", "http://www.ii-nami.com/gt-aoshimahd", "http://www.ii-nami.com/gt-aoshima"]
drivers = ['','','','']

for index, item in enumerate(urlList):
  drivers[index] = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
  drivers[index].get(item)    

