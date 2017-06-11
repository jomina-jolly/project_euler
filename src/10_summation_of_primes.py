'''
Created on Jun 10, 2017

@author: Jomina Jolly

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

from math import sqrt


def is_prime(n):
    count=0
    sqr_root=int(sqrt(n))
    if n==0 or n==1:
        return False
    if n==3:
        list_of_prime.append(n)
        return True
    else:
        for i in list_of_prime:#checks for the divisibility with just the prime number less than the sqrt root of the number.
            if i<=sqr_root:
                if n%i==0:
                    count+=1
                    break
            else:
                break
        if count>0:
            return False
                
        else:
            list_of_prime.append(n)
            return True
        
list_of_prime=[2]
limit=input("Enter the limit")
total=2
number=1
print "Computing the total..."
#List of all odd numbers to check for prime
for i in range(1,limit,2):
    if is_prime(i):
        total+=i

print 'The sum of all the primes below %d =%d'%(limit,total)