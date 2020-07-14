name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    start = line.find(':')
    host = line[start-2:start]
    lst.append(host)
    

for l in lst:
    counts[l] = counts.get(l,0) + 1


for k,v in sorted(counts.items()):
    print(k,v)

    
'''
for key in counts :
    print(key, counts[key])


code my Jaewoo Nam
'''

