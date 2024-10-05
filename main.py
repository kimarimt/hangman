import assets
import helpers


def main():
    word = 'hello'
    dashes = ['_' for _ in word]
    guesses = set()
    lives = len(assets.STAGES) - 1
    final_word = ''.join(dashes)

    print(assets.LOGO)
    input('Press any key to continue: ')
    helpers.clear()

    while final_word != word and lives != 0:
        print(assets.STAGES[lives])
        print(f'\nWord: {final_word}')
        print(f'Guesses: {", ".join(guesses)}')
        guess = input('Guess a letter: ')

        if len(guess) != 1:
            print('Guesses should be one letter')
            helpers.clear()
            continue
        elif guess in word:
            for i, ch in enumerate(word):
                if guess == ch:
                    dashes[i] = ch

            final_word = ''.join(dashes)
        else:
            lives -= 1

        guesses.add(guess)
        helpers.clear()
    else:
        if lives == 0:
            print(assets.STAGES[lives])
            print('GAME OVER!', end=' ')
        else:
            print('YOU WIN!', end=' ')

        print(f'The word was {word}')


if __name__ == '__main__':
    main()
