
brailleToEng = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'O.OO..': 'f', 'OOOO..': 'g', '.OO...': 'h', '.OOO..': 'i', 'O..OO.': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': '', '.O.OOO': '', '......': ' ', 
    '.O.....': '1', '.O.O...': '2', '..O....': '3', '..OO...': '4', 
    '..O.O..': '5', '...O...': '6', '...OO..': '7', '...O.O.': '8', 
    '.OO....': '9', '.OOO...': '0',
}

# Map out the English to Braille conversion
engToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'O.OO..', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 
    '1': '.O.....', '2': '.O.O...', '3': '..O....', '4': '..OO...', 
    '5': '..O.O..', '6': '...O...', '7': '...OO..', '8': '...O.O.', 
    '9': '.OO....', '0': '.OOO...', 
}
def isBraille(string):
    #check if string only contains braille 'O' or '.'
    return all(s in 'O.' for s in string)

def engToBrailleConversion(string):
    result = ''  # create blank string to store conversion
    for char in string:
        if char.isupper():  # check if letter is capitalized
            result += '.....O'  # indicates capitalization
            char = char.lower()
        
        if char.isdigit():  # check if character is a digit
            result += '.O.OOO'  # add number indicator
        result += engToBraille.get(char, '')  # add Braille value of the letter

    return result

def brailleToEngConversion(string):
    result='' #create blank string to store conversion
    #split string into segments of 6 chars, since each Braille contains 6 chars
    brailleChars = [string[i:i+6] for i in range(0, len(string),6)] 
    isCapital =False

    for char in brailleChars:
        if char =='.....O': #check if capitalized
            isCapital= True
            continue
        if char == '.O.OOO': #check if number
            continue
        #retrieve the english value of the Braille character
        value = brailleToEng.get(char, '')
        if value:  # ensure value is not empty
            if isCapital:  # f previously marked as capital, convert to uppercase
                value = value.upper()
                isCapital = False  # reset capitalization flag
            result += value  # append the translated character
    
    return result

def translate(string):
    #check if string is Braille or english to use appropriate conversion function
    if isBraille(string):
        return brailleToEngConversion(string)
    else:
        return engToBrailleConversion(string)
    
if __name__ == '__main__':
    # for user input testing
    inputString= input("Please enter text to translate: ")
    outputString= translate(inputString)
    print(outputString)
    
    #Handle command line arguements
    # import sys
    # if len(sys.argv) > 1:
    #     input = " ".join(sys.argv[1:])
    #     output = translate(input)
    #     print(output)


