
#AUTHOR : ALEX YAMASAKI

#IMPORTED LIBARRIES
import random
import time


#GLOBAL VARIABLES
jap_hiragana_dict = {
    "vowels": {
        'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    },
    "k-row": {
        'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    },
    "s-row": {
        'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    },
    "t-row": {
        'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    },
    "n-row": {
        'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    },
    "h-row": {
        'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    },
    "m-row": {
        'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    },
    "y-row": {
        'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    },
    "r-row": {
        'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    },
    "w-row": {
        'わ': 'wa', 'を': 'wo',
    },
    "n": {
        'ん': 'n',
    },
    "dakuten": {
        'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
        'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
        'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do',
        'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
    },
    "handakuten": {
        'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
    },
    "small": {
        'ゃ': 'ya', 'ゅ': 'yu', 'ょ': 'yo',
        'ぁ': 'a', 'ぃ': 'i', 'ぅ': 'u', 'ぇ': 'e', 'ぉ': 'o',
        'っ': 'tsu',  # small tsu for geminate consonants (っk, っt, etc.)
    },
}
#Dictionary that will allow the user to save their study values

user_mode_select = {
    'hiragana_mode' :[],

    'katakana_mode' :[]
}
user_select_length = 0
#FUNCTIONS
#Function displayWelcomeScreen
#Purpose:  A void function that will display a welcoming message
#Function parameters: None
#Return Statement: Void/None
def displayWelcomeScreen():
    print('='*50)
    print('\t\t    Welcome\n\t\tto the Japanese\n\t\tLearning Program')
    print('Created by: Alyamas')
    print('='*50)


#Function: checkUserInputMode
#Purpose:  To check and see the input of the user mode selection is correct
#Function parameters: user_input - a variable that would check the user input
#Return statement: True/False, depending on the user input by conditional statement
def checkUserInputMode(user_input):
    if user_input == '1' or user_input == '2':
        return True
    print('ERROR: Please select either of the modes\n')
    return False

#Function: userSelect_chars
#Purpose:  To check and see if the user wanted to select which row shall be add to the study
#Function parameters: user_input - the row they want to select
#                     mode       - depending on if its hiragana or katakana, preset variable
#Return statement: True/False based on the Row selection of the dictionary.
def userSelect_chars(user_input, dict, mode = 0):
    if user_input == 'done':
        return True
    i = 0
     
    for i, keys in enumerate(dict):
        if user_input == str(i+1):
            if not(checkDuplicatedSelection(user_mode_select, user_input, 1 )):
                return False
            #Conditional statement
            #to check and to see user hiragana/katakana mode
            #if mode is 1, then its hiragana
            #if mode is 2, then its katakana
            if(mode == 1):
                user_mode_select['hiragana_mode'].append(i)
                
            elif(mode == 2):
                user_mode_select['katakana_mode'].append(i)

            print('Row has been added!\n')
            return False
    
    print('ERROR: Please select which row or type done to start.\n')
    return False

#Function: checkDuplicatedSelection
#Purpose: To check and see if the user has already selected the row
#Function parameters: diction - dictionary of array of user mode selection
#                     user_input - self explainatory
#                     mode - hiragana/katakana mode selected
#Return statement: Boolean Type
def checkDuplicatedSelection(diction, user_input, mode = 0 ):
    mode_select = 'hiragana_mode'
    if mode == 2:
        mode_select = 'katakana_mode'
    for item in diction[mode_select]:
        if str(item+1) == user_input:
            print('ERROR: You\'ve already selected the character.\n')
            return False
    return True
    

#Function: display_chars
#Purpose:  To display the vowls of the japanese characters
#Function parameters: jap_dict a dictionary where it loops over the keys.
#Return statement: Void/none
def display_chars(jap_dict = 0):
    i = 1
    for keys in jap_dict:
        print('{})\t'.format(i) + keys)
        i+=1

#Function: userSelect_amnt
#Purpose:  To check user-input whether they have typed values between 5 - 20 or custom
#Function parameters:  user_input - a string datatype to check userinput
#Return statement:  Boolean Type
def userSelect_amnt(user_input):
    if user_input == '1' or user_input == '2' or user_input == '3' or user_input == '4':
        return True
    
    print('ERROR: Please re-enter the amount of questions.\n')
    return False

#Function: startGame
#Purpose: To run the application/quiz game
#Function parameters: user_input_val - A counter value
#                     mode - to select katakana or hiragana mode
#Return statements:   None/void
def startGame(user_input_val, user_mode_select, mode = 0):
    mode_select = 'hiragana_mode'
    dictionary_mode = jap_hiragana_dict
    if mode == 2:
        mode_select = 'katakana_mode'
    #print(random.choice(user_mode_select[mode_select]))
    while user_input_val > 0:    
        #Based on user select, randomize
        randomChoice_charRow = random.randint(0, len(user_mode_select)-1)
        #Convert the dictionary keys to a list
        keys_list = list(dictionary_mode.keys())
        #Get the index value
        chosen_key = keys_list[randomChoice_charRow]
        #Based on the index value (word), you can access that row
        dict_mode = jap_hiragana_dict[chosen_key]
        #Convert that row specifically 
        r = list(dict_mode.items())
        
        randomChoice_char = random.randint(0, len(r)-1)
        key, value = r[randomChoice_char]
        #print(key)
        #print(value)
        userchar_input = input('what is this character {}: '.format(key))
        userchar_input = userchar_input.lower()
        if userchar_input == value:
            print('correct!')
        else:
            print('incorrect')
        user_input_val -= 1

#Function: setUserInput
#Purpose: Based on the user_input, return the value. Its a setter function
#Function parameters: user_input_val - a variable that will check the value by 
#                                       using equal operator
#Return Statement: Integer
def setUserInput(user_input_val):
    if user_input_val == '1':
        return 5
    elif user_input_val == '2':
        return 10
    elif user_input_val == '3':
        return 15
    elif user_input_val == '4':
        return 20

def hiragana_mode():
    print('Selected Hiragana...')
    print('Enter which rows to be added along to the quiz!')
    
    display_chars(jap_hiragana_dict)
    user_input = 0
    flag = False
    #whie loop until the user has typed 'done'
    while(not(flag)):
        user_input = input('Select which Rows to be added to your study: ')
        if((userSelect_chars(user_input, jap_hiragana_dict, 1))):
            flag = True
    print('\n')
    #re-use the flag variable
    flag = False
    while(not(flag)):
        print('Select the amount of questions.\n1)\t5\n2)\t10\n3)\t15\n4)\t20\n5)\tCustom')
        user_input = input('')
        if(userSelect_amnt(user_input)):
            user_input = setUserInput(user_input)
            flag = True
    print('\n')
        
    #if we pass the input statements, store the length towards the user Input
    #then start game.
    user_select_length = int(user_input)
    startGame(user_select_length, user_mode_select, mode=1)
    
    

def katakana_mode():
    pass

#Function: Main
#Purpose: The main program/application when called.
def main():
    displayWelcomeScreen()
    time.sleep(0.5)
    print('\n'*20) 
    #Create a boolean, could be False or 0.
    user_select = 0
    #This is a loop where user can allow input for the mode
    #The function checks to see if the user input is sucessfull or not  
    flag = False
    while(not(flag)):
        flag = False
        print('Select which mode you want to practice')
        print('1. Hiragana')
        print('2. Katakana')
        user_select = input('')
        if ((checkUserInputMode(user_select))):
            flag = True
    #we assume the input works, so continue on with the mode section
    print('\n'*2)
    if user_select == '1':
        hiragana_mode()
    elif user_select == '2':
        katakana_mode()
    
#MAIN PROGRAM
if __name__ == '__main__':
    main()