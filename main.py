from products import Product
from store import Store

def print_menu():

    """Prints the menu"""

    print('''
   Store Menu
   __________

1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
''')


def list_all_products(product_list):

    """Prints full info about entered products"""

    print('_' * 10)
    for number, product in enumerate(product_list, 1):
        print(f"{number}.", end=' '), product.show()


def show_total_amount_in_store(product_list):

    """Prints total quantity of the all products in the store"""

    total_amount = 0
    for product in product_list:
        total_amount += product.quantity
    print(f"Total of {total_amount} items in store")


def get_valid_product_choice():

    """Prompts to choose the product, validates and returns it"""

    while True:
        try:
            product_choice = input('Which product number do you want? ')
            if not product_choice.isdigit() and len(product_choice) != 0:
                raise Exception('Only positive integers or blank line are allowed.')
            if product_choice.isdigit():
                product_choice = int(product_choice)
            return product_choice
        except Exception as e:
            print(f"Such error occurred: {e}")


def get_valid_quantity_choice(product: Product):

    """Prompts to choose the quantity, validates and returns it"""

    while True:
        try:
            quantity_choice = int(input('What amount do you want? '))
            # if not quantity_choice.isdigit() :
            #     raise Exception('Only positive integers are allowed.')
            if product.validate_quantity_in_stock(quantity_choice):
                return quantity_choice
        except ValueError:
            print('Only positive integers are allowed.')
        except Exception as e:
            print(f"Such error occurred: {e}")


def make_an_order(product_list):

    """
    Prompts user to choose the product and amount of the product,
    decreases their quantity in the store and returns total price of the order.
    """

    list_all_products(product_list)
    print('_' * 10)
    print('When you want to finish order, enter empty text.')
    order_list = []
    while True:
        product_choice = get_valid_product_choice()
        if isinstance(product_choice, str):
            break
        product = product_list[product_choice - 1]
        quantity_choice = get_valid_quantity_choice(product)
        try:
            order_list.append((product_list[product_choice - 1], quantity_choice))
            print('Product added to list!\n')
        except IndexError:
            print('Wrong choice, try again.')
    if len(order_list) == 0:
        return
    return Store.order(order_list)


def print_total_price(total_price):

    """
    Prints either total price of the order or error message.
    """

    if total_price is None:
        print("You didn't choose any of product. Order is not made.")
    elif isinstance(total_price, int):
        print('*' * 10)
        print(f"Order made! Total payment: ${total_price}")


def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    valid_inputs = ['1', '2', '3', '4']
    while True:
        products = best_buy.get_all_products()
        print_menu()
        user_action = input('Enter choice (1-4): ')
        while user_action not in valid_inputs:
            print('Invalid choice')
            print_menu()
            user_action = input('Enter choice (1-4): ')
        if user_action == '1':
            list_all_products(products)
        if user_action == '2':
            show_total_amount_in_store(products)
        if user_action == '3':
            total_price = make_an_order(products)
            print_total_price(total_price)
        if user_action == '4':
            print('Bye!')
            break

if __name__ == '__main__':
    main()
