def main():
    user_ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?: ").lower()
    print(question_ans(user_ans))
    
    
    
    
def question_ans(text):
    return "Yes" if text in ["42","forty-two","forty two"] else "No"

main()