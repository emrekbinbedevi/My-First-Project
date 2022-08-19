confirm = input("Write 'start' to continue: ")
onay = "start"
if confirm == onay:
    print("Good!")
while confirm != onay:
    confirm = input("Write 'start' to continue: ")
print("Welcome the game!")
secret_word = "hevagi"
guess_string = ""
lives = 10
while lives > 0:
	charecter_left = 0
	for charecter in secret_word:
		if charecter in guess_string:
			print(charecter)
		else:
			print("-")
			charecter_left += 1
	if charecter_left == 0:
		print("Well done!!")
		break

	guess = input("Write a word: ")
	guess_string += guess
	if guess not in secret_word:
		lives -= 1
		print("Wrong!")
		print(f"You have {lives} left")
		if lives == 0:
			print("You died")
