"""
Projeto de um leitor de DANFE usando a biblioteca xmltodict, pandas e tkinter

- O sistema lerá arquivos DANFE em busca de informações específicas
- imprimirá essas informações numa GUI feita com TKinter
- O sistema oferecerá a opção de criar um arquivo excel com os dados retirados das DANFES
"""
import tkinter
from tkinter import filedialog


def select_dir():
    selected_dir = filedialog.askdirectory()
    if select_dir:
        label_selected_dir.config(text='{}'.format(selected_dir))

window = tkinter.Tk()
window.title('Leitor de DANFE by MeuHubPython')

label = tkinter.Label(window, text='Leitor de DANFE', font='helvetica 15')
label.pack(pady=20)

main_frame = tkinter.Frame(window, height=250, width=400)
main_frame.pack()

label_selected_dir = tkinter.Label(main_frame, text='Nenhum caminho selecionado', font='helvetica 11')
label_selected_dir.grid(row=0, column=1, padx=5, pady=5)

label_entry_dir = tkinter.Label(main_frame, text='Caminho da pasta: ', font='helvetiva 11')
label_entry_dir.grid(row=1, column=0, padx=1, pady=1)

entry_variable = tkinter.StringVar()
dir_entry = tkinter.Entry(main_frame, textvariable=entry_variable, width=50)
dir_entry.grid(row=1, column=1, padx=5)

search_dir_button = tkinter.Button(main_frame, text='Selecionar Diretório', font='helvetica 11', cursor='hand2', command=select_dir)
search_dir_button.grid(row=1, column=2, padx=5)



window.mainloop()
