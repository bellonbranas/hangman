
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    a=[]
    b=0
    for e in lettersGuessed:
        if e not in a:
            a.append(e)
    for i in range(len(secretWord)):
        if secretWord[i] in a:
            b+=1
    if b==len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    a=''
    for i in range(len(secretWord)):
        a+='_'
    a=list(a)
    for j in range(len(secretWord)):
        if secretWord[j] in lettersGuessed:
            a[j]=secretWord[j]
    str1 = ''.join(a)
    return str1


def getAvailableLetters(lettersGuessed):
    alfabeto=string.ascii_lowercase
    letras = ''.join(lettersGuessed)
    for e in letras:
            alfabeto=alfabeto.replace(e, '')
            
    return alfabeto
    

def hangman(secretWord):
    print('Welcome to the game Hangman')
    print('I\'m thinking of a word that is',str(len(secretWord)),'letters long')
    lettersGuessed=[]
    i=0
    while i <8:
        print('-----------')
        print('You have',str(8-i),'guesses left')
        print('Available Letters:',getAvailableLetters(lettersGuessed))
        guess=input('Please guess a letter:')
        guesslower=guess.lower()
        if guesslower in secretWord:
            if guesslower in lettersGuessed:
                print('Oops! You\'ve already guessed that letter:',getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guesslower)
                print('Good guess:',getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed)==True:
                    print('-----------')
                    return print('Congratulations you won!')
       
        elif guesslower not in secretWord:
            if guesslower in lettersGuessed:
                print('Oops! You\'ve already guessed that letter:',getGuessedWord(secretWord, lettersGuessed))
            else:
                i+=1
                lettersGuessed.append(guesslower)
                print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))
    print('-----------')
    return print('Sorry, you ran out of guesses. The word was', secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)