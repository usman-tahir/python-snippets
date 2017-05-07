
from user import *
from database import *

def validate_data(data, regex = None):
		# If no regex is provided, check for non-blank string data
		return(str(data) != '')

def confirm_data(original, verification):
		print(original == verification)
		return original == verification

def create_new_account():
		username = ''
		password = ''
		password_confirmation = False
		pin_confirmation = False
		pin = -1


		# Ask for a username (TODO: validate on "backend" Database class, regex rules for username)
		while username == '':
				print('Select a non-blank unsername: ')
				username = raw_input()

		# Ask for a password and verify it (TODO: regex rules for password)
		while password == '':
				print('Select a non-blank password: ')
				password = raw_input()

				while not password_confirmation:
						print('Please verify this password: ')
						password_confirmation = confirm_data(password, raw_input())

		# Ask for a PIN and verify it (TODO: regex rules for pins)
		while pin == -1:
				print('Select a 4-digit PIN: ')
				pin = int(raw_input())

				while not pin_confirmation:
						print('Please verify this PIN: ')
						pin_confirmation = confirm_data(pin, int(raw_input()))

		user = User(username, password, pin)
		return user

if __name__ == '__main__':
		menu = '\n1. Log in\n2. Sign up\n'
		print('Enter a selection: ' + menu)
		choice = int(raw_input())

		if choice == 1:
				pass
		else:
				user = create_new_account()
				print('new user created')