string = input("Enter your full name: ")
list1 = string.split()
if(len(string)==2):
    (first_name, last_name) = list1
    print(first_name, last_name)
elif(len(string)==3):
    (first_name, middle_name, last_name) = list1
    print(first_name, middle_name, last_name)
