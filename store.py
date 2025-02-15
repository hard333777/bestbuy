from products import Product

class Store:

    def validate_products(store_products):
        try:
            if not isinstance(store_products, list):
                raise Exception('Products must be a list')
            for product in store_products:
                if not isinstance(product, Product):
                    raise Exception('Wrong format of the product. Only Product type is allowed.')
            return store_products
        except Exception as e:
            print(f"Such error occurred: {e}")

    def __init__(self, store_products: list):
        self.store_products = Store.validate_products(store_products)

    def validate_product(product):
        try:
            if not isinstance(product, Product):
                raise Exception('Only Product type is allowed')
            return product
        except Exception as e:
            print(f"Such error occurred: {e}")


    def add_product(self, product: Product):
        self.store_products.append(Store.validate_product(product))


    def remove_product(self, product: Product):
        if product in self.store_products:
            self.store_products.remove(product)
        else:
            print('There is no such product in the store.')


    def get_total_quantity(self):
        return len(self.store_products)


    def get_all_products(self):
        return [product for product in self.store_products if product.is_active()]

    def validate_shopping_list(shopping_list):
        try:
            if not isinstance(shopping_list, list):
                raise Exception('Invalid format of the shopping list.')
            return shopping_list
        except Exception as e:
            print(f"Such error occurred: {e}")


    def order(self, shopping_list: list):
        shopping_list = Store.validate_shopping_list(shopping_list)
        if shopping_list is None:
            return 'Impossible to make the order.'
        total_price = 0
        for order_item in shopping_list:
            product, quantity = order_item
            item_price = product.buy(quantity)
            if item_price is None:
                return 'Impossible to make the order.'
            total_price += item_price
        return total_price


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                   ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 101), (products[1], 2)]))

if __name__ == '__main__':
    main()


