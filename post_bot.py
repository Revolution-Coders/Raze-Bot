from instabot import Bot 
from selenium_driver import path
from credentials import usr,psw
from make_quote import fileName
import os


def post():
	bot = Bot()   
	bot.login(username = usr,password = psw) 
	bot.upload_photo(path+fileName+'.jpg', caption ="Test") 
	os.remove(path+fileName+'.jpg.REMOVE_ME')
