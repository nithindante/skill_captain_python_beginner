try:
    len = int(input("enter the length of dictionary"))
except:
    print("enter number")
else:
    arr_list={}
    for a in range(len):
        inp = input("enter the key")
        val = input("enter the value")
        arr_list[inp]=val
arr_list["e"]=5
print(arr_list)
del arr_list["e"]
print(arr_list)
arr_list["a"]=10
if "b" in arr_list:
    print("b is present")
for keyss in arr_list.keys():
    print(keyss)

