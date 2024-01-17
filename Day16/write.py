import string
import random

file = open("C:\\Users\\NithinRajkumar\\Desktop\\skill_captain_python_beginner\\Day16\\test.txt", "a")
arr= []

try:
    no_of_characters= int(input("Please enter the no of charachters"))
except:
   print("please enter a number")
else:
    for i in range(0,no_of_characters):
        charachter =  random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
        print(charachter)
        if(arr.__contains__(charachter)):
            print("Already exists")
        else:
            arr.append(charachter)
    for i in range(0,no_of_characters):
        file.write(arr[i]+"\n")


