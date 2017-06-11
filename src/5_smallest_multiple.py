'''
Created on Jun 9, 2017

@author: Jomina Jolly
'''
import fractions
from math import sqrt

# Creates a list of prime  numbers till n
def prime_numbers(n):
    p=[]
    for i in range(1,n+1):
        if is_prime(i):
            p.append(i)
        else:
            non_prime.append(i)
    return p   

#Function to check whether a number is prime or not           
def is_prime(n):
    count=0
    sqr_root=int(sqrt(n))
    if n==0 or n==1:
        return False
    else:
        for i in range(2,sqr_root+1): #check for the modulo of n with all numbers below sqrt(n)
            if n%i==0:
                count+=1
        if count>0:
            return False
            
        else:
            return True

#Function to get the product of all numbers in a list        
def product(p):
    product=1
    for i in p:
        product*=i
    return product
            
non_prime=[]
a=input("Enter the limit ")
prime= prime_numbers(a)
product= product(prime)
for i in range(len(non_prime)-1,0,-1):#List of all the prime numbers in the range entered
    if product%non_prime[i]==0:       #checks if the product of prime numbers below the limit is divisible by each non prime number  
        continue
    else:                                         #if the non-prime number is not divisible,  
        gcd= fractions.gcd(product, non_prime[i]) #Find the HCF/GCD of existing product and the non prime number
        product*=(non_prime[i]/gcd)               # multiplies the factor to make the non-prime number divisible by product  
        
        
print 'the smallest positive number that is evenly divisible by all of the numbers from 1 to 20=',product



