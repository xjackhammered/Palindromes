def main():
    while True:
        word = input("Which word do you want to check? (Press 'x' to stop) ")
        if word.upper() == "X":
            break
        elif word.isdigit():
            print("Numbers cannot be palindromes.")
        else:
            palindrome(word)

def palindrome(word):
    reversed_word = "".join(reversed(word))
    if word.upper() == reversed_word.upper():
        print("The word is a palindrome!")
    else:
        print("The word is not a palindrome.")

main()



