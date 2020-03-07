class VendingMachine:
    def __init__(self):
        self.available_products = {}
        self.available_bills = {bill: 0 for bill in ['5', '10', '20', '50', '100']}
        self.ongoing_payment = False
        self.selected_product = ''

    def add_product(self, product_name, product_price):
        self.available_products[product_name] = product_price

    def add_products(self, products):
        for product in products:
            self.add_product(product[0], product[1])

    def choose_payment_method(self, payment_method):
        if payment_method == 'Cash' or payment_method == 'Card':
            self.payment_method = payment_method

    def check_stock(self, selected_product):
        if self.available_products[selected_product] > 0:
            self.selected_product = selected_product
            return True
        return False

    def pay_with_cash(self):
        current_sum = 0
        product_name = self.selected_product
        product_price = self.available_products[product_name]
        while current_sum < product_price:
            print('You inserted %d$. You need to insert %d$ more.' % (current_sum, product_price - current_sum))
            inserted_bill = input('Insert a bill')
            if not inserted_bill in self.available_bills.keys():
                print('You inserted a wrong bill. Try again.')
                continue

            inserted_bill = int(inserted_bill)
            current_sum += inserted_bill
            self.available_bills[inserted_bill] += 1

        self.available_products[product_name] -= 1
        return True


