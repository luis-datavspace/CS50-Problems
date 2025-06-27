'''
In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. 
If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. 
Ignore any leading whitespace in the user's greeting, and treat the user's greeting case-insensitively.
'''



def main():
    user_greeting = input('Greeting: ').lower().strip()
    print(ev_greeting(user_greeting))




def ev_greeting(user_greeting):
    return "$0" if user_greeting == "hello" else "$20" if "h" in user_greeting else "$100"
    #Returns "$ 0" if User Greeetin is equal to "Hello", but "$ 20" if the letter "H" is in User Greetin and if it does not return "$ 100"

main()
    