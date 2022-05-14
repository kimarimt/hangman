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
    lives = len(assets.stages)

    while ''.join(dashes) != word and lives > 1:
        guess = input('Guess a letter: ')

        if guess not in guesses:
            if guess in word:
                for position, letter in enumerate(word):
                    if guess == letter:
                        dashes[position] = letter
            else:
                print('Incorrent guess. 1 life lost')
                lives -= 1
        else:
            print(f'You already guessed {guess}')

        clear()
        guesses.add(guess)
        print(f'Word: {"".join(dashes)}')
        print(f'Guesses: {", ".join(guesses)}')
        print(assets.stages[lives - 1])
    else:
        if ''.join(dashes) == word:
            print('YOU WIN!')
        else:
            print('GAME OVER!') 

        print(f'The word was {word}.')

if __name__ == '__main__':
    main()
