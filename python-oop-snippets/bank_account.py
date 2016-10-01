
class BankAccount:
	"""Class for Bank Accounts (Simple)"""

	type = 'Normal Account'

	def __init__(self, name):
		# Default variables unique to each object
		self.name = name
		self.balance = 0.00

	# Methods
	def get_balance(self):
		return(this.balance)

	def deposit(self, amount):
		if (amount < 0):
			print("You entered an invalid amount for depositing.")
			return False
		else:
			self.balance += amount
			return True

	def withdraw(self, amount):
		if self.balance < amount:
			print("You do not have enough money to withdraw $%.2f" % (amount))
			return False
		else:
			self.balance -= amount
			return True

	def get_name(self):
		return(this.name)

	def describe(self):
		return("This bank account belongs to %s and it currently contains $%.2f" % (self.name, self.balance))