def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord = list(secretWord)
    match = False
    for letter in secretWord:
        for charecter in lettersGuessed:
            match = letter == charecter
            if match == True:
                break
        if match == False:
            return False
    return True





secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'a', 'l']
print(isWordGuessed(secretWord, lettersGuessed))