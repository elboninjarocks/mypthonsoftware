#Elijah Sarver 2024

def introduction():
	choice = input("Press P to convert percentage to decimal, D to convert decimal to percentage, or Q to quit ").strip().upper()
	if choice == "P":
		percernttodecimal()
	elif choice == "D":
		decimaltopercent()
	elif choice == "Q":
		exit()
	else:
		introduction()
	
def percernttodecimal():
	percentage = float(input("Enter a percentage without the % symbol and I'll convert it to a decimal: "))
	x = 100
	result = percentage / x
	print(result)
	check = input("Enter y to go back, or any other key to continue > ").upper
	if check == "y": 
		introduction()
	percernttodecimal()
	

def decimaltopercent():
	decimal = float(input("Enter a decimal and I'll convert it to a percentage: "))
	x = 100
	result = decimal * x
	print(result,"%")
	check = input("enter y to go back, or any other key to continue > ").upper
	if check == "y": 
		introduction()
	decimaltopercent()
	
introduction()