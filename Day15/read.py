
try:
    with open("C:\\Users\\NithinRajkumar\\Desktop\\skill_captain_python_beginner\\Day15\\test.txt") as file:
        print(len(file.readlines()))
except:
    print("file not found")
