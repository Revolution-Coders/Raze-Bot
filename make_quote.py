from selenium_driver import driver
from fetch_quote import quote,author
import time
import datetime as dt

driver.get('https://quotescover.com/designs/wording?res=UFg2ajdxa2FRQ3hIa0VrZGc5dEE0Zz09')
driver.find_element_by_id("quotes").send_keys(quote)
driver.find_element_by_id("author").send_keys(author)
driver.find_element_by_id("template-contactform-submit").click()

time.sleep(3)

driver.find_element_by_xpath("//div[@class='forDesktop']/div/button[@onclick='openDownload()']").click()

time.sleep(15)

driver.find_element_by_xpath('''//button[@onclick="openNav('jpg')"]''').click()

time.sleep(3)

now = dt.datetime.now()
fileName = "quote_" + now.strftime("%d_%H_%M_%S")
driver.find_element_by_id("fileName").send_keys(fileName)

time.sleep(3)

driver.find_element_by_xpath('''//button[@class=" defaultHidden dlButton-3 button designButton save_image_locally_jpg"]''').click()
