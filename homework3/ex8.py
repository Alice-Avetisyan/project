words = ['I', 'am', 'a', 'word']
print("Enter two words: ")
word1 = input()
words.append(word1)
word2 = input()
words.append(word1)

print("Present") if word1 in words else print("Absent")
print("Which element would you like to remove? ")
removeel=int(input())
words.pop(removeel)
print(words[:])