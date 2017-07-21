r"""
Computer Plays a Hand
10.0/10.0 points (graded)
Now that we have the ability to let the computer choose a word, we need to set up a function to allow the computer to play a hand -
in a manner very similar to Part A's playHand function (get the hint?).

Implement the compPlayHand function. This function should allow the computer to play a given hand, using the procedure you just wrote in the previous part.
This should be very similar to the earlier version in which a user selected the word, although deciding when it is done playing a particular hand will be different.

Be sure to test your function on some randomly generated hands using dealHand.
"""

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)
    bestWord = 'None'
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            # If the score for that word is higher than your best score
            if getWordScore(word, n) > maxScore:
                # Update your best score, and best word accordingly
                maxScore = getWordScore(word, n)
                bestWord = word
    # return the best word you found.
    return bestWord

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalScore = 0
    word = ''
    while True:
        word = compChooseWord(hand, wordList, n)
        if word == 'None':
            break
        print "Current Hand:" ,
        displayHand(hand)
        totalScore += getWordScore(word, n)
        print '"'+ word + '" ' + "earned " + str(getWordScore(word, n)) + " points. Total: " + str(totalScore) + " points\n"
        hand = updateHand(hand, word)
    if calculateHandlen(hand):
        print "Current Hand:" ,
        displayHand(hand)
    print "Total: " + str(totalScore) + " points\n"
    
