class Product:
  def __init__(self,name,price,quantity) :
      self.name=name
      self.price = price
      self.quantity =quantity

  def __str__(self):
      return f"{self.name},{self.price},{self.quantity}"

#apple = Product("Apple",430,1)
arr = []
def product_registration(arr):
  name = input("Enter the name of the product: ")
  price = float(input("Enter the price of product "))
  quantity = int(input("Enter the quantity of product "))
  new_product = Product(name,price,quantity)
  arr.append(new_product)
  return new_product

apple = product_registration(arr)
bannan = product_registration(arr)
for i in range(len(arr)):
  print(arr[i])
