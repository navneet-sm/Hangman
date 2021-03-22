import random
words_list = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N')
random_word = random.choice(words_list)
uncovered_str = '-' * len(random_word)    # sample
rw_list = list(random_word)        # converting random word into a list
uncovered_list = list(uncovered_str)
indices = []
guessed = []
i = 1
menu = input('Type "play" to play the game, "exit" to quit:')
if menu == 'play':
    while i <= 8:
        print('\n' + uncovered_str)
        x = input('Input a letter:')
        guessed.append(x)
        if (uncovered_str == random_word):
            print("""You guessed the word!
        You survived!""")
            break
        elif len(x) != 1:
            print("You should input a single letter .\n")
        elif x.islower() is False:
            print("Please enter a lowercase English letter .\n")
        elif guessed.count(x) > 1:
            print("You've already guessed this letter\n")
        elif x not in random_word:
            print("That letter doesn't appear in the word")
            i += 1
        elif x in random_word:
            for j in range(len(random_word)):
                if rw_list[j] == x:
                    indices.append(j)
                for k in range(len(indices)):
                    uncovered_list[indices[k]] = x
                    uncovered_str = ''.join(map(str, uncovered_list))
            indices = []
    else:
        print('You lost!')
elif menu == 'exit':
    quit()