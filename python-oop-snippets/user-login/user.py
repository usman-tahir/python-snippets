
class User:
		def __init__(self, username, password, pin):
				self.username = username
				self.password = password
				self.pin = pin

				'''
						User Privileges
						0 - Standard User
						1 - Administrator
						2 - System Administrator
						3 - Super/Root User
				'''
				self.privileges = 0
				
		def get_username(self):
				return self.username

		def set_username(self, new_username):
				self.username = new_username if new_username != '' else self.username

		def get_pin(self):
				return self.pin

		def set_pin(self, new_pin):
				self.pin = new_pin if len(str(new_pin)) == 4 else self.pin