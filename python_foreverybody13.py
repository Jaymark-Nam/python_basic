
import re

hand = open('actual.txt')

numlist = list()
add = 0

for line in hand:
    want = re.findall('([0-9]+)',line)
    numlist = numlist + want
    

for i in numlist:
    add = add + int(i)

print(add)