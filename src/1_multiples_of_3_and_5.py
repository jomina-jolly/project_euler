'''
Created on Jun 9, 2017

@author: Jomina Jolly
'''
# Find the sum of n terms in an series
def sum_of_n(a,m,d):
    n=((m-a)/d)+1   #to find the number of terms in the series
    total= float((n)*(m+a)/2)
    return total

def upper_limit(n,d):
    return n-(n%d)


n=input("Enter the limit")  
# Adds the sum of multiples of 3 and 5 and subtract the sum of common multiples(multiples of 15) 
result = sum_of_n(0,upper_limit(n-1,5),5)+sum_of_n(0,upper_limit(n-1,3),3)-sum_of_n(0,upper_limit(n-1,15),15)
print 'The sum of all the multiples of 3 or 5 below %d is %d'%(n,result)

    
    


    