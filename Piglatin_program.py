from datetime import date, time

#Creating a date object
d1 = date.today()

#Creating a time object
t1 = time(12,30,00)

print("Welcome to Pig Latin!")

def main():

    word = input('Enter a word: ').upper()
    # Defining vowels and consonants
    consonant = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'Y', 'V', 'X', 'Z')
    vowel = ('A', 'E', 'I', 'O', 'U')

    # getting first letter
    first = word[0]
    rest = word[1:]

    # if first letter is a consonant
    if first in consonant:
        result = rest + "-" + first + "ay"
        PigLatin = result
        print('The world in PigLatin is:', PigLatin.lower(),".", d1, t1)

    # if first letter is a vowel
    elif first in vowel:
        result = word + "-" + "way"
        PigLatin = result
        print('The world in PigLatin is:', PigLatin.lower(),".", d1, t1)

    # If first letter is neither a vowel nor a consonant
    else:
        print("I don't know what first letter is",".", d1, t1)

    # Restarting the program if the user wants to translate another word
    restart = input("Write 'yes' if you wish to translate another word: ").lower()
    if restart == 'yes':
        main()
    else:
        print("Thank you for using PigLatin translator")
        exit()

main()