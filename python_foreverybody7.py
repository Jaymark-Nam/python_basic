# Use words.txt as the file name
file_name = input("Enter file name: ")
file = open(file_name)
for line in file:
    
    line = line.rstrip()
    line = line.upper()
    print(line)
