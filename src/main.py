import os
from coin_flip import coin_flip
from coin_flip_simulator import coin_flip_simulator
from guessing_game import play_guessing_game

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("--- Coin Flip Simulator ---")
        print("1. Flip a coin")
        print("2. Simulate multiple coin flips")
        print("3. Play coin flip guessing game")
        print("4. Quit")
        print()

        user_choice = input("Enter the number corresponding to your choice: ")

        if user_choice == '1':
            result = coin_flip()
            print(f"\nThe coin landed on {result}.")
            input("\nPress Enter to continue...")
        elif user_choice == '2':
            num_of_flips = int(input("\nEnter the number of coin flips: "))
            heads, tails = coin_flip_simulator(num_of_flips)
            print(f"\nAfter {num_of_flips} flips, there were {heads} Heads and {tails} Tails.")
            input("\nPress Enter to continue...")
        elif user_choice == '3':
            num_of_guesses = int(input("\nEnter the number of guessing rounds you want to play: "))
            correct_guesses = play_guessing_game(num_of_guesses)
            print(f"\nYou guessed correctly {correct_guesses} times out of {num_of_guesses} rounds.")
            input("\nPress Enter to continue...")
        elif user_choice == '4':
            print("\nThank you for using the Coin Flip Simulator. Goodbye!")
            break
        else:
            print("\nInvalid input. Please enter a number between 1 and 4.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
