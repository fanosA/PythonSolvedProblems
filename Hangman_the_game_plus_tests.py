r"""
Hangman Part 2: The Game/Complex Tests
15.0/15.0 points (graded)
Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess.
This starts up an interactive game of Hangman between the user and the computer.
Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one.
Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player guesses a letter,
the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters,
you should print a message telling them they've already guessed that - so try again!).
"""

def update_result(hidden_word, result, guess):
    new_result = str()
    for i in xrange(len(result)):
        if hidden_word[i] == guess:
            new_result += guess
        else:
            new_result += result[i]
    return new_result

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = ''
    result = '_'*len(secretWord)
    mistakesMade = 0
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'
    print '------------'
    while mistakesMade != 8 and result != secretWord:
        print 'You have ' + str(8 - mistakesMade) + ' guesses left'
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print '------------'
        elif guess in secretWord:
            result = update_result(secretWord, result, guess)
            lettersGuessed += guess
            print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
            print '------------'
        else:
            lettersGuessed += guess
            print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
            print '------------'
            mistakesMade += 1
    if result == secretWord:
        print 'Congratulations, you won!'
    elif mistakesMade == 8:
        print 'Sorry, you ran out of guesses. The word was ' + secretWord +'.'
