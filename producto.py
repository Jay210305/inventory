class Product:
    def __init__(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, code={self.code}, price={self.price}, quantity={self.quantity})"

class ProductList:
    def __init__(self):
        self.products = []

    def add_product(self, name, code, price, quantity):
        product = Product(name, code, price, quantity)
        self.products.append(product)

    def delete_product(self, code):
        for product in self.products:
            if product.code == code:
                self.products.remove(product)
                break

    def modify_product(self, code, name=None, price=None, quantity=None):
        for product in self.products:
            if product.code == code:
                if name:
                    product.name = name
                if price:
                    product.price = price
                if quantity:
                    product.quantity = quantity
                break

    def show_products(self):
        for product in self.products:
            print(product)


# Create a ProductList object
product_list = ProductList()

name=str(input())
code=str(input())
price=float(input())
quantity=int(input())
product_list.add_product(name, code, price, quantity)

# Add some products to the list
product_list.add_product("Apple", "APL001", 0.99, 100)
product_list.add_product("Banana", "BNN001", 1.50, 50)
product_list.add_product("Orange", "ORN001", 0.75, 75)

# Show all products on the screen
product_list.show_products()

# Modify a product's name and quantity
product_list.modify_product("BNN001", name="Organic Banana", quantity=25)

# Show all products on the screen again
product_list.show_products()

# Delete a product from the list
product_list.delete_product("ORN001")

# Show all products on the screen one more time
product_list.show_products()



