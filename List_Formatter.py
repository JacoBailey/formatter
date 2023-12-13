#LIST FORMAT MODE: Formats user data from clipboard

import Mods_Packs_Libs #Custom modules
import pyperclip
import pyinputplus as pyip

class ClipboardContentMissingDelimiter(Exception):
    'Exiting program due to delimiter missing from user\'s clipboard content. Please ensure copied clipboard content has at laeast one of the selected delimiters.'
    pass

def list_formatter():
    #Ask user where data should be added (before, after, or both) pyinput plus list
    formatLocation = pyip.inputMenu(['Prefix Input', 'Suffix Input', 'Prefix & Suffix Input'], prompt='Please select where to format each line:\n', numbered=True)
    
    #Ask user for delimiter (use a list of common delimiters and option for custom)
    delimiterDict = {'Newlines':'\n', 'Commas':',', 'Spaces':' ', 'Commas and Spaces':', ', 'Custom Delimiter':''}
    delimiterSelection = pyip.inputMenu(list(delimiterDict.keys()), prompt='Please select your list\'s delimiter:\n', numbered=True)
    if delimiterSelection == 'Custom Delimiter':
       delimiterDict['Custom Delimiter'] = str(Mods_Packs_Libs.input_correct_validation('Please enter your custom delimiter.', 'Custom Delimiter'))
    delimiterSelection = delimiterDict[delimiterSelection]
    
    #Ask user to provide inputs for formatting based on format location selection
    inputsDict = {}
    if formatLocation == 'Prefix Input' or formatLocation == 'Prefix & Suffix Input':
        inputsDict['Prefix Input'] = Mods_Packs_Libs.input_correct_validation('Please provide an input for Prefix Input', 'Prefix Input')
    if formatLocation == 'Suffix Input' or formatLocation == 'Prefix & Suffix Input':
        inputsDict['Suffix Input'] = Mods_Packs_Libs.input_correct_validation('Please provide an input for Suffix Input', 'Suffix Input')

    #Have user copy formatting to clipboard
    Mods_Packs_Libs.yes_to_continue('Please enter \'yes\' or \'y\' when you have copied the list to your clipboard.')
    
    #Take input and split values into a list based on user-provided delimiter
    clipboard = pyperclip.paste()
    if delimiterSelection not in clipboard:
        raise ClipboardContentMissingDelimiter
    listToFormat = clipboard.split(delimiterSelection)
    
    #Main list formatting loop
    for index in range(len(listToFormat)):
        #Strip empty spaces and characters from beginning and end of each value
        listToFormat[index] = listToFormat[index].strip()
        #Add prefix and/or suffix values to each item
        if formatLocation == 'Prefix Input' or formatLocation == 'Prefix & Suffix Input':
            listToFormat[index] = inputsDict['Prefix Input'] + listToFormat[index]
        if formatLocation == 'Suffix Input' or formatLocation == 'Prefix & Suffix Input':
            listToFormat[index] = listToFormat[index] + inputsDict['Suffix Input']
        continue

    #Join list into a string with selected delimiter and return it
    formattedList = delimiterSelection.join(listToFormat)
    return formattedList