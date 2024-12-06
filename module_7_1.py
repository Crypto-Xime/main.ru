                                    # Task "Accounting for goods":

from pprint import pprint

# Define the file name
names = "products.txt.py"

class Product:
    def __init__(self, name, price, type_of_product, customer):
        self.name = name
        self.price = price
        self.type_of_product = type_of_product
        self.customer = customer

    # String representation of the product
    def __str__(self):
        return f"{self.name}, {self.price}, {self.type_of_product}, Customer: {self.customer}"

class Shop:
    def __init__(self):
        self.__file_name = names  # File name where products are stored

    def get_products(self):
        try:
            # Execute the content of the file to create the products
            with open(self.__file_name, "r") as file:
                exec(file.read())  # This will define p1, p2, etc.

            # Return a list of the products (you will have p1, p2, etc. after exec)
            return [p1, p2, p3, p4, p5]
        except FileNotFoundError:
            print(f"File {self.__file_name} not found.")
            return []

    def add(self, *products):
        current_products = self.get_products()
        existing_names = {product.name for product in current_products}

        with open(self.__file_name, "a") as file:
            for product in products:
                if product.name in existing_names:
                    print(f"Product {product.name} is already in the store")
                else:
                    file.write(f"{str(product)}\n")  # Writing the new product to the file
                    existing_names.add(product.name)


# Example Usage
s1 = Shop()

# Add some product objects manually or get from the file
p1 = Product("Tomato", 5.50, "Vegetables", "Alice")
p2 = Product("Spaghetti", 4.40, "Carbohydrates", "Bob")
p3 = Product("Potato", 6.50, "Vegetables", "Charlie")
p4 = Product("Meat", 7.80, "Protein", "Dave")
p5 = Product("Strawberry", 9.53, "Fruits", "Eve")

# Add products to the shop
s1.add(p1, p2, p3, p4, p5)

# Show product details as formatted string
pprint([str(product) for product in s1.get_products()])

# Show all products in the shop
print("\nProducts in the shop:")
print("\n".join(str(product) for product in s1.get_products()))
