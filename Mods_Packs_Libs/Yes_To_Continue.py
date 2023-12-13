import pyinputplus as pyip

def yes_to_continue(prompt):
    print(prompt)
    while True:
        response = pyip.inputYesNo()
        if response != 'yes':
            print('Answer other than \'yes\' provided.')
            continue
        else:
            break