
def computer_chose(word):
	with open("word_games/scrabble.txt", 'r') as f:
		for line in f:
			if line[0:len(word)] == word:
				if len(line) - 1 > len(word):
					return line[0:len(word) + 1]
		return None
		
def is_word(word):
	with open("word_games/scrabble.txt", 'r') as f:
		for line in f:
			longest = ""
			if line[0:len(line)-1] == word:
				return True
		return False
		print("not found")

def go_through(letters, word):
	with open("word_games/scrabble.txt", 'r') as f:
		for line in f:
			if line[0:letters] == word:
				return True
		return False

word = ""
game_going = True
while game_going:
	appending = input("next letter: ")
	if len(appending) != 1:
		print("improper input")
	elif appending == 'q':
		break
	else:
		word += appending
		if (not go_through(len(word), word)):
			print("Cannot turn into a word; you lose")
			word = ""
			break
		elif is_word(word) and len(word) > 3:
			print("You made a word; you lose")
			word = ""
		else:
			print(word)
		if computer_chose(word) == None:
			print("you win, the computer couldn't make a valid word")
		else:
			word = computer_chose(word)
			if is_word(word) and len(word) > 3:
				print("computer said: " + word + ", you win")
				word = ""
			else:
				print("Computer made the new word: " + word)