import assets
import os
import time


def clear():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print(assets.logo)
    clear()

    word = 'hello'
    dashes = ['_' for _ in range(len(word))]
    guesses = set()

    while ''.join(dashes) != word:
        guess = input('Guess a letter: ')

        if guess not in guesses:
            if guess in word:
                for position, letter in enumerate(word):
                    if guess == letter:
                        dashes[position] = letter
            else:
                print('Bad guess')
        else:
            print(f'You already guessed {guess}')

        clear()
        guesses.add(guess)
        print(f'Word: {"".join(dashes)}')
        print(f'Guesses: {", ".join(guesses)}')


if __name__ == '__main__':
    main()
