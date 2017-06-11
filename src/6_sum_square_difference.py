'''
Created on Jun 9, 2017

@author: Jomina Jolly
Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.
'''


def sumOfSquares(n):
    sum_of_square=(n*(n+1)*(2*n+1))/6
    return sum_of_square
    
def squareOfSum(n):
    sum_of_n= (n*(n+1))/2
    square_of_sum= sum_of_n**2    
    return square_of_sum

input_value=input("Enter the limit")
difference=  squareOfSum(input_value)-sumOfSquares(input_value)
print 'The difference between the sum of the squares the square of the sum of first %d is %d'%(input_value,difference)