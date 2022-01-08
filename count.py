count = 0 # The letter count is 0
sentence = input('Type a something ') # Ask the user to put a sentence
if " " in sentence: # If there is a space in the sentence that the user is giving us
	new_sentence = sentence.replace(" ", "") # Variable with new_sentence where we delete the space e.g: If I type: Hello World this will transfer it to: HelloWorld
	for i in new_sentence: # For every character/letter in the new sentence
		count += 1 # We add 1 to the count so it counts all the letters
		print(f"{i} -> {count}") # We print i which is every character/letter in the sentence and then the count  
else: # Else if the sentence hasn't " " (space) 
	for i in sentence: # For every character/letter in the sentence
		count += 1 # Add one in the variable count
		print(f"{i} -> {count}") # We print i which is every character/letter in the sentence and then the count
