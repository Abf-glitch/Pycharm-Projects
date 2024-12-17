
letter = input("Enter a letter: ")


if len(letter) == 1 and letter.isalpha():

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # Check if the letter is in the set of vowels
    if letter in vowels:
        print("The letter '" + letter + "' is a vowel.")
    else:
        print("The letter '" + letter + "' is a consonant.")
else:
    print("Please enter a single alphabet letter.")
