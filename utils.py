import random
import os

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

SUCCESSFUL_PAYMENT = 'Payment successful. Pick up your product from the vending machine tray. Thank you for your purchase.'
WAIT = 'Please wait...'

cards = ['5273467758367213']

log_file_name = 'vending_machine.log'


def check_cancel(user_input):
	if user_input.lower() == 'c' or user_input.lower() == 'cancel':
		print('You canceled the transaction.')
		return True
	return False


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


def verify_card_number(card_number):
	if not is_input_number(card_number) or len(card_number) != 16:
		return False

	aux = [int(digit) for digit in card_number]
	total_sum = 0
	for i in range(0, len(aux)):
		if i % 2 == 0:
			aux[i] *= 2
			if aux[i] / 10 != 0:
				aux[i] = int(aux[i] / 10 + aux[i] % 10)
		total_sum += aux[i]
	return total_sum % 10 == 0


def verify_card_expiration_date(card_expiration_date):
	if len(card_expiration_date.split('/')) != 2:
		return False

	month = card_expiration_date.split('/')[0]
	year = card_expiration_date.split('/')[1]
	months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

	if not month in months or not is_input_number(year) or not int(year) in [x for x in range(20, 30)]:
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


def log(timestamp, product_name, product_price, payment_type, transaction_status):
	f = None
	if os.path.isfile(log_file_name):
		f = open(log_file_name, "a+")
	else:
		f = open(log_file_name, "w+")
		f.write('Log format: Timestamp-Product Name-Product Price ($)-Payment Type-Transaction Status\n')

	if f is not None:
		f.write('{}-{}-{}$-{}-{}\n'.format(timestamp, product_name, product_price, payment_type, transaction_status))
		f.close()
