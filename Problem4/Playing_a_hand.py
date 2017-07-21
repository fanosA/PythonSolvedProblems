r"""
Playing a Hand
15.0/15.0 points (graded)
In ps4a.py, note that in the function playHand, there is a bunch of pseudocode.
This pseudocode is provided to help guide you in writing your function.
Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.

Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.

Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. Here is some example output of playHand:
"""

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # Keep track of the total score
    totalScore = 0
    handed = hand.copy()
    # As long as there are still letters left in the hand:
    while True:
        if calculateHandlen(handed) == 0:
            print "Run out of letters. Total score: " + str(totalScore) + " points."
            break
        # Display the hand
        print "Current Hand:",
        displayHand(handed)
        # Ask user for input
        wordInput = raw_input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if wordInput == '.':
            # End the game (break out of the loop)
            print "Goodbye! Total score: " + str(totalScore) + " points."
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(wordInput, handed, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print "Invalid word, please try again.\n"
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                totalScore += getWordScore(wordInput, n)
                print '"'+ wordInput + '" ' + "earned " + str(getWordScore(wordInput, n)) + " points. Total: " + str(totalScore) + " points\n"
                # Update the hand
                handed = updateHand(handed, wordInput)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
