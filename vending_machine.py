import utils
import time


class VendingMachine:

    def __init__(self):
        self.available_bills = {bill: 5 for bill in [5, 10, 20, 50, 100]}
        self.ongoing_payment = False
        self.selected_product = ''
        self.payment_method = None

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

            if utils.check_cancel(user_input):
                return False

            inserted_bill = int(user_input)
            if not inserted_bill in self.available_bills.keys():
                print('You inserted a wrong bill. Try again.')
                continue

            current_sum += inserted_bill
            self.available_bills[inserted_bill] += 1

        if current_sum > product_price:
            change = True

        print(utils.WAIT)
        time.sleep(1)

        if change:
            self._give_change(current_sum - product_price)

        print(utils.SUCCESSFUL_PAYMENT)
        utils.available_products_stock[product_name] -= 1
        return True

    def _give_change(self, change):
        print('Giving %d$ change' % change)
        print(utils.WAIT)
        time.sleep(1)

        while change > 0:
            available_bills = [x for x in self.available_bills.keys() if self.available_bills[x] > 0]
            available_bills.sort(reverse=True)
            for bill in available_bills:
                if bill > change:
                    continue
                print('%d$ bill' % bill)
                change -= bill
                self.available_bills[bill] -= 1

    def _pay_with_card(self):
        product_name = self.selected_product
        product_price = utils.available_products_prices[product_name]

        print('Enter your card details.')
        while True:
            user_input = input('Enter your card number: ')
            if utils.check_cancel(user_input):
                return False

            if not utils.verify_card_number(user_input):
                print('You entered an invalid card number. Try again.')
                continue

            card_number = user_input
            break

        while True:
            user_input = input('Enter your card expiration date (format mm/yy): ')
            if utils.check_cancel(user_input):
                return False

            if not utils.verify_card_expiration_date(user_input):
                print('You entered an invalid expiration date. Try again.')
                continue

            break

        while True:
            user_input = input('Enter your card security code (CVC): ')
            if utils.check_cancel(user_input):
                return False

            if not utils.is_input_number(user_input) or len(user_input) != 3:
                print('You entered an invalid security code (CVC). Try again.')
                continue

            cvc = user_input
            break

        # self.payment_token = utils.generate_payment_token()
        print('Validating your card. Please wait...')
        time.sleep(1)
        print('Your card was validated. Please wait...')
        time.sleep(1)
        print(utils.SUCCESSFUL_PAYMENT)
        return True
