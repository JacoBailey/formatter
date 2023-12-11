#LIST FORMAT MODE: Formats user data from clipboard

import ModsPacksLibs #Custom modules
import pyperclip
import pyinputplus as pyip

class ClipboardContentMissingDelimiter(Exception):
    'Exiting program due to delimiter missing from user\'s clipboard content. Please ensure copied clipboard content has at laeast one of the selected delimiters.'
    pass

def listFormatter():
    #Ask user where data should be added (before, after, or both) pyinput plus list
    formatLocation = {'Before Each Line':'Prefix Input','After Each Line':'Suffix Input','Prefix & Suffix Input':['Prefix Input', 'Suffix Input']} #TODO: Update to list (don't need key values for prefix/suffix denotation)
    formatLocation_UserSelection = pyip.inputMenu(list(formatLocation.keys()), prompt='Please select where to format each line:\n', numbered=True)
    #Ask user for delimiter (use a list of common delimiters and option for custom)
    delimiterDict = {'Newlines':'\n', 'Commas':',', 'Spaces':' ', 'Commas and Spaces':', ', 'Custom Delimiter':''}
    delimiterSelection = pyip.inputMenu(list(delimiterDict.keys()), prompt='Please select your list\'s delimiter:\n', numbered=True)
    if delimiterSelection == 'Custom Delimiter':
       delimiterSelection = str(ModsPacksLibs.inputCorrectValidation('Please enter your custom delimiter.', 'Custom Delimiter'))
    else:
        delimiterSelection = delimiterDict[delimiterSelection]
    #Ask user to provide inputs for formatting based on format location selection
    inputsDict = {}
    inputLocation = formatLocation[formatLocation_UserSelection]
    if type(formatLocation[formatLocation_UserSelection]) == list:
        for inputLocIndex in range(len(formatLocation[formatLocation_UserSelection])):
            print(f'Please provide an input for: {formatLocation[formatLocation_UserSelection][inputLocIndex]}')
            inputLocation = formatLocation[formatLocation_UserSelection][inputLocIndex]
            inputsDict[inputLocation] = input()
    else:
        print(f'Please provide an input for: {formatLocation[formatLocation_UserSelection]}')
        inputsDict[inputLocation] = input()
    #Pause then request user to ensure their content is saved to their clipboard, then confirm with pyinputplus yes/no
    ModsPacksLibs.yesToContinue('Please enter \'yes\' or \'y\' when you have copied the list to your clipboard.')
    #Take input and split values into a list based on user-provided delimiter
    clipboard = pyperclip.paste()
    if delimiterSelection not in clipboard:
        raise ClipboardContentMissingDelimiter
    listToFormat = clipboard.split(delimiterSelection)
    #Strip empty spaces and characters from beginning and end of each value AND add inputs to front/end of each index in user's list
    for index in range(len(listToFormat)):
        listToFormat[index] = listToFormat[index].strip()
    #Using a looped function, concat values to front/back of each item and add them back to the list
        if 'Prefix Input' in inputsDict.keys():
            listToFormat[index] = inputsDict['Prefix Input'] + listToFormat[index]
        elif 'Suffix Input' in inputsDict.keys():
            listToFormat[index] = listToFormat[index] + inputsDict['Suffix Input']
        continue
    #Combine list into a string with selected delimiter and return it
    formattedList = delimiterSelection.join(listToFormat)
    return formattedList