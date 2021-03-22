import time
str1=input("Enter string you want to print")
n=int(input("Enter number of lines"))
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print(str1, end=" ")
    print()
time.sleep(30)
