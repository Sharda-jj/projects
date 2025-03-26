import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()

    if choice == 'y':  # Colon (:) was missing
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')  # Fixed print statement

    elif choice == 'n':  # Corrected elif syntax
        print('Thanks for playing!')
        break  # Fixed break placement

    else:
        print('Invalid choice!')  # Corrected indentation




