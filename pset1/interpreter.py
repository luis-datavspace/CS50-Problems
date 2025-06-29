'''
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then 
calculates and outputs the result as a floating-point value formatted to one decimal place. 
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

'''

def main():
    
    expr = input('Enter the expression: ')
    
    X, operator, Z = expr.split() # We use split() to "temporarily" convert the string to a list, and assign each value in the list to the variables
    
    X= int(X) #Convert "X" string to X integer
    Z= int(Z) #Convert "Z" string to Z integer


    # We evaluate in case the user wants to divide by 0
    if operator == '/' and Z==0:
        
        Z = dive_nonzero() # Request a valid value using a function that only allows division by Z other than 0 (focus on minimal errors only, exceptions will be handled in pset3)
        
    result = operating_with(X,operator,Z)
    print(f'{result: .1f}')



    
def  operating_with(X, stroperator, Z):
    
    if stroperator == '+':
        return X + Z
    elif stroperator == '-':
        return X - Z
    elif stroperator == '*':
        return X * Z
    elif stroperator == '/':
        return X / Z
    
def dive_nonzero():
    
    # Function to validate that the input Z is not zero using a loop, returns a value only if it is != 0, continues asking for a valid value if Z==0
    while True:
        new_z = int(input('You cannot divide by zero, enter a new value of Z: ')) #Save the variable
        
        #Evaluate the input
        if new_z != 0: 
            return new_z   





main()