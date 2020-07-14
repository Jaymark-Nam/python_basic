

counts = dict()
print("Enter line of text")
line = input()
words = line.split()     # list of splitted words
for word in words :
    counts[word] = counts.get(word,0) + 1

    
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
