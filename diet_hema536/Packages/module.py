def add(num1,num2):
    return num1+num2

def isleapyear(year):
    if (year%400==0) or (year%4==0 and year%100!=0):
        print("it is a leap year")
    else:
        print("not a leap year")
       
    
    
    
    
def isPrime(num):
    flag=0
    for i in range(2,num+1):
        if num%i==0:
            flag=1
    if flag==1:
        print("prime")
    else:
        print("not a prime")
        
        
        
def alleven(lb,ub):
    for i in range(lb,ub+1):
        if i%2==0:
            print(i)
            
            
            
            
def fact(num):
    mul=1
    for i in range(1,num+1):
        mul*=i
    return mul