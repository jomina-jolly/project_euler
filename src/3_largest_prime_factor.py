'''
Created on Jun 10, 2017

@author: Jomina Jolly
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt

#return a list of prime numbers below the square root of n
def list_of_prime(n):  
    print "Please wait while computing the prime numbers"
    sqr_root=int(sqrt(n))
    for i in range(1,sqr_root+1,2): 
        if is_prime(i):
            prime_numbers.append(i)

#checks if a given number is prime
def is_prime(n):
    sqr_root=int(sqrt(n))
    count=0
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    else:
        for i in range(2,sqr_root+1): 
            if n%i==0:
                count+=1
        if count==0:
            return True
        else:
            return False
             
input_value=input("Enter the value ")
prime_numbers=[2]
list_of_prime(input_value)  #returns the list of prime numbers below the sqrt root of the input_value
count=0
factors=[]
for prime in prime_numbers:
    if input_value%prime==0:  #Checks for the divisibility with each prime number below the input_value
        y= input_value/prime    
        factors.append(prime)  #adds to the list of factors of input_value 
        if is_prime(y):         #if divisible, checks of  quotient after dividing is a prime.
            factors.append(y)   #if prime, the largest prime factor is optained and add to the list of factors
            break
        
            
print 'the largest prime factor of the number %d =%d'%(input_value,max(factors))

        
        
