class Product:

  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def __str__(self):
    return f"{self.name},{self.price},{self.quantity}"


class Cart:

  def __init__(self, name):
    self.name = name

  products_list = []

  def add_to_cart(self, product, products_list):
    products_list.append(product)

  def remove_from_cart(self, product, products_list):
    products_list.remove(product)

  def display_cart(self, products_list):
    for product in range(len(products_list)):
      print(products_list[product])


Apple = Product("Apple", 1, 10)
Banana = Product("Banana", 2, 10)
Kiwi = Product("Kiwi", 3, 10)
anil = Cart("anil")
anil.add_to_cart(Apple, anil.products_list)
anil.add_to_cart(Banana, anil.products_list)
anil.add_to_cart(Kiwi, anil.products_list)
anil.display_cart(anil.products_list)
anil.remove_from_cart(Banana, anil.products_list)
anil.display_cart(anil.products_list)