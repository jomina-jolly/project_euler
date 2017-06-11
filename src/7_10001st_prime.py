'''
Created on Jun 9, 2017

@author: Jomina Jolly
'''

from math import sqrt   
#to check a number for prime             
def is_prime(n):
    sqr_root=int(sqrt(n))
    count=0
    if n==0 or n==1:
        return False
    else:
        for i in list_of_prime: #checks for the divisibility with just all the prime numbers less than the number.
            if i<=sqr_root:
                if n%i==0:
                    count+=1
                    break
        if count>0:
            return False
            
        else:
            list_of_prime.append(n)
            return True
        

a=input("Enter the index")
list_of_prime=[2]
max_index=a
index=1
number=1
while index<max_index:
    number+=2
    if is_prime(number):
        index+=1
        print 'the prime number of %d is %d'%(index,number)
        

print '%d prime number is %d'%(a,number)  