#REGEX REPLACEMENT MODE
#Use a user-provided regex pattern to find and replace matches in a user-provided file/clipboard-string

import ModsPacksLibs #Custom modules
import os, re, pyperclip
import pyinputplus as pyip
from pathlib import Path

def regexReplacement():
    regexPattern = ModsPacksLibs.inputCorrectValidation('Please enter your regex match pattern.', 'Regex Match Pattern')
    regexMatchReplacement = ModsPacksLibs.inputCorrectValidation('Please enter your regex match replacement string.', 'Regex Match Replacement String')
    regexPattern = repr(regexPattern).strip("'") #Closest equivalent to raw string for regex match
    regexMethod = pyip.inputMenu(['Template File', 'Clipboard String'], prompt='Select type of string to use for regex replacement:\n', numbered=True)
    if regexMethod == 'Template File':
        progDirectory = __file__.removesuffix(str(Path(__file__).name))
        templatesDirectory = os.path.join(Path(progDirectory), 'User_Regex_Templates')
        userRegexTempalates = ModsPacksLibs.filewalk(templatesDirectory)
        regexReplacementFilename = pyip.inputMenu(userRegexTempalates, prompt='Select textfile template for regex replacement:\n', numbered=True)
        with os.path.join(Path(progDirectory),regexReplacementFilename) as regexReplacmentFile:
            regexReplacementString = open(regexReplacmentFile, 'r')
    else:
        ModsPacksLibs.yesToContinue('Please enter "Yes" when you have copied the regex replacement string to your clipboard.')
        regexReplacementString = pyperclip.paste()
    return re.sub(regexPattern, regexMatchReplacement, regexReplacementString)