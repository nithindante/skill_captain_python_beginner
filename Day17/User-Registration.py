file = open("C:\\Users\\NithinRajkumar\\Desktop\\skill_captain_python_beginner\\Day17\\input.txt", "w")

class User:

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def __str__(self):
    return f"{self.name},{self.email},{self.password}"


arr = []


def user_registration(arr):
  name = (input("enter the name please "))
  email = str(input("enter the email please "))
  password = (input("enter the password please "))
  user = User(name, email, password)
  for i in range(len(arr)):
    if arr[i].email == mail:
      print("user already exist, so cant add this one ")
      return
  arr.append(user)   
  return user


nithin = user_registration(arr)
rahul = user_registration(arr) 
for i in range(0, len(arr)):
    print(arr[i])
    file.write(f"{arr[i].name}, {arr[i].email}, {arr[i].password}\n")
  