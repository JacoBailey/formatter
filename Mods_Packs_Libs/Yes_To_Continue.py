import pyinputplus as pyip

def yes_to_continue(promptVar, test=False):
    while True:
        response = pyip.inputYesNo(prompt=promptVar)
        if response not in ['yes', 'y', 'YES', 'Y', 'Yes' 'yEs', 'yeS', 'YEs', 'yES', 'YeS']:
            if test == True:
                return True
            print('Answer other than \'yes\' provided.')
            continue
        else:
            if test == True:
                return True
            break