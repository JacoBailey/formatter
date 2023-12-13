#TEMPLATE INPUT MODE
#Locate prompt input locations, have the user supply inputs, & fill in the prompt with the user-supplied inputs

import Mods_Packs_Libs #Custom modules
import os, re
import pyinputplus as pyip
from pathlib import Path

inputRegex = re.compile(r'''(
                        (INSERT{1})
                        ((\s{1}[A-Z0-9]+)+)
                        )''', re.VERBOSE)

class NoInputsInTemplateFile(Exception):
    'Exiting program due to no inputs in template file. Please ensure the template file used has at least one input slot and that they are using correct syntax.'
    pass

def template_inputter():
    progDirectory = __file__.removesuffix(str(Path(__file__).name))
    templatesDirectory = os.path.join(Path(progDirectory), 'Template_Inputter', 'Templates')
    templatesDirectoryObject = Mods_Packs_Libs.walk_simple(templatesDirectory)
    templatesList = templatesDirectoryObject.files()
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
        userInput = Mods_Packs_Libs.inputCorrectValidation(f'Please enter an input for: {inputSlotName}.', inputSlotName)
        userInputsDict[inputSlotName] = userInput
        userSelectedTemplate_Contents = userSelectedTemplate_Contents.replace(fullInputSlot, userInput)
    return userSelectedTemplate_Contents