
from user import *
from database import *

def validate_data(data, regex = None):
		# If no regex is provided, check for non-blank string data
		return(str(data) != '')

def confirm_data(original, verification):
		return original == verification

def get_data(data_type, needs_confirmation = True):
		data = ''
		data_confirmed = False

		data = raw_input(('Please enter a %s: ' % (data_type)))

		if needs_confirmation:
				data_confirmed = confirm_data(data, raw_input('Please confirm this %s: ' % (data_type)))

				while not data_confirmed:
						print('Confirmation failed. Please try again.')
						data_confirmed = confirm_data(data, raw_input('Please confirm this %s: ' % (data_type)))
		return data

def create_new_account():
		username = ''
		password = ''
		password_confirmation = False
		pin_confirmation = False
		pin = -1


		# Ask for a username (TODO: validate on "backend" Database class, regex rules for username)
		username = get_data('username', False)

		# Ask for a password and verify it (TODO: regex rules for password)
		password = get_data('password')

		# Ask for a PIN and verify it (TODO: regex rules for pins)
		pin = get_data('PIN')

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