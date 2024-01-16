class Vehicle:

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def display_info(self):
    return f"Brand: {self.brand}, Model: {self.model}"

class Truck(Vehicle):

  def __init__(self, brand, model, load_capacity):
    super().__init__(brand, model)
    self.load_capacity = load_capacity

  def display_info(self):
    return f"Brand: {self.brand}, Model: {self.model}, Load Capacity: {self.load_capacity}"

Ferrari = Vehicle("Ferrari", "F40")
print(Ferrari.display_info())

truc = Truck("Ford", "F-150", "5 tonnes")
print(truc.display_info())
