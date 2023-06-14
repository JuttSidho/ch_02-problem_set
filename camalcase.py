"""
 implement a program that prompts the user for the name of a variable in camel case 
 and outputs the corresponding name in snake case. Assume that the user’s input will 
 indeed be in camel case
"""
def main():
    # Prompt the user for a variable name in camel case
    camel_case = input('Enter the variable name in camal case:  ')

    # Convert the camel case name to snake case
    snake_case = convert_to_snake_case(camel_case)

    # Output the snake case name
    print("Snake case name:", snake_case) 

def convert_to_snake_case(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')

# if  __name__ == "__main__":
main()