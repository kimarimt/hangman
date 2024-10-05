def main():
    word = 'hello'
    dashes = ['_' for _ in word]
    guesses = set()
    lives = 6
    final_word = ''.join(dashes)

    while final_word != word and lives > 0:
        print(f'Word: {final_word}')
        print(f'Guesses: {", ".join(guesses)}')
        guess = input('Guess a letter: ')

        if len(guess) != 1:
            print('Guesses should be one letter')
            continue
        elif guess in word:
            for i, ch in enumerate(word):
                if guess == ch:
                    dashes[i] = ch

            final_word = ''.join(dashes)
        else:
            lives -= 1

        guesses.add(guess)
    else:
        if lives == 0:
            print('GAME OVER!', end=' ')
        else:
            print('YOU WIN!', end=' ')

        print(f'The word was {word}')


if __name__ == '__main__':
    main()
