#! python3

import ModsPacksLibs #Custom Modules
import pyperclip
import pyinputplus as pyip

#Print a fun formatter tool message to screen
print('- - - - - - - - - - -\n- - - FORMATTER - - -\n- - - - - - - - - - -')
#Have user select mode, execute selection mode function, and save to variable
modeDictionary = {'List Formatter':ModsPacksLibs.listFormatter,'Template Inputter':ModsPacksLibs.templateInputter, 'Regex Replacement':ModsPacksLibs.regexReplacement}#,'Regex Replacement':regexReplace} - TODO: Replace when Regex module is activated
listSelection = pyip.inputMenu(list(modeDictionary.keys()), prompt='Select formatter mode:\n', numbered=True)
returnValue = modeDictionary[listSelection]()
#Print and copy formatter return to clipboard
pyperclip.copy(returnValue)
print(f'\n--------------------------\n\n{returnValue}\n\n--------------------------\n\n Copied to clipboard.\n')