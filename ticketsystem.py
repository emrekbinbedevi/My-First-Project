#welcome to ticket system

print("Hello!Welcome to ticket buy system.Please follow the insturictions.")
arrival = input("Hello Please choose the arrival destination: ")
if arrival == "izmir":
	print("'izmir' selected.")
	date = input("Please choose this dates;today,tomorrow: ")
	if date == "tomorrow":
		print("Sorry,Flight not found!")
	if date == "today":
		print("Great!Last step,please choose your class;bussines or economy")
		x = input("Choose your class: ")

		if x == "bussines":
			print("You choosed bussines class")

		elif x == "economy":
			print("You choosed economy class!")

		else:
			print("You choosed a wrong class.But if you want you can continue")


		name = input("Please enter the name: ")
		print(f"You have succesfuly bought the ticket {name}!You will pay When you go to the our kiosk")
		print(f"Your informations:{name},istanbul-{arrival},{date},{x}")

if arrival != "izmir":
	print("Flight not found please try again!")


