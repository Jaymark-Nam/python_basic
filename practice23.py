
hand = open('sample.txt','r')
for line in hand:
    line = line.rstrip()
    if line.find('This') >= 0:
        print(line)


import re

hand = open('sample.txt')
for line in hand:
    line = line.rstrip()
    if re.search('We',line):
        print(line)