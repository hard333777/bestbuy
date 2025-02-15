class Product:

    def validate_name(name: str):
        try:
            if False in [i.isalnum() for i in name.split()] or name.isspace() or len(name) == 0:
                raise Exception('Only literals and numbers are allowed.')
            return name
        except AttributeError:
            print('Only literals and numbers are allowed.')
        except Exception as e:
            print(f"Such error occurred: {e}")


    def validate_price(price: float):
        try:
            if not str(price).isdigit():
                raise Exception('Only positive integers are allowed.')
            return price
        except Exception as e:
            print(f"Such error occurred: {e}")


    def validate_quantity(quantity: int):
        try:
            if not str(quantity).isdigit():
                raise Exception('Only positive integers are allowed.')
            return quantity
        except Exception as e:
            print(f"Such error occurred: {e}")


    def __init__(self, name, price, quantity):
        self.name = Product.validate_name(name)
        self.price = Product.validate_price(price)
        self.quantity = Product.validate_quantity(quantity)
        self.active = True


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def validate_quantity_in_stock(self, quantity):
        try:
            if self.quantity - quantity < 0:
                raise Exception(f"Oops! There are only {self.quantity} of the {self.name} left.")
            return True
        except Exception as e:
            print(f"Such error occurred: {e}")


    def buy(self, quantity) -> float:
        if self.validate_quantity_in_stock(quantity):
            self.quantity -= quantity
            if self.quantity == 0:
                self.active = False
            return quantity * self.price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
if __name__ == '__main__':
    main()


