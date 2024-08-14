from tkinter import Label, Frame, Button
from tkinter import ttk

# MainView contém toda a interface gráfica do sistema

class MainView(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(padx=20, pady=10)
        self.create_widgets()
        self.list_files_xml = []
        self.create_label_files()

    def create_widgets(self):

        """create_widgets inicia a primeira etapa de widgets, para a busca do diretório dos arquivos"""

        self.main_label = Label(self, text='Leitor de DANFE', font='Roboto 15', pady=15)
        self.main_label.grid(row=0, column=1)

        self.label_dir = Label(self, text='Selecione o caminho da pasta: ', font='Roboto 11')
        self.label_dir.grid(row=1, column=0)

        self.label_selected_dir = Label(self, text='Nenhum caminho selecionado', font='helvetica 11')
        self.label_selected_dir.grid(row=1, column=1, padx=5)

        self.search_dir = Button(self, text='Procurar Pasta', cursor='hand2', font='helvetica 11')
        self.search_dir.grid(row=1, column=2, padx=5)
        
    def create_label_files(self):

        """create_label_files inicia a segunda etapa de widgets, pede ao usuário para selecionar um arquivo .xml contido no diretório escolhido na etapa anterior"""

        self.label_radio = Label(self, text='Selecione o arquivo XML que deseja abrir: ', font='Roboto 11')
        self.label_radio.grid(row=2, column=0)
        
        self.combo_files = ttk.Combobox(self, value=self.list_files_xml, font='helvetica 11', width=40)
        self.combo_files.grid(row=2, column=1,columnspan=2, pady=5)

        self.button_select_file = Button(self, text='Confirmar', font='helvetica 11', cursor='hand2')
        self.button_select_file.grid(row=2,column=3)
    
    def search_information_xml(self, reset=False):

        """search_information_xml é a etapa final de widgets, exibe na interface gráfica toda a informação da NFe"""

        if reset == True:
            self.seller_cnpj.config(text='')
            self.seller_name_label.config(text='')

            self.buyer_name.config(text='')
            self.buyer_cnpj.config(text='')

            self.date.config(text='')
            self.total.config(text='')

        else:
            self.blank_label = Label(self, text='')
            self.blank_label.grid(row=3, column=0)
    
            self.seller_name_label = Label(self, font='Roboto 11')
            self.seller_name_label.grid(row=4,column=0)
    
            self.seller_cnpj = Label(self, font='helvetica 11')
            self.seller_cnpj.grid(row=4, column=1)
    
            self.buyer_name = Label(self, font='Roboto 11')
            self.buyer_name.grid(row=5, column=0)
    
            self.buyer_cnpj = Label(self, font='helvetica 11')
            self.buyer_cnpj.grid(row=5, column=1)
    
            self.date = Label(self, font='Roboto 11')
            self.date.grid(row=4, column=2)
    
            self.total = Label(self, font='Roboto 11')
            self.total.grid(row=5, column=2)
