import utils
from vending_machine import *


def print_menu():
    vending_machine = VendingMachine()

    print('\t==== Welcome to Avira Vending Machine! ====')
    print('\t==== Press \'c\' or write \'cancel\' at any time to cancel. ====\n')

    while True:
        print('Please select one of the products below:')
        for x in utils.available_products_list:
            current_product = '\t(' \
                    + str(utils.available_products_list.index(x) + 1) \
                    + ') ' \
                    + x \
                    + ' - ' \
                    + str(utils.available_products_prices[x]) \
                    + '$';
            if utils.available_products_stock[x] == 0:
                current_product += ' (Out of stock)'
            print(current_product)

        product_option = input('Please select a product number from the ones above: ')

        if product_option.lower() == 'c' or product_option.lower() == 'cancel':
            print('You canceled the transaction.')
            return False

        if not utils.is_input_number(product_option):
            print('You entered a wrong input. Please try again.')
            continue

        product_option = int(product_option) - 1
        if not product_option in range(len(utils.available_products_list)):
            print('You entered a wrong number. Please try again.')
            continue

        if not utils.check_stock(utils.available_products_list[product_option]):
            print('Sorry, but the product you chose is not available anymore. Please try another.')
            continue

        print('\nYou chose ' + utils.available_products_list[product_option])
        print('-' * 30 + '\n')
        vending_machine.choose_product(utils.available_products_list[product_option])
        break

    while True:
        print('Please select a payment method from the ones listed below:')
        for i in range(len(utils.payment_methods)):
            print('\t(%d) %s' % (i + 1, utils.payment_methods[i]))
        payment_method = input('Please select a payment method number from the ones above: ')

        if payment_method.lower() == 'c' or payment_method.lower() == 'cancel':
            print('You canceled the transaction.')
            return False

        if payment_method != '' and not int(payment_method) in range(1, len(utils.payment_methods)):
            print('You entered a wrong input. Please try again.')
            continue

        if payment_method == '':
            payment_method = '1'

        # payment_methods = [x.split(' ')[0] for x in utils.payment_methods]

        payment_method = utils.payment_methods[int(payment_method) - 1].split(' ')[0]
        print('You chose to pay with ' + payment_method.lower())
        print('-' * 30 + '\n')
        vending_machine.choose_payment_method(payment_method)
        break

    payment_result = vending_machine.pay()

if __name__ == '__main__':
    print_menu()