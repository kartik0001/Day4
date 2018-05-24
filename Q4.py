age=int(input("Enter your age:"))
sex=input("Enter your sex(M/F):")
ms=input("Enter your Maritial Status (Y/N):")
if sex=='F':
	print("Employee will work only in urban areas")
elif sex=='M' and age>=20 and age<=40:
	print("Employee can work anywhere")
elif sex=='M' and age>=40 and age<=60:
	print("Employee will work only in urban areas")
else:
	print("ERROR")