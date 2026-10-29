# hw8

import random


class BankAccount:
	# Represent a customer's bank acct

	#initialize acct constructor
	def __init__(self, customer_name):
		self.customer_name = customer_name
		self.account_number = random.randint(10000, 99999)
		self.balance = 0.0
		#deposit function
	def deposit(self, amount):
		if amount <= 0:
			return False
		self.balance += amount
		return True
		#withdraw function

	def withdraw(self, amount):
		if amount <= 0 or amount > self.balance:
			return False
		self.balance -= amount
		return True


def make_deposit(account):
	# ask for amount to deposit
	try:
		amount = float(input("How much would you like to deposit? $"))
		if account.deposit(amount):
			print("Deposit successful.")
		else:
			print("Please enter a positive amount.")
	except ValueError:
		print("Please enter a valid amount.")


def make_withdrawal(account):
	# ask for amount to withdraw
	try:
		amount = float(input("How much would you like to withdraw? $"))
		if account.withdraw(amount):
			print("Withdrawal successful.")
		elif amount > account.balance:
			print("You cannot withdraw more than your current balance.")
		else:
			print("Please enter a positive amount.")
	except ValueError:
		print("Please enter a valid amount.")


def view_account_information(account):
	# display the customer's acct info
	print(f"Name: {account.customer_name}")
	print(f"Account #: {account.account_number}")
	print(f"Balance: ${account.balance:.2f}")


def display_menu():
	print("\nPlease choose an option:")
	print("1. Make a deposit")
	print("2. Make a withdrawal")
	print("3. View account information")
	print("4. Quit")

