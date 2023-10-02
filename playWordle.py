
import random

infile = open("outputLength4.txt", "r")
allText = infile.read()
words = list(allText.split('\n'))
infile.close()


def getWord():    ##choosing a random word
    word = random.choice(words)
    return word.upper()



def play(word):
    wordCompletion = "_"*len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 10
##    counters = {}
    print(wordCompletion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please, guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word. You lost a life.")
                tries -= 1
                guessedLetters.append(guess)
            else:
                print("Good job! ", guess, " is the word.")
                guessedLetters.append(guess)
                wordAsList = list(wordCompletion)
                wordListt = list(word)
##                for i in wordListt:
##                    if i not in counters:
##                        counters[i]=1
##                    else:
##                        counters[i] += 1                        
                indices = [i for i, letter in enumerate(word) if letter == guess]   ##attributing an index to each value in the list
                for i in indices:
                    wordAsList[i] = guess
                wordCompletion = "".join(wordAsList)
                if "_" not in wordCompletion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print("You already guessed the word.", guess)
            elif guess != word:
                print(guess, "is not in the word. You lost a life.")
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordCompletion = word
                
                

        else:
            print("Invalid guess")
            tries -= 1

        print("You have ",tries,"tries left.")
        print(wordCompletion)
        print("\n")

    if guessed == True:
        print("Congratulations!")
    else:
        print("Sorry, you ran out of tries. The word was ", word)




def main():
    word = getWord()
    play(word)
    while input("Play again? Y or N").upper() == "Y":
        word = getWord()
        play(word)

main()
