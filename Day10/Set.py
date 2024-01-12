try:
    num = int(input("enter the length of list"))
except:
    print("enter a number")
else:
    first_list= []
    for a in range(num):
        ele = input("enter the elements")
        first_list.append(ele)
    second_set = set()
    def list_to_set(first_list):
        new_set = set(first_list)
        return new_set
    second_set = list_to_set(first_list)
    def set_to_list(second_set):
        new_list = list(second_set)
        return new_list
    second_list = set_to_list(second_set)
    print(second_set)
    print(second_list)

