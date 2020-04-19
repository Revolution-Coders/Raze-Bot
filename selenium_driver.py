from selenium import webdriver
import os


Driverpath = '/usr/bin/chromedriver'
path = os.getcwd()+'/temp_quote/'

options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path}
options.add_experimental_option('prefs', prefs)
options.add_argument("--headless") 

driver = webdriver.Chrome(Driverpath, chrome_options=options)
