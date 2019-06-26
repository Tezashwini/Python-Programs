# Function to check whether the number is prime or not
n=int(input())
def prime(n):
    flag=1
    if n==2:
        return True
    for i in range(2,n//2+1):
        if n%i==0:
            flag=0
            return False
    if flag ==1 :
        return True
prime(n)
# function to know no of factors
def noofprimefactors(n):
    if prime(n):
        return 1
        count=0
        for i in range(2,n//2+1):
            if prime(i) and n%i==0:
                count+=1
            return count
# factorial program
s=int(input())
def fact(s):
    for w in range (1,s+1):
        if s%w==0:
            print(w,end=" ")
fact(s)