"""
implement a program that prompts the user to insert a coin, one at a time, each
time informing the user of the amount due. Once the user has inputted at least 50 cents,
output how many cents in change the user is owed. Assume that the user will only input 
integers, and ignore any integer that isn’t an accepted denomination.
"""
def calculate_change(coins_inserted):
    change = coins_inserted - 50
    return change

def main():
    coins_inserted = 0

    while coins_inserted < 50:
        coin = int(input("Insert a coin (5, 10, or 25 cents): "))

        if coin in [5, 10, 25]:
            coins_inserted += coin
        else:
            print("Invalid coin. Please insert a valid coin.")

        amount_due = 50 - coins_inserted
        print("Amount due:", amount_due, "cents")

    if coins_inserted >= 50:
        change = calculate_change(coins_inserted)
        print("Change owed:", change, "cents")

# Call the main function
if __name__ == "__main__":
    main()