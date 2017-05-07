
class Database:
		def __init__(self):
				self.users = []
				self.entries = 0
				self.password_hashes = {} # Authentication for login

		# Possible usage for autocompletion based on logging in (come back to this)
		def get_users(self):
				output = [user + '\n' for user.get_username() in self.users]
				return output