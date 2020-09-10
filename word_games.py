"""with open("scrabble.txt", 'r') as f:
	count = 0
	for line in f:
		if count > 5:
			break
		print(line)
		count = count + 1
"""
def is_word(word):
	with open("scrabble.txt", 'r') as f:
		for line in f:
			if line == word:
				print("found")

def go_through(letters, word):
	with open("scrabble.txt", 'r') as f:
		for line in f:
			#print(line[0: letters])
			if line[0:letters] == word:
				return True
		return False



word = ""
game_going = True
while game_going:
	appending = input("next letter: ")
	if len(appending) != 1:
		print("improper input")
	elif appending == 'quit':
		break
	else:
		word += appending
		print(word)
		print(len(word))
		print(is_word(word))
		#print(go_through(len(word), word))
		"""if go_through(len(word), word):
			print("going to be a word")
		else:
			print("no")"""
