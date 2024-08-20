# O MainController conecta a interface gráfica(MainView) com a lógica do programa(MainModel)
import platform
class MainController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.search_dir.config(command=self.ask_diretory)

        self.information = False

    def ask_diretory(self):

        """Função que conecta a seleção de pasta com a interface do usuário"""

        ask_dir = self.model.path_dir()
        if ask_dir:
            self.view.label_selected_dir.config(text="{}".format(ask_dir))
            self.view.list_files_xml = self.model.search_archives(ask_dir)
            self.view.create_label_files()
            self.view.button_select_file.config(command=self.run_xml)
    
    def run_xml(self):

        """Função para linkar váriaveis extraidas do xml com seus respectivos labels na interface do usuário"""

        if self.information == True:
            self.view.search_information_xml(reset=True)
            self.information = False

        selected_file = self.view.combo_files.get()

        if selected_file:
            system = platform.system()

            if system != 'Windows':
                new_path = self.model.path + '/' + selected_file
            else:
                new_path = self.model.path + '\\' + selected_file 

            self.model.search_information_on_file(new_path)
            self.view.search_information_xml()
            self.view.seller_name_label.config(text=f'Vendedor: {self.model.sellers_name}')

            if len(self.model.sellers_cnpj) == 11:
                self.view.seller_cnpj.config(text=f'CPF: {self.model.sellers_cnpj}')
            
            else:
                self.view.seller_cnpj.config(text=f'CNPJ: {self.model.sellers_cnpj}')

            self.view.buyer_name.config(text=f'Comprador: {self.model.buyers_name}')

            if len(self.model.buyers_cnpj) == 11:
                self.view.buyer_cnpj.config(text=f'CPF: {self.model.buyers_cnpj}')
            else:
                self.view.buyer_cnpj.config(text=f'CNPJ: {self.model.buyers_cnpj}')

            self.view.date.config(text=f'Data da nota: {self.model.date_format}')
            self.view.total.config(text=f'Valor total da nota: R${self.model.total_value}')
            self.view.product_code.config(text=f'Código do produto: {self.model.product_code}')
            self.view.product_name.config(text=f'{self.model.product_name}')
            self.information = True
            
            return self.information