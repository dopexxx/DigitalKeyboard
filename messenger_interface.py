import sys, os, argparse, re, getpass, time
import numpy as np 

from class_digit_keyboard import typing
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys




class browser(object):

	def __init__(self,gecko_path='//geckodriver', profile_path='/Firefox_Profiles/Jannis'): 
		"""
		Parameters:
		-----------
		DEV      {str} specifiying the serial port (depending on used device)
		PIPE     {str} specifiying the pipeline to use (Mo's per default)

		"""

		self.gecko_path = gecko_path
		self.profile_path = profile_path

		self.profile = webdriver.FirefoxProfile(os.getcwd()+self.profile_path)
		self.browser = webdriver.Firefox(self.profile,executable_path=os.getcwd()+self.gecko_path)



	def login_facebook(self):

		self.browser.get('http://www.facebook.com')

		while True:

			email_field = self.browser.find_element_by_id('email')
			email = str(input("Please enter the emailadress of your account: "))
			email_field.send_keys(email)

			pw_field = self.browser.find_element_by_id('pass')
			pw = str(getpass.getpass("Please enter the password of your account: "))
			pw_field.send_keys(pw)
			pw_field.send_keys(Keys.RETURN)

			# Check whether login succesful
			time.sleep(4)
			try:
				a = self.browser.find_element_by_id('email') 
			except NoSuchElementException:
				break
			print('Password wrong, try again!')
			continue


	def select_friend(self):

		 # Open message field
		message_button = self.browser.find_element_by_id("u_0_d")
		message_button.click()
		write_message_button = self.browser.find_element_by_id("u_0_e")
		write_message_button.click()
		
		# Select friend
		time.sleep(2)
		path = self.browser.find_element_by_class_name('_3l9s')
		path.click()
		time.sleep(1)
		path2 = path.find_element_by_class_name('innerWrap')
		friend_name_box = path2.find_element_by_xpath("//input[@tabindex='0']")
		time.sleep(1)
		self.friend_name = str(input("Please enter the name of the friend you want to message: "))
		friend_name_box.send_keys(self.friend_name)
		time.sleep(2)
		friend_name_box.send_keys(Keys.RETURN)


	def write_message(self):

		# Select text field
		root_textbox = self.browser.find_element_by_class_name('_5rpb')
		root_textbox.click()
		time.sleep(1)
		sub_path = "//div[@role='combobox']"
		#//div[@data-contents='true']//div[@data-block='true']//div[@class='_1mf _1mj']"
		#sub_path += "//span[@data-offset-key='5s5s6-0-0']//span[@data-text='true']"

		path_textbox = root_textbox.find_element_by_xpath(sub_path)
		path_textbox.click()
		time.sleep(2)

		print("Website set up to write a message to", self.friend_name)
		print("Please type your message below: ")
		typer = typing()
		path_textbox.send_keys(typer.OUTPUT)
		time.sleep(1)
		path_textbox.send_keys(Keys.RETURN)

		print("Message successfully sent!")



		    