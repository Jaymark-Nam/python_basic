
counts = dict()
print("Enter line of text")
line = input()
words = line.split()     # list of splitted words

#print(words)

for word in words :
    counts[word] = counts.get(word,0) + 1  #dictionary.  'word': number
print(counts) 