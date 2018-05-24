age1 = input("Enter age of first person:")
age2 = input("Enter age of second person:")
age3 = input("Enter age of third person:")
if age1 > age2 and age1 > age3:
    print("Person 1 is oldest")
    if age2 < age3:
        print("Person 2 is youngest")
    else:
        print("Person 3 is youngest")
elif age2 > age3 and age2 > age1:
    print("Person 2 is oldest")
    if age1 < age3:
        print("Person 1 is youngest")
    else:
        print("Person 3 is youngest")
else:
    print("Person 3 is oldest")
    if age1 < age2:
        print("Person 1 is youngest")
    else:
        print("Person 2 is youngest")
