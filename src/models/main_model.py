from tkinter import filedialog
import os, xmltodict

 # MainModel contém toda a parte de processamento de dados do sistema

class MainModel:
    def __init__(self):
        self.path = ''
        
        self.sellers_cnpj = '' 
        self.sellers_name = ''
        self.buyers_name = ''
        self.buyers_cnpj = ''
        self.date_format = ''
        self.total_value = ''
        self.product_name = ''
        self.product_code = ''
        self.index = 0
        self.itens = []

    def path_dir(self):

        """Função para selecionar a pasta onde estão os arquivos xml no dispositivo"""

        self.path = filedialog.askdirectory()
        if self.path:
            return self.path

    def search_archives(self, path):
       
       """Função que itera sobre todos os arquivos da pasta selecionada, colocando em uma lista todos os arqivos que contenham .xml no seu título"""

       self.directory = os.listdir(path=path)
       self.archives = [files for files in self.directory if '.xml' in files]
       return self.archives
    
    def search_information_on_file(self, path_file):
        
        """Função que abre o arquivo selecionado pelo usuário e extrai do xml as informações mais importantes da nota"""
        
        with open(f'{path_file}', 'rb') as selected_file:
            selected_xml = xmltodict.parse(selected_file)
            xml = selected_xml['nfeProc']['NFe']['infNFe']

            try:
                self.sellers_cnpj = xml['emit']['CNPJ']
            except KeyError:
                self.sellers_cnpj = xml['emit']['CPF']

            self.sellers_name = xml['emit']['xNome'].upper()

            try:
                self.buyers_cnpj = xml['dest']['CNPJ']
            except KeyError:
                self.buyers_cnpj = xml['dest']['CPF']

            self.buyers_name = xml['dest']['xNome'].upper()
            buy_date = xml['ide']['dhEmi'][0:10]
            self.date_format = f'{buy_date[8:10]}/{buy_date[5:7]}/{buy_date[0:4]}'
            self.total_value = xml['total']['ICMSTot']['vNF']
            
            try:
                self.product_code = xml['det']['prod']['cProd']
                self.product_name = xml['det']['prod']['xProd']

            except TypeError:
                for indice in range(len(xml['det'])):
                    self.product_name = xml['det'][indice]['prod']['xProd']
                    self.product_code = xml['det'][indice]['prod']['cProd']
                    if indice == 12:
                        break