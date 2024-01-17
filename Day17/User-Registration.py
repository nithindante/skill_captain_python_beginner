file = open("C:\\Users\\NithinRajkumar\\Desktop\\skill_captain_python_beginner\\Day17\\input.txt", "a")

class User:

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def __str__(self):
    return f"{self.name},{self.email},{self.password}"


arr = []


def user_registration(arr):
  f_name = (input("enter the name please "))
  mail = str(input("enter the email please "))
  password = (input("enter the password please "))
  user = User(f_name, mail, password)
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
  file.write(arr[i])
file.close() 