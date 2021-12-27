def isPalindrome(w):
    i = 0
    j = len(w)-1
    while (i<j):
        if (w[i]!=w[j]): return False
        i+=1
        j-=1
    return True

def isPrime(x):
    i = 2
    while (i<x):
        if (x%i == 0):return False
        i += 1
    return True

def factorial(x):
    if (x == 0): return 1
    else: return x*factorial(x-1)
    
def isInRange(x,range):
    return (x<=range[1] and x>=range[0])

def sumList(list):
    sum = 0
    for x in list:
        sum += x
    return sum

def max(x,y,z):
    if (x>=y):
        if (z>=x): return z
        else: return x
    else:
        if (z>=y): return z
        else: return y


str = input("Please enter the string: ")
rev = ""
i = len(str)-1

while (i>=0):
    rev += str[i]
    i-=1

print("Reversed String: "+rev)
