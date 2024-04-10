#REGEX REPLACEMENT MODE
#Use a user-provided regex pattern to find and replace matches in a user-provided file/clipboard-string

#TODO: Break up replacement modes into separate files/functions
#TODO: Handle exceptions (consider all edge cases)

import Mods_Packs_Libs #Custom modules
import os, re, pyperclip, csv
import pyinputplus as pyip
from pathlib import Path

def regex_replacement():
    #Setup local func variables
    regexReplacement = ''
    mainRegexReplacementList = []
    progDirectory = __file__.removesuffix(str(Path(__file__).name))
    
    #Select program mode
    mode = pyip.inputMenu(['Single Replacement', 'Multiple Replacement'], prompt='Select a regex replacement mode:\n', numbered=True)

    #Single Replacement Mode
    if mode == 'Single Replacement':
        #Input regex match pattern and regex replacement string
        regexPattern = Mods_Packs_Libs.input_correct_validation('Please enter your regex match pattern.', 'Regex Match Pattern')
        regexPattern = repr(regexPattern).strip("'") #Closest equivalent to raw string for regex match
        regexMatchReplacement = Mods_Packs_Libs.input_correct_validation('Please enter your regex match replacement string.', 'Regex Match Replacement String')
        #Ask for source for regex string (clipboard or file), copy source contents as regex string
        regexMethod = pyip.inputMenu(['Template File', 'Clipboard String'], prompt='Select a source for your regex search string:\n', numbered=True)
        if regexMethod == 'Template File':
            srDirectoryPath = os.path.join(Path(progDirectory), 'Regex', 'Single_Replacement')
            srDirectory = Mods_Packs_Libs.walk_simple(srDirectoryPath)
            srFilename = pyip.inputMenu(srDirectory.files, prompt='Please select the file you would like to use for the Regex Search String:\n', numbered=True)
            srFilePath = os.path.join(Path(srDirectoryPath),srFilename)
            with open(srFilePath, 'r') as regexReplacementFile:
                regexString = regexReplacementFile.read()
        else:
            Mods_Packs_Libs.yes_to_continue('Please enter "Yes" when you have copied the regex search string to your clipboard.\n')
            regexString = pyperclip.paste()
        #Append main regex list with regex match pattern, replacement, and regex string
        mainRegexReplacementList.append([regexPattern, regexMatchReplacement, regexString])
    
    #Multiple replacement mode
    else:
        mrDirectoryPath = os.path.join(Path(progDirectory), 'Regex', 'Multiple_Replacement')
        mrDirectory = Mods_Packs_Libs.walk_simple(mrDirectoryPath)
        #Select directory as source for regex replacement components
        mrSubdirectoryName = pyip.inputMenu(mrDirectory.dirs, prompt='Please select a directory:\n', numbered=True)
        mrSubdirectoryPath = os.path.join(mrDirectoryPath, mrSubdirectoryName)
        mrSubdirectory = Mods_Packs_Libs.walk_simple(mrSubdirectoryPath)
        #Save CSV contents as regex patterns and replacements
        for file in mrSubdirectory.files:
            if Path(file).suffix == '.csv':
                regexCsvFile = os.path.join(mrSubdirectoryPath, file)
            elif Path(file).suffix == '.txt':
                regexStringFile = os.path.join(mrSubdirectoryPath, file)
            else:
                continue
        with open(regexCsvFile, 'r') as csvFile:
            csvReader = csv.reader(csvFile)
            next(csvReader) #Skipping first row - this is the column name row
            for row in csvReader:
                mainRegexReplacementList.append(row)
        #Save textfile contents as regex search string
        with open(regexStringFile, 'r') as fileContents:
            regexString = fileContents.read()
    
    #Perform regex sub(s)/replacement(s)
    for row in mainRegexReplacementList:
        regexPattern = row[0]
        regexMatchReplacement = row[1]
        regexString = re.sub(regexPattern, regexMatchReplacement, regexString)
    
    #Return replaced string
    return regexString