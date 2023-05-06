from coin_flip import coin_flip

def guess_coin_flip():
    guess = input("Guess the outcome of the next coin flip (Heads/Tails): ").capitalize()

    if guess not in ['Heads', 'Tails']:
        print("Invalid input. Please enter 'Heads' or 'Tails'.")
        return None

    return guess

def play_guessing_game(flips):
    correct_guesses = 0

    for _ in range(flips):
        user_guess = guess_coin_flip()
        if user_guess is None:
            continue

        actual_outcome = coin_flip()
        if user_guess == actual_outcome:
            correct_guesses += 1
            print(f"Correct! The coin landed on {actual_outcome}.")
        else:
            print(f"Sorry, the coin landed on {actual_outcome}.")

    return correct_guesses
