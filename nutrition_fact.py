"""
implement a program that prompts consumers users to input a fruit (case-insensitively)
and then outputs the number of calories in one portion of that fruit, per the FDA’s 
poster for fruits, which is also available as text. Capitalization aside, assume that 
users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). 
Ignore any input that isn’t a fruit.
"""
def get_fruit_calories(fruit):
    fruit_calories = {
        "Apple": 52,
        "Banana": 96,
        "Blueberries": 57,
        "Grapes": 69,
        "Orange": 62,
        "Peach": 59,
        "Pear": 57,
        "Pineapple": 50,
        "Strawberries": 32,
        "Watermelon": 30
    }

    return fruit_calories.get(fruit.capitalize())

def main():
    fruit = input("Enter a fruit: ")

    calories = get_fruit_calories(fruit)
    if calories is not None:
        print("Number of calories in one portion of", fruit, ":", calories)
    else:
        print("Invalid fruit. Please enter a valid fruit.")

# Call the main function
if __name__ == "__main__":
    main()