import sys, os, argparse, re, getpass, time
import numpy as np 

#from class_digit_keyboard import typing
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys




geckoP = '//geckodriver'
browser = webdriver.Firefox(executable_path=os.getcwd()+geckoP)

browser.get('http://www.messenger.com')

while True:

	t = browser.find_element_by_id('email')
	email = str(input("Please enter the emailadress of your account: "))
	t.send_keys(email)
	t = browser.find_element_by_id('pass')
	pw = str(getpass.getpass("Please enter the password of your account: "))
	t.send_keys(pw)
	t.send_keys(Keys.RETURN)

	# Check whether login succesful
	time.sleep(5)
	try:
		a = browser.find_element_by_id('email') 
	except NoSuchElementException:
		break
	print('Password wrong, try again!')
	continue

search_mask = browser.find_elements_by_class_name('_58ak')
#search_mask = browser.find_elements_by_class_name('_58al')
friend_name = str(input("Please enter the name of the friend you want to write: "))
search_mask.send_keys(friend_name)
time.sleep(3)

text_field = browser.find_elements_by_class_name('_1mf _1mj')
text = str(input("Please enter the message to your friend: "))

text_field.send_keys(text)

	