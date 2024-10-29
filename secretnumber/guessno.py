secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    # Ask the user to enter an integer number
    guess = int(input("Enter an integer number: "))
    
    # Check if the guess is correct
    if guess == secret_number:
        print("Well done, muggle! You are free now.")
        break  # Exit the loop if guessed correctly
    
    else:
        print("Ha ha! You're stuck in my loop!")