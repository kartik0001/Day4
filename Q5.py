quantity=int(input("Enter quantity of purchase: "))
cost=float(quantity*100)

print("Initial cost of %d items = %f" %(quantity,cost))

if cost>1000:
	print("Giving 10% discount")
	cost=cost*0.9
else:
	print("No discount given")

print("Total Cost=%f" %(cost))