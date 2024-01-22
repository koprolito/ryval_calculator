from cmath import sqrt, pi, e
import math

class Operation():    
        
    def sum(n1:float,n2:float) -> float: 
        '''Returns a float value of the sum of two numbers n1 and n2 (n1+n2)'''
        return n1+n2
    
    def substract(n1:float,n2:float) -> float:
        '''Returns a float value of the subtraction of two numbers n1 and n2 (n1-n2)'''
        return n1-n2
    
    def multiply(n1:float,n2:float) -> float:
        '''Returns a float value of the multiplication of two numbers n1 and n2 (n1*n2)'''
        return n1*n2
    
    def divide(n1:float,n2:float) -> float:
        '''Returns a float value of the division of two numbers n1 and n2 (n1/n2)
        \nIf n2 is 0, returns a string value of "Error"'''
        try:
            return n1/n2
        except ZeroDivisionError:
            return 'Cannot divide by 0'

    def power(n1:float,n2:float) -> float:
        '''Returns a float value of a n1 number powered by a n2 number (n1**n2)'''
        return n1**n2
    
    def porcentage(n1:float,n2:float) -> float:
        '''Returns a float value of the percentage of a n1 number over a n2 number (n1*n2/100)'''
        return n1*n2/100
    
    def squared_root(n1:float) -> float:
        '''Returns a float value of the square root of a n1 number (sqrt(n1))'''
        return sqrt(n1)
    
    def root(n1:float,n2:float) -> float:
        '''Returns a float value of a n1 number rooted by a n2 number (n1**(1/n2))'''
        return n1**(1/n2)