#Part of Pig latin program

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
        #test

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