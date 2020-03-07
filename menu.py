from utils import avira_product, avira_product_prices


def print_menu():
    print('\t==== Welcome to Avira Vending Machine! ====\n'
          'Please select one of the products below:')
    for x in avira_product:
        print('\t(' + str(avira_product.index(x) + 1) + ') ' + x + ' - ' + str(avira_product_prices[x]) + '$')
    product_option = input('Please select a product number from the ones above: ')
    print('You choose ' + str(product_option))
    print('Please one of the payment method from the  ones listed below:\n'
          '\t(1) Cash\n'
          '\t(2) Card')
    payment_option = input('Please select a payment method number from the ones above: ')
    print('You choose ' + str(payment_option))


if __name__ == '__main__':
    print_menu()