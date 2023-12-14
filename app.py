import random
def get_player_name():
    return input("Hello, enter your name: ")

def generate_secret_number():
    return random.randint(1, 20)

def get_player_guess():
    return int(input('Take a guess: '))

def evaluate_guess(guess, secret_number):
    if guess < secret_number:
        return 'low'
    elif guess > secret_number:
        return 'high'
    else:
        return 'correct'

def main():
    name = get_player_name()
    secret_number = generate_secret_number()

    print(f"Well {name}, I am thinking of a number between 1 and 20")

    for i in range(1, 7):
        guess = get_player_guess()
        result = evaluate_guess(guess, secret_number)

        if result == 'low':
            print('Your guess is too low')
        elif result == 'high':
            print('Your guess is too high')
        else:
            break

    if result == 'correct':
        print(f"Good job, {name}! You guessed my number.")
    else:
        print(f'Nope, the number I was thinking of was {secret_number}')

main()
