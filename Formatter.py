#! python3

import pyperclip, os, re
import pyinputplus as pyip
from pathlib import Path

inputRegex = re.compile(r'''(
                        (INSERT{1})
                        ((\s{1}[A-Z0-9]+)+)
                        )''', re.VERBOSE)

class NoInputsInTemplateFile(Exception):
    'Exiting program due to no inputs in template file. Please ensure the template file used has at least one input slot and that they are using correct syntax.'
    pass

class ClipboardContentMissingDelimiter(Exception):
    'Exiting program due to delimiter missing from user\'s clipboard content. Please ensure copied clipboard content has at laeast one of the selected delimiters.'
    pass

def yesToContinue(prompt):
    print(prompt)
    while True:
        response = pyip.inputYesNo()
        if response != 'yes':
            print('Answer other than \'yes\' provided.')
            continue
        else:
            break

def inputCorrectValidation(prompt, inputType):
    while True:
        print(prompt)
        userInput = input()
        print(f'You have entered \'{userInput}\' as {inputType}.\nIs this correct?')
        yesNo = pyip.inputYesNo()
        if yesNo == 'no':
            continue
        else:
            return userInput

def filewalk(directory): #TODO: Determine way to hide hidden filetypes such as .DS_Store
    for root, dirs, files in os.walk(directory):
        directoryFiles = files
    return directoryFiles

#TEMPLATE INPUT MODE
#Locate prompt input locations, have the user supply inputs, & fill in the prompt with the user-supplied inputs
def templateInputter():
    progDirectory = __file__.removesuffix(str(Path(__file__).name))
    templatesDirectory = os.path.join(Path(progDirectory), 'User_Templates')
    templatesList = filewalk(templatesDirectory)
    userSelectedTemplate_Name = pyip.inputMenu(templatesList, prompt='Please select a template file:\n', numbered=True)
    userSelectedTemplate_DirectoryLocation = os.path.join(Path(templatesDirectory), userSelectedTemplate_Name)
    userSelectedTemplate_Contents = Path(userSelectedTemplate_DirectoryLocation).read_text(encoding='utf8')
    templateInputSlots = inputRegex.findall(userSelectedTemplate_Contents)
    if templateInputSlots == None:
        raise NoInputsInTemplateFile
    userInputsDict = {}
    templateInputSlots == ['']
    for inputSlot in range(len(templateInputSlots)):
        fullInputSlot = templateInputSlots[inputSlot][0]
        inputSlotName = templateInputSlots[inputSlot][2]  
        userInput = inputCorrectValidation(f'Please enter an input for: {inputSlotName}.', inputSlotName)
        userInputsDict[inputSlotName] = userInput
        userSelectedTemplate_Contents = userSelectedTemplate_Contents.replace(fullInputSlot, userInput)
    return userSelectedTemplate_Contents

#LIST FORMAT MODE: Formats user data from clipboard
def listFormatter():
    #Ask user where data should be added (before, after, or both) pyinput plus list
    formatLocation = {'Before Each Line':'Prefix Input','After Each Line':'Suffix Input','Prefix & Suffix Input':['Prefix Input', 'Suffix Input']} #TODO: Update to list (don't need key values for prefix/suffix denotation)
    formatLocation_UserSelection = pyip.inputMenu(list(formatLocation.keys()), prompt='Please select where to format each line:\n', numbered=True)
    #Ask user for delimiter (use a list of common delimiters and option for custom)
    delimiterDict = {'Newlines':'\n', 'Commas':',', 'Spaces':' ', 'Commas and Spaces':', ', 'Custom Delimiter':''}
    delimiterSelection = pyip.inputMenu(list(delimiterDict.keys()), prompt='Please select your list\'s delimiter:\n', numbered=True)
    if delimiterSelection == 'Custom Delimiter':
       delimiterSelection = str(inputCorrectValidation('Please enter your custom delimiter.', 'Custom Delimiter'))
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
    yesToContinue('Please enter \'yes\' or \'y\' when you have copied the list to your clipboard.')
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


#!! MODULE IN PROGRESS !!
#REGEX REPLACEMENT MODE
'''def regexReplace(): #TODO: Figure out best method of implementation
    #Have user enter regex pattern and handle invalid regex pattern AND blank entries
    while True: #TODO: Determine how to use raw regex strings with user inputs
        pattern = inputCorrectValidation('Please enter a regex match pattern. [Only first group will matched]', 'Regex Match Pattern')
        try:
            regex = re.compile(pattern)
            break
        except re.error:
            print('Please enter a valid regex pattern.')
            continue
    #Have user enter replacment for regex
    regexReplacement = inputCorrectValidation('What should we replace found regex matches with?','Regex Match Replacement')
    #Request user to ensure their content for regex replacement is saved to their clipboard, then confirm with pyinputplus yes/no
    yesToContinue('Please respond \'yes\' or \'y\' when you have copied the text you would like to regex search to your clipboard.')
    #Replace regex matches
    clipboard = pyperclip.paste()
    replacementSlots = regex.findall(clipboard) #TODO Fix this
    
    replacementSlots[0]
    
    
    for slot in range(replacementSlots):
        userClipboardPrompt = userClipboardPrompt.replace(slot, regexReplacement)
    #Return replaced string
    return userClipboardPrompt'''



#Print a fun formatter tool message to screen
print('- - - - - - - - - - -\n- - - FORMATTER - - -\n- - - - - - - - - - -')
#Have user select mode, execute selection mode function, and save to variable
modeDictionary = {'List Formatter':listFormatter,'Template Inputter':templateInputter}#,'Regex Replacement':regexReplace} - TODO: Replace when Regex module is activated
listSelection = pyip.inputMenu(list(modeDictionary.keys()), prompt='Select formatter mode:\n', numbered=True)
returnValue = modeDictionary[listSelection]()
#Print and copy formatter return to clipboard
pyperclip.copy(returnValue)
print(f'\n--------------------------\n\n{returnValue}\n\n--------------------------\n\n Copied to clipboard.\n')