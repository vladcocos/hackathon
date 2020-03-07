import utils
import time


class VendingMachine:

    def __init__(self):
        self.available_bills = {bill: 5 for bill in [5, 10, 20, 50, 100]}
        self.ongoing_payment = False
        self.selected_product = ''
        self.payment_method = None

    # def add_product(self, product_name, product_price):
        # self.available_products[product_name] = product_price

    # def add_products(self, products):
        # for product in products:
            # self.add_product(product[0], product[1])

    def choose_product(self, product):
        self.selected_product = product

    def choose_payment_method(self, payment_method):
        if payment_method == 'Cash' or payment_method == 'Card':
            self.payment_method = payment_method

    def pay(self):
        if self.payment_method == 'Cash':
            self._pay_with_cash()
        elif self.payment_method == 'Card':
            self._pay_with_card()

    def _pay_with_cash(self):
        current_sum = 0
        product_name = self.selected_product
        product_price = utils.available_products_prices[product_name]
        change = False

        while current_sum < product_price:
            print('You inserted %d$. You need to insert %d$ more.' % (current_sum, product_price - current_sum))
            user_input = input('Insert a bill: ')

            if user_input.lower() == 'c' or user_input.lower() == 'cancel':
                print('You canceled the transaction.')
                return False

            inserted_bill = int(user_input)
            if not inserted_bill in self.available_bills.keys():
                print('You inserted a wrong bill. Try again.')
                continue

            current_sum += inserted_bill
            self.available_bills[inserted_bill] += 1

        if current_sum > product_price:
            change = True

        print('Please wait...')
        time.sleep(1)

        if change:
            self._give_change(current_sum - product_price)

        print('Payment successful. Pick up your product from the vending machine tray. Thank you for your purchase.')
        utils.available_products_stock[product_name] -= 1
        return True

    def _give_change(self, change):
        print('Giving %d$ change' % change)
        print('Please wait...')
        time.sleep(1)

        while change > 0:
            available_bills = [x for x in self.available_bills.keys() if self.available_bills[x] > 0]
            available_bills.sort(reverse=True)
            print(available_bills)
            for bill in available_bills:
                if bill > change:
                    continue
                print('%d$ bill' % bill)
                change -= bill
                self.available_bills[bill] -= 1

    def _pay_with_card(self):
        product_name = self.selected_product
        product_price = utils.available_products_prices[product_name]

        user_input = input('Enter your card. (Write \'card\') ')
        while True:
            if user_input.lower() == 'c' or user_input.lower() == 'cancel':
                print('You canceled the transaction.')
                return False

            if user_input.lower() == 'card':
                self.payment_token = utils.generate_payment_token()
                print('Validating your card. Please wait.')
                time.sleep(1)
                print('Your card was validated. Please wait.')
                time.sleep(1)
                print('Payment successful. Here is your product. Thank you for your purchase.')
                return True
            else:
                print('You entered the wrong card. Please try again.')
