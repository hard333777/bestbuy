class Product:

    def validate_name(name: str):

        """Validates name of product"""

        try:
            if False in [i.isalnum() for i in name.split()] or name.isspace() or len(name) == 0:
                raise Exception('Only literals and numbers are allowed.')
            return name
        except AttributeError:
            print('Only literals and numbers are allowed.')
        except Exception as e:
            print(f"Such error occurred: {e}")


    def validate_price(price: float):

        """Validates price of product"""

        try:
            if not str(price).isdigit():
                raise Exception('Only positive integers are allowed.')
            return price
        except Exception as e:
            print(f"Such error occurred: {e}")


    def validate_quantity(quantity: int):

        """Validates quantity of product"""

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

        """Returns quantity of product"""

        return self.quantity


    def set_quantity(self, quantity):

        """Sets quantity of product"""

        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self) -> bool:

        """Checks if product is active"""

        return self.active


    def activate(self):

        """Activates product"""

        self.active = True


    def deactivate(self):

        """Deactivates product"""

        self.active = False


    def show(self):

        """Prints full info of product"""

        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def validate_quantity_in_stock(self, quantity):

        """Validates if it is enough of product in stock"""

        try:
            if self.quantity - quantity < 0:
                raise Exception(f"Oops! There are only {self.quantity} of the {self.name} left.")
            return True
        except Exception as e:
            print(f"Such error occurred: {e}")


    def buy(self, quantity) -> float:

        """
        According to entered quantity decreases the quantity of the product.
        Returns the price of the bought product.
        """

        if self.validate_quantity_in_stock(quantity):
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
            return quantity * self.price
