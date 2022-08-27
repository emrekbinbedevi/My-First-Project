def calculate(x,y,ops):
	if ops not in "+-*/":
		return "Only + - * /!!!"
	if ops == "+":
		return(str(x) + ops + str(y) + "=" + str(x + y))
	if ops == "-":
		return(str(x) + ops + str(y) + "=" + str(x - y))
	if ops == "*":
		return(str(x) + ops + str(y) + "=" + str(x * y))
	if ops == "/":
		return(str(x) + ops + str(y) + "=" + str(x / y))
while True:

	x = int(input("Please enter the first number!: "))
	ops = input ("Please choose this symbols +-*/: ")
	y = int(input("Please enter the second number!: "))
	print(calculate(x,y,ops))
