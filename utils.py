import random

available_products_list = ['Avira Prime', 'Antivirus PRO', 'Phantom VPN', 'Password Manager', 'Optimizer', 'System Speedup']

available_products_prices = {
						'Avira Prime' : 75,
						'Antivirus PRO' : 35,
						'Phantom VPN' : 50, 
						'Password Manager' : 20,
						'Optimizer' : 10,
						'System Speedup' : 25}

available_products_stock = {
						'Avira Prime' : 5,
						'Antivirus PRO' : 5,
						'Phantom VPN' : 5,
						'Password Manager' : 5,
						'Optimizer' : 0,
						'System Speedup' : 5}

payment_methods = ['Cash (default)', 'Card']


def check_stock(selected_product):
	if available_products_stock[selected_product] > 0:
		return True
	return False


def is_input_number(input):
	if input == '':
		return False
	for letter in input:
		if not letter.isdigit():
			return False
	return True


def generate_payment_token():
	lowercase_letters = ''.join([chr(letter) for letter in range(ord('a'), ord('z') + 1)])
	uppercase_letters = lowercase_letters.upper()
	digits = ''.join([chr(digit) for digit in range(ord('0'), ord('9') + 1)])
	characters = lowercase_letters + uppercase_letters + digits
	result = ''
	for _ in range(25):
		result += random.choice(characters)
	return generate_payment_token
