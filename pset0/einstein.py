'''
In a file called einstein.py, implement a program in Python that prompts the user for mass
as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer.
'''

def main():
    
    E = None #I define E as no value, it is the value to calculate, defined to have previous order
    c= 300000000 #represents the speed of light (measured approximately as 300000000 meters per second)
    
    m_user = int(input("m: "))
    
    E = m_user * (c**2) #We calculate the value of E and assign it to the variable created previously
    
    print(f"E: {E}") # I print using f-strings to display variable E formatted to know that E is printed "E: {Value of E}"

    
main()