def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = list('abcdefghijklmnopqrstuvwxyz')
    lettersClone = letters[:]
    for i in lettersClone:
        if i in lettersGuessed:
            letters.remove(i)
    return ''.join(letters)

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))