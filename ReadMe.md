Title

    Formatter Tool

Project Description
    
    The purpose of this program is to enable the user to quickly format text-based data in a variety of useful ways. The 3 main options for formatting with this program are as follows:

        1. List Formatter
            - Enables the user to easily add prefixes and suffixes to delimited text-based data.
        2. Template Inputter
            - Lets the user easily and efficiently fill out a custom text-based template.
        3. Regex Replacement
            - Allows the user to quickly regex search-and-replace a text string with their selected
              regex-match pattern.

    Packaging together a multitude of ways to manipulate text-based data into a single program enables users to speed up and simplify a variety of workflows in a number of unique and valuable ways.

Technologies Used

    For the main logic of the program, I chose to use python. During my original creation of the program, it was the sole programming language which I knew. Additionally, this was a personal project which I used to both optimize my work and solidify my knowledge of the language.

Challenges faced

    - No significant notable challenges thus far

Features

    Current Features
        1. List Formatter
            - Enables the user to easily add prefex and suffixes to delimited text-based data.
        2. Template Inputter
            - Lets the user easily and efficiently fill out a user-supplied text-based template.
        3. Regex Replacement (IN PROGRESS)
            - Allows the user to quickly regex search-and-replace a text string with their selected
              regex-match pattern.

    Planned Features
    - None at the moment

Installation

    1. Download the files via GitHub: https://github.com/JacoBailey/formatter
        - Click the green "code" button > "Download ZIP"
        - Save the ZIP somewhere on your device locally (icloud or similar cloud-based storage directories will not work)
    2. Unzip the file.
    3. Open Terminal/Powershell/etc. and run the following command(s) within the "...":

        " pip3 install pyperclip pyinputplus"

Setup

    1. Open the program file (usually named 'formatter-master').
    2. Open the "formatter-master" folder.
    3. Open the "User_Templates" folder (this is where all of your templates for the "Template Inputter"
        module will be stored).
    4. Using the example formatting which is showcased in the example files in this directory, create as many textfile prompt templates as you would like and save them in this folder.
        - Files MUST use formatting shown in the example file with each input slot starting with "INSERT" and the remaining text written in capitals, otherwise the program will not recgonize it.
        - After creating and saving your custom templates, you are welcome to delete the example tempalate files so that they will not be picked up and used by the program.

Run Instructions

    There are 2 options to run the program.

    A. Bash/Shell Script (recommended).
        - Google instructions on how to do this. There are many resources available online.
        - Use the filepath of the 'formatter.py' file for the Bash/Shell script.
    B. Terminal w/ Filepath.
        - Open the program file (should be named 'formatter-master').
        - Copy the filepath for the 'formatter.py' file.
        - Open Terminal, Powershell, etc.
        - Enter 'python3 COPIED-FILEPATH-HERE' (Make sure to replace the COPIED-FILEPATH HERE with your filepath location which you just copied)
        - Click 'enter'

How To Contribute

    I'm very open to changes, espeically if they are related to adding additional text-modification modules to 
    the program. Please open a PR and feel free to tag me in the comments section of your PR.