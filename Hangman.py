import random

EASY_WORDS_DIR = './WORDS/EASY_WORDS_LIST.txt'
MEDIUM_WORDS_DIR = './WORDS/MEDIUM_WORDS_LIST.txt'
HARD_WORDS_DIR = './WORDS/HARD_WORDS_LIST.txt'

EASY_WORDS_LIST = []
MEDIUM_WORDS_LIST = []
HARD_WORDS_LIST = []

Gallows = 0

pickedWordList = []

invertedDisplayWord = []

displayWord = []

alreadyGuessed = []

LOGO = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |
                   |___/
'''

GAME_STARTING = '''
 _   _                                         _
| | | |                                       (_)
| |_| |__   ___    __ _  __ _ _ __ ___   ___   _ ___
| __| '_ \\ / _ \\  / _` |/ _` | '_ ` _ \\ / _ \\ | / __|
| |_| | | |  __/ | (_| | (_| | | | | | |  __/ | \\__ \\
 \\__|_| |_|\\___|  \\__, |\\__,_|_| |_| |_|\\___| |_|___/
                   __/ |
                  |___/
     _             _   _
    | |           | | (_)
 ___| |_ __ _ _ __| |_ _ _ __   __ _
/ __| __/ _` | '__| __| | '_ \\ / _` |
\\__ \\ || (_| | |  | |_| | | | | (_| |  _   _   _
|___/\\__\\__,_|_|   \\__|_|_| |_|\\__, | (_) (_) (_)
                                __/ |
                               |___/
'''
GAME_OVER = '''

  __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
 / _` |/ _` | '_ ` _ \\ / _ \\  / _ \\ \\ / / _ \\ '__|
