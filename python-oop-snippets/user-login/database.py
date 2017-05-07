
from user import *

class Database:
		# TODO: add regex rules hash to use in main.get_data() (makes sense to put it here)
		def __init__(self):
				self.users = []
				self.entries = 0
				self.password_hashes = {} # Authentication for login

		def add_user(self, user):
				self.users.append(user)
				self.entries += 1

		# Possible usage for autocompletion based on logging in (come back to this)
		def get_users(self):
				return [user.get_username() for user in self.users]