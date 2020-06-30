#escape letter

print("I love you \n I see you")
print("C:\\Users\\folder")

print("Red Apple \rWine")   # \r  cursor to first
print("Redd\b apple")       # \b  backspace
print("Red \t apple")       # \t  tap



#Quiz. password making algorythm
#ex. http://google.com
#1. -> google.com
#2. -> google
#3. -> first 3 letters(goo) + letter num(6)+'e' number(1)+!
#password : goo61!

site = "http://facebook.com"
site = site[7:-4]
print(site[:3]+str(len(site))+"!")

url = "http://goooogle.com"
myurl=url.replace("http://", "") #1
myurl= myurl[ : myurl.index(".")] #2
print(myurl)
password = myurl[:3] + str(len(myurl)) + str(myurl.count("e")) + "!"
print(password)