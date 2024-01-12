try:
    number = int(input("Please enter the number"))  
except:
    print("Please enter a number")
else:
    def is_even(num):
        if num%2==0:
            return True
        else:   
            return False
    print(is_even(number))