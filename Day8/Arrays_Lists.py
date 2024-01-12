
a = int(input("enter the length of the list"))
list_one = []
for i in range(a):
    ele = input("enter the element")
    list_one.append(ele)

b = int(input("enter the length of the second list"))
list_two = []
for i in range(a):
    ele = input("enter the element")
    list_two.append(ele)

def sum_lists(list_one,list_two):
    return list_one + list_two

print(sum_lists(list_one,list_two))