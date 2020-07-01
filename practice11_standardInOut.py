#standard In and out

print("Python","Java", "C++", sep=" vs ")

print("Python","Java", "C++", sep=",",end="?")   #end = connects with next sentence. default = 줄바꿈
print("what is more fun?")

import sys
print("Python", "Java", file=sys.stdout)  # standard output
print("Python", "Java", file=sys.stderr)  # standard error, need to check error



scores = {"math":0,"eng":50,"code":100}
for subject, score in scores.items():
    print(subject.ljust(8),str(score).rjust(4),sep=":")   #왼쪽 정렬 8칸


# bank waiting num
for num in range(1,21):
    print("waiting number" +str(num).zfill(3))



#scanf
answer = input("insert any value : ")   #string type
print("inserted value is " +answer)


#different output format
print("{0: >10}".format(500))  #leave empty place empty, sort right(>), prepare 10 places
print("{0: >+10}".format(500))  #if (+), show +, if(-) show -
print("{0:_<+10}".format(500))  #sort left, replace empty to _
print("{0:,}".format(103003202030))  # comma every 3 digits
print("{0:+,}".format(103003202030))  # comma every 3 digits, +-
print("{0:^<+30,}".format(103003202033320))  # comma every 3 digits, +-, prepare places, emptyplace = ^
print("{0:f}".format(5/3))  #소수점
print("{0:.2f}".format(5/3))  #소수점 2 자리까지


#FILE IN AND OUT

#write
score_file = open("score.txt","w", encoding="utf8") #encoding="utf8" -- for korean
print("Math = 0", file = score_file)
print("English = 30", file = score_file)
score_file.close()


score_file = open("score.txt", "a", encoding="utf8")    # "a" 있는 파일에 추가 입력
score_file.write("Science = 80")
score_file.write("\nHistory  = 80")
score_file.close()


#read
score_file = open("score.txt","r", encoding="utf8") 
print(score_file.read())
score_file.close()


#read line by line
score_file = open("score.txt","r")
print(score_file.readline())    #한 줄 읽고 커서는 다음줄로
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()


#if we dont know how many rows are file
score_file = open("score.txt","r")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()



score_file = open("score.txt","r")
lines = score_file.readlines()  # save in list type
for l in lines:
    print(l, end="")
score_file.close()
