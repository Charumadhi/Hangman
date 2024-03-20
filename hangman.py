import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_status = "-" * len(word)   #put hyphen in all places of the word
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    
    name = input("What is your name? ")
    print("Welcome to Hangman, " + name + "!")
    print(display_hangman(tries))
    print(word_status)
    print("")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()
        
        if len(guess)  == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter {}. Try again".format(guess))
            elif guess not in word:
                print("{} is not in the word.".format(guess))
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nicely done! {} is in the word!".format(guess))
                guessed_letters.append(guess)

                word_as_list = list(word_status)    
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess 
                word_status = "".join(word_as_list)

                if "-"  not in word_status:
                    guessed = True   

        elif len(guess)  == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed the word {}. Try again".format(guess))
            elif guess != word:
                print(guess + "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:     
                guessed = True
                word_status = word
        else:
            print("Not a valid guess") 

        print(display_hangman(tries))
        print(word_status)
        print("")

    if guessed:
        print("Congratulations! You guessed the word! You win!")
    else:
        print(display_hangman(0))
        print("")
        print("Sorry, you ran out of tries. The word was " + word + ". Better luck next time!")                 


def display_hangman(tries):
    #states = ['Image 6', 'Image 5', 'Image 4', 'Image 3', 'Image 2', 'Image 1', 'Initial image']
    states = [
        '''
            -------------
            |         |
            |         0
            |       \\\|//
            |         |
            |        / \\
            -------------
        ''' ,
        '''
            -----------   
            |          |
            |          0
            |        \\\|//
            |          |
            |         / 
            -----------
        ''' ,  
        '''
            -----------   
            |          |
            |          0
            |        \\\|//
            |          |
            |          
            -----------
        ''' ,           
        '''
            -----------   
            |          |
            |          0
            |        \\\|
            |          |
            |          
            -----------
        ''' ,  
        '''
            -----------   
            |          |
            |          0
            |          |
            |          |
            |          
            -----------
        ''' ,   
        '''
            -----------   
            |          |
            |          0
            |          
            |          
            |          
            -----------
        ''' ,
        '''
            -----------   
            |         |
            |          
            |          
            |          
            |          
            -----------
        '''          
    ]
    return states[tries] 


def play_again():
    replay = input("Play again? (Y/N) ").lower()
    if replay == 'y':
        return True
    else:
        return False    

def main():
    while True:
        word = get_word()
        play(word)
        if not play_again():
            print("Hope to see you soon!")
            break

main()