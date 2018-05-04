from messenger_interface import browser


if __name__ == '__main__':

	b = browser()
	b.login_facebook()
	b.select_friend()
	b.write_message()




