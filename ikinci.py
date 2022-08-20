name = input("What's your name?: ")
print(f"Hello {name},Welcome!")
live = 5
secret_word = ("airplane")
guess_global = ""
while live > 0:
	karakter_left = 0
	for karakter in secret_word:
		if karakter in guess_global:
			print(karakter)
		else:
			print("-")
			karakter_left += 1
	if karakter_left == 0:
		print("Well done!")
		break

	guess = input("Write a word: ")
	guess_global += guess
	if guess not in secret_word:
		live -= 1
		print("Wrong!")
		print(f"{live} lives remaining")
		if live == 0:
			print("GG!")
