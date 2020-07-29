
num = list()

while True:
    inp = input('Enter number')
    if not inp =='done':
        num.append(float(inp))
    elif inp=='done':break

average = float(sum(num)/len(num))

print(average)