largest = None
smallest = None
while True:
	try:
		num = input("Enter a number: ")
		if num == "done" : break
		if int(num)>largest or largest ==None:
			largest = int(num)
		if int(num)<smallest or smallest ==None:
			smallest = int(num)
	except :
		print("Invalid input")
    
    
print("Maximum is", largest)
print("Minimum is", smallest)