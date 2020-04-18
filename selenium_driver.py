from selenium import webdriver


options = webdriver.ChromeOptions()
path = '/home/tr4cer/Raze bot/temp_quote/'
prefs = {'download.default_directory' : path}
options.add_experimental_option('prefs', prefs)
options.add_argument("--headless") 
driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)
