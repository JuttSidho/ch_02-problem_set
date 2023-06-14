"""
implement a program that prompts the user for a vanity plate and then output Valid
if meets all of the requirements or Invalid if it does not. Assume that any letters
in the user’s input will be uppercase. Structure your program per the below, wherein
is_valid returns True if s meets all requirements and False if it does not. Assume 
that s will be a str. You’re welcome to implement additional functions for is_valid 
to call (e.g., one function per requirement).
"""
def starts_with_two_letters(s):
    return s[:2].isalpha()

def has_valid_length(s):
    return 2 <= len(s) <= 6

def no_numbers_in_middle(s):
    return s[-1].isalpha() or s[-1].isdigit() and s[-2] != '0'

def no_punctuation(s):
    return s.isalnum()

def is_valid(s):
    return starts_with_two_letters(s) and has_valid_length(s) and no_numbers_in_middle(s) and no_punctuation(s)

def main():
    plate = input("Enter a vanity plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Call the main function
if __name__ == "__main__":
    main()