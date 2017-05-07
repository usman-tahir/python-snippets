
from user import *
from database import *

def validate_data(data, regex = None):
		# If no regex is provided, check for non-blank string data
		return(str(data) != '')

def confirm_data(original, verification):
		return original == verification

def validate_username(username, database):
		return username in database.get_users()

def get_data(data_type, database, needs_confirmation = True):
		data = ''
		data_confirmed = False

		data = raw_input(('Please enter a %s: ' % (data_type)))

		if data_type.lower() == 'username':
				# Check to see if the username is already taken (TODO: possible 'similar usernames' functionality)
				username_taken = validate_username(data, database)
				while username_taken:
						print('This username has been taken. Please try again.')
						get_data('username', database, False)

		if needs_confirmation:
				data_confirmed = confirm_data(data, raw_input('Please confirm this %s: ' % (data_type)))

				while not data_confirmed:
						print('Confirmation failed. Please try again.')
						data_confirmed = confirm_data(data, raw_input('Please confirm this %s: ' % (data_type)))
		return data

def create_new_account(database):

		# Ask for a username (TODO: validate on "backend" Database class, regex rules for username)
		username = get_data('username', database, False)

		# Ask for a password and verify it (TODO: regex rules for password)
		password = get_data('password', database)

		# Ask for a PIN and verify it (TODO: regex rules for pins)
		pin = get_data('PIN', database)

		user = User(username, password, pin)
		return user

if __name__ == '__main__':
		user_database = Database()

		menu = '\n1. Log in\n2. Sign up\n3. Quit'
		print('Enter a selection: ' + menu)
		choice = int(raw_input())

		if choice == 1:
				pass
		elif choice == 3:
				print('Goodbye!')
		else:
				user = create_new_account(user_database)
				user_database.add_user(user)