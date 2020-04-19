from selenium_driver import driver
from bs4 import BeautifulSoup
import random as r


quote_list = []
author_list = []

driver.get("https://www.brainyquote.com/quote_of_the_day")

content = driver.page_source
soup = BeautifulSoup(content,features='html.parser')

for i in soup.findAll('div',attrs={'class':'qotd-q-cntr'}):
	temp_quote = i.find('a', attrs={'title':'view quote'})
	temp_author = i.find('a', attrs={'title':'view author'})
	quote_list.append(temp_quote.text)
	author_list.append(temp_author.text)

print(quote_list)
index = r.randint(0,int(len(quote_list)))
quote = quote_list[index]
author = author_list[index]
