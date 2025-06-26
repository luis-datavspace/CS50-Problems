def main():
    #Prompt the user for your phrase
    phrase = input('')
    
    phrase_playbaack= phrase.replace(" ", "...") #Replace spaces with "..."
    
    print(phrase_playbaack)#Return the phrase withe "..." as separator of words
    
main()
