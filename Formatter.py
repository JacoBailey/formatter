#! python3

from List_Formatter import list_formatter
from Template_Inputter import template_inputter
from Regex_Replacement import regex_replacement
import Mods_Packs_Libs #Custom modules
import pyperclip, os
import pyinputplus as pyip
from pathlib import Path

#Print a fun formatter tool message to screen
print('- - - - - - - - - - -\n- - - FORMATTER - - -\n- - - - - - - - - - -')

#Have user select mode, execute selection mode function, and save return value to variable
modeDictionary = {'List Formatter':list_formatter,'Template Inputter':template_inputter, 'Regex Replacement':regex_replacement}
listSelection = pyip.inputMenu(list(modeDictionary.keys()), prompt='Select formatter mode:\n', numbered=True)
returnValue = modeDictionary[listSelection]()

#Have user select how to output results (copied to clipboard, saved to textfile, or both)
outputSelection = pyip.inputMenu(['Saved to Clipboard', 'Saved to \'Outputs\' directory', 'Saved to Clipboard and \'Outputs\' directory'], prompt='How would you like to output your results:\n', numbered=True)
outputsDirecPath = os.path.join(__file__.removesuffix(str(Path(__file__).name)), 'Outputs')
if outputSelection == 'Saved to Clipboard' or outputSelection == 'Saved to Clipboard and \'Outputs\' directory':
    pyperclip.copy(returnValue)
if outputSelection == 'Saved to \'Outputs\' directory' or outputSelection =='Saved to Clipboard and \'Outputs\' directory':
    fileName = Mods_Packs_Libs.input_correct_validation('Please enter a name for the output file:', 'output filename')
    with open(Path(os.path.join(outputsDirecPath, (fileName + '.txt'))), 'w') as file:
        file.write(returnValue)

#Print results and selected output method
print(f'\n--------------------------\n\n{returnValue}\n\n--------------------------\n\n{outputSelection}\n')