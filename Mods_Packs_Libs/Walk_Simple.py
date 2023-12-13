import os

class walk_simple:
    def __init__(self, directory):
        self.directory = directory

    '''def ammendDirectory(self, ammendment_directory):
        self.directory = os.path.join(self.directory ,ammendment_directory)'''
    
    def files(self): #TODO: Determine way to hide hidden filetypes such as .DS_Store
        for root, dirs, files in os.walk(self.directory):
            return files

    def directories(self): #TODO: Determine way to hide hidden filetypes such as .DS_Store
        for root, dirs, files in os.walk(self.directory):
            return dirs