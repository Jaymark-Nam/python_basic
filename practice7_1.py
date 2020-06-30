from random import *
memb = range(1,21)
memb = list(memb)

print(memb)
shuffle(memb)
print(memb)

winner = (sample(memb,4))
coffee = ("{}".format(winner[0]))
chicken = ("{}".format(winner[1:]))
print("Coffee winnner is " +coffee)
print("Chicken winnner is "+chicken)


