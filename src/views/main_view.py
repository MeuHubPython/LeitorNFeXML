from tkinter import Label, Frame, Button, Entry
from controllers.main_controller import MainController

class MainView(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.list_files_xml = []

    def create_widgets(self):
        self.main_label = Label(self, text='Leitor de DANFE', font='helvetica 15', pady=15)
        self.main_label.grid(row=0, column=1)

        self.label_dir = Label(self, text='Selecione o caminho da pasta: ', font='helvetica 11')
        self.label_dir.grid(row=1, column=0)

        self.label_selected_dir = Label(self, text='Nenhum caminho selecionado', font='helvetica 11')
        self.label_selected_dir.grid(row=1, column=1, padx=5)

        self.search_dir = Button(self, text='Procurar Pasta', cursor='hand2', font='helvetica 11')
        self.search_dir.grid(row=1, column=2, padx=5)
        
    def create_label_files(self):
        counter = 0
        for file_ in self.list_files_xml:
            self.label_files = Label(self, text=file_, font='helvetica 11')
            self.label_files.grid(row=2 + counter, column=1, pady=6)
            counter += 1
        