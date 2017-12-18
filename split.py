string = input("Enter your full name: ")
list1 = string.split()
if(len(string)==2):
    (first_name, last_name) = list1
    print("first_name: ", first_name)
    print("Last name: ", last_name)
elif(len(string)==3):
    (first_name, middle_name, last_name) = list1
    print("First_name: ",first_name)
    print("Middle name: ",middle_name)
    print("Last name: ",last_name)
