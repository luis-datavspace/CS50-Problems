def main():
    
    usert_phrase = input('Enter the text: ')
    print(convert(usert_phrase))    
    
    
def convert(text):
    text = text.replace(":(", "🙁")
    text = text.replace(":)", "🙂")
    
    return text


main()