import random
hangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def loadWord():
    
    ''' Populate each list with at least 10 different items.  Create a variable called secretWord that is assigned a random word from one of the lists. 
    
    return a tuple in the following format:  (secretWord, list the secretWord is from)   
    
    Hint:  You will need to randomly choose one of the lists, and THEN choose a random word from that list.
    '''
    persons = ['mike', 'joe', 'fred', 'bob', 'jimmy', 'tom', 'john']
    places = ['Mexico', 'Publix', 'Walmart','Merica','China','Japan','Moon']
    things = ['Dogs', 'Cats','Mouse','Chair','Bannanas','Computer','Cord']
    listoflists = [persons, places, things]
    listoflistschoice =random.choice(listoflists)
    secretWord = random.choice(listoflistschoice)
    return secretWord

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE..
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
        
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    printedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            printedWord += letter + ' '
        else:
            printedWord += '_ '
    return printedWord
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
      
    '''
    
    availableLetters = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters
        
        
    
    

def hangman():
    '''
    secretWord: string, the secret wordgetAvailableLetters(['s','g','b','a'])
 to guess.

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
    # FILL IN YOUR CODE HERE...
    secretWord = loadWord()
    lettersGuessed = []
    wrongGuesses = 0
    secretWord = secretWord.lower()
    
    while wrongGuesses <= 6:
        print hangmanPics[(wrongGuesses)]
        if isWordGuessed(secretWord, lettersGuessed) == True:
            return "You Win! The Word was",secretWord,"!"
        else:
            print getAvailableLetters(lettersGuessed)
            print getGuessedWord(secretWord, lettersGuessed)
            guess = raw_input('Please pick A letter:     ')
            while guess not in getAvailableLetters(lettersGuessed):
                guess = raw_input('Please pick A LETTER that you havent guessed yet:       ')
            lettersGuessed.append(guess)                
            if guess not in secretWord:
                wrongGuesses += 1
                print "You were wrong!"
            else:
                print "You were right!"
            

           
            

    return "You Lose The Word was",secretWord,"!"


