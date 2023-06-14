"""
implement a program that prompts the user for a str of text and then outputs 
that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted 
in uppercase or lowercase.
"""
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    text_without_vowels = ''

    for char in text:
        if char not in vowels:
            text_without_vowels += char

    return text_without_vowels

def main():
    text = input("Enter a string of text: ")
    text_without_vowels = remove_vowels(text)
    print("Text without vowels:", text_without_vowels)

# Call the main function
if __name__ == "__main__":
    main()