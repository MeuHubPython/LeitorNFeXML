"""
Projeto de um leitor de DANFE .xml usando a biblioteca xmltodict, pandas e tkinter

- O sistema lerá arquivos DANFE.xml em busca de informações específicas
- imprimirá essas informações numa GUI feita com TKinter
- O sistema oferecerá a opção de criar um arquivo excel com os dados retirados das DANFES
"""
from tkinter import Tk
from views.main_view import MainView
from controllers.main_controller import MainController
from models.main_model import MainModel

def main():
    root = Tk()
    root.title("Leitor de DANFE by MeuHubPython")

    #Inicializando a Model
    model = MainModel()

    #Inicializando a View
    main_view = MainView(root)
    
    #Inicializando o Controller
    controller = MainController(main_view, model)


    root.mainloop()

if __name__ == '__main__':
    main()