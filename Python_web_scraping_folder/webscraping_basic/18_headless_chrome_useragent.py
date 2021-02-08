
from selenium import webdriver


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url =  