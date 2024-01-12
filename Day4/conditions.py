age = int(input("enter your age"))

if age < 18:
    print("You are a minor")
elif age>=18 and age<65:
    print("you are an adult")
elif age > 65:
    print("You are a senior citizen")