| (_| | (_| | | | | | |  __/ | (_) \\ V /  __/ |   
 \\__, |\\__,_|_| |_| |_|\\___|  \\___/ \\_/ \\___|_|   
  __/ |                                           
 |___/

 '''
WELL_DONE = '''
              _ _       _                  
             | | |     | |                 
__      _____| | |   __| | ___  _ __   ___ 
\\ \\ /\\ / / _ \\ | |  / _` |/ _ \\| '_ \\ / _ \\
 \\ V  V /  __/ | | | (_| | (_) | | | |  __/
  \\_/\\_/ \\___|_|_|  \\__,_|\\___/|_| |_|\\___|
'''
HANGMAN_NOOSE = ['''






         ''', '''




=========''', '''
      |
      |
      |
      |
      |
      |\\
=========''', '''
  ----+
      |
      |
      |
      |
      |\\
=========''', '''
  +---+
  |   |
      |
      |
      |
      |\\
=========''', '''
  +---+
  |   |
  0   |
      |
      |
      |\\
=========''', '''
  +---+
  |   |
  0   |
  |   |
      |
      |\\
=========''', '''
  +---+
  |   |
  0   |
 /|   |
      |
      |\\
=========''', '''
  +---+
  |   |
  0   |
 /|\\  |
      |
      |\\
=========''', '''
  +---+
  |   |
  0   |
 /|\\  |
 /    |
      |\\
=========''', '''
  +---+
  |   |
  0   |
 /|\\  |
 / \\  |
      |\\
========='''
                 ]

def InitialiseLists():
    with open(EASY_WORDS_DIR, 'r') as EASY_WORDS:
        for line in EASY_WORDS:
            EASY_WORDS_LIST.append(line)
    with open(MEDIUM_WORDS_DIR, 'r') as MEDIUM_WORDS:
        for line in MEDIUM_WORDS:
            MEDIUM_WORDS_LIST.append(line)
    with open(HARD_WORDS_DIR, 'r') as HARD_WORDS:
        for line in HARD_WORDS:
            HARD_WORDS_LIST.append(line)


def CheckGuess(guess):
    global displayWord
    global chosenWord
    global Gallows
    while guess in invertedDisplayWord:
            index = invertedDisplayWord.index(guess)
            invertedDisplayWord.pop(index)
            invertedDisplayWord.insert(index, '_')
            displayWord = displayWord[:index] + displayWord[index+1:]
            displayWord.insert(index, guess)

    if guess not in chosenWord:
        alreadyGuessed.append(guess)
        print('\n\t\tIncorrect Guess\n')
        Gallows += 1


def WordPicker(gamestyle):
    global invertedDisplayWord
    confirmed = False
    if gamestyle == 'EASY':
        pickedWord = random.choice(EASY_WORDS_LIST)
    elif gamestyle == 'MEDIUM':
        pickedWord = random.choice(MEDIUM_WORDS_LIST)
    elif gamestyle == 'HARD':
        pickedWord = random.choice(HARD_WORDS_LIST)
    elif gamestyle == 'CUSTOM_WORD':

        pickedWord = input('\nPlease enter a word. It cannot contain spaces, special characters or numbers: ')
        while not all(x.isalpha() for x in pickedWord):
            pickedWord = input(
                'The word cannot contain spaces, numbers or special characters. Please enter a different word')
        print('Your word is valid')
        while not confirmed:
            print(' Are you sure that you want to use ', pickedWord, ' as your word? [Y/n]')
            confirmEntry = input()
            if confirmEntry == 'y':
                confirmed = True
            elif confirmEntry == '':
                confirmed = True
            elif confirmEntry == 'n':
                print('Word not confirmed. Taking you back to the Main menu.')
                main()
    else:
        raise Exception('Sorry, an internal error occured :( Please try running the program again.')

    pickedWordList = []
    for Char in pickedWord:
        if Char.isalpha():
            pickedWordList.append(Char)
            invertedDisplayWord.append(Char)
            displayWord.append('_')
        else:
            print(Char)
    return pickedWordList


def GetGuess(alreadyguessed):
    while True:
        print('\nEnter a single letter ')
        guess = input().lower()
        if len(guess) != 1:
            print('\nPlease enter a SINGLE LETTER only ')
        elif guess in alreadyguessed:
            print('\nYou have already guessed that letter. Please choose again.')
        elif guess in displayWord:
            print('\nYou have already guessed that letter. Please choose again.')
        elif not all(x.isalpha() for x in guess):
            print('Please enter a LETTER only.')
        else:
            return guess


def main():
    global chosenWord
    print(LOGO)
    validChoice = False
    print(
        '\n\nPlease choose an option from the list: \n\n1 – Get an easy word \n2 – Get a medium word \n3 – Get a hard word \n4 – Enter in your own word\n')
    while not validChoice:
        # try:
        Choice = input()
        if Choice == '1':
            chosenWord = WordPicker('EASY')
            validChoice = True
        elif Choice == '2':
            chosenWord = WordPicker('MEDIUM')
            validChoice = True
        elif Choice == '3':
            chosenWord = WordPicker('HARD')
            validChoice = True
        elif Choice == '4':
            chosenWord = WordPicker('CUSTOM_WORD')
            validChoice = True
        else:
            print('Please enter a valid choice:\n')
            # except:
            # print('Sorry, an error occured. Restarting main loop...')
            # Main()
    while displayWord != chosenWord:
        if Gallows != 10:
            print(' '.join(alreadyGuessed))
            print('\t\t\t', HANGMAN_NOOSE[Gallows])
            print('\n\n', ' '.join(displayWord))
            guess = GetGuess(alreadyGuessed)
            CheckGuess(guess)
        else:
            print(GAME_OVER)
            print('\n\nYou lost :(\n\nThe word was ', ''.join(chosenWord),'\n\nBetter luck next time!')
            break

    if displayWord == chosenWord:
        print(WELL_DONE)
        print('\n\nYou won!\n\nThe word was ', ''.join(chosenWord),'\n You lost ',Gallows,' Lives')
        print('\nThank you for playing!')

InitialiseLists()
main()