'''
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the user's input will indeed be in camel case.
'''

def main():
    user_name = input('camelCase: ')
    print(snake(user_name))
    

def snake(text):
    
    # Accmulator that builds the text in Snake_case
    result = ''
    
    #Loop for to traverse letter by letter in "text"
    for c in text:
        
        if c.isupper(): #if c is upper
            
            #store the uppercase letter with a "_" before it to have something like "_c"
            result += f'_{c.lower()}'
            
        #If c is not capitalized, store the letter in its original state in result 
        else:
            result += c
    #Return the Text converted in Snake_case
    return result
        
        
        
main()