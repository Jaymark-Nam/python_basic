# string

sentence = 'I wish I were a boy'
print(sentence)
sentence2 = "python is easy"
print(sentence2)


#slicing
jumin= "950120-1654321"
print("sex :" +jumin[7])
print("year :" +jumin[0:2])
print("month :" +jumin[2:4])
print("day :" +jumin[4:6])

#string 
python = "Python is Fancy"
print(python.lower())   #all lower
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Life"))

index = python.index("n")
print(index)
index = python.index("n", index+1)  #finding next "n"
print(index)

print(python.find("n"))


#sting format
print("a"+"b")  #ab
print("a","b")  #a b

print("I'm %d age years old" % 30)
print("I'm interested to %s" %"climbing")   
print("Apple starts from %c" %"A")          #one letter
print("I like %s and %s" %("blue","red"))

print("I am {}age years old" .format(20))
print("I like {} and {}" .format("cafe","tabasco"))
print("I like {1} and {0}" .format("cafe","tabasco"))


print("I am {age}years old, like {color}" .format(age=20,color="red"))

age = 80
color = "dark blue"
print(f"I am {age}years old, like {color}")