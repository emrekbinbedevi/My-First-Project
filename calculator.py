def calculate(x,y,ops):
	if ops not in "+-*/":
		return "Only + - * /!!!"
	if ops == "+":
		return(str(x) + ops + str(y) + "=" + str(x+y))
	elif ops == "-":
		return(str(x) + ops + str(y) + "=" + str(x-y))
	elif ops == "*":
		return(str(x) + ops + str(y) + "=" + str(x*y))
	elif ops == "/":
		return(str(x) + ops + str(y) + "=" + str(x/y))
while True:

	x = input("Please enter the first number!: ")
	y = input("Please enter the second number!: ")
	ops = input ("Please choose this symbols +-*/: ")
	print(calculate(x,y,ops))