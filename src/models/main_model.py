from tkinter import filedialog
import os

class MainModel:
    def __init__(self):
        self.path = ''

    def path_dir(self):
        self.path = filedialog.askdirectory()
        if self.path:
            return self.path

    def search_archives(self, path):
       self.directory = os.listdir(path=path)
       self.archives = [files for files in self.directory if '.xml' in files]
       return self.archives
    
