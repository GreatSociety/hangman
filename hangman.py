import random

print("H A N G M A N")

flag = 1

while flag:

    answer = input('Type "play" to play the game, "exit" to quit:\n')

    if answer == 'exit':
        flag = 0
        continue
    elif answer != 'play':
        print(answer)
        continue

    random.seed()
    words = 'python', 'java', 'kotlin', 'javascript'
    word = random.choice(words)
    word_to_guess = list('-' * len(word))
    counter = 0
    verification = set()

    while counter < 8:
        print(''.join(word_to_guess))
        letter_out = input('Input a letter:')

        if len(letter_out) > 1 or letter_out == '':
            print("You should input a single letter\n")
            continue

        if not letter_out.isalpha() or letter_out.isupper():
            print("Please enter a lowercase English letter\n")
            continue

        if letter_out in verification:
            print("You've already guessed this letter\n")
            continue

        verification.add(letter_out)

        if letter_out in set(word):

            if letter_out not in set(word_to_guess):
                for num in range(len(word_to_guess)):
                    if word[num] == letter_out:
                        word_to_guess[num] = letter_out

        else:
            print("That letter doesn't appear in the word")
            counter += 1

        if '-' not in set(word_to_guess):
            guessed_word = (''.join(word_to_guess))
            print(f"You guessed the word {guessed_word}!\nYou survived!")
            break

        if counter < 8:
            print('\n')

    else:
        print("You lost!")

    print('\n')