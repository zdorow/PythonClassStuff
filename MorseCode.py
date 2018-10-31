#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author:  Wun Her
#     Teacher:  Mr. Kevin Kurek
#     Last Edited:  Oct 27,   2018
#
#     Description:  The program function is to convert string to morse code.
#
#######################################################################################

def main(): 

    # Setting up the dictionary for the morse code translation.
    morseCode = {" ":  " ", '':  '--..--',  '.':  '.-.-.-',  '?':  '..--..',
                 '0': '-----', '1': '.----', '2': '..--', '3': '...--',
                 '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                 '8': '---..', '9': '----.', 'A': '.-', 'B': '-...', 'C': '-.-.', 
                 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 
                 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
                 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 
                 'X': '-..-', 'Y': '-.-', 'Z': '--..'}

    # Getting the input from the user.
    userString = str(input('Enter a string: '))

    # Printing out what the user has put in.
    print('\nUser Input: ' + userString)

    # Converting it all to upper case to reference the dictionary.
    userString = userString.upper()

    # Printing the output.
    print('\nMorse Code: ')

    # Looping to go through the users characters.
    for character in userString: 
        print(character)
        if character in morseCode: 
            print(morseCode[character])

    # Triple for loops to get the matches the two dimensional array.
        # for row in range(len(morseCode)): 
        #     for col in range(len(morseCoderow)): 
        #         if morseCoderowcol == character: 
        #             print(morseCoderow1)

    input('\n\n  Press Any Key to Exit... \n\n')

main()
