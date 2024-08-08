

class MainController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.search_dir.config(command=self.ask_diretory)

    
    def ask_diretory(self):
        ask_dir = self.model.path_dir()
        if ask_dir:
            self.view.label_selected_dir.config(text="{}".format(ask_dir))
            self.view.list_files_xml = self.model.search_archives(ask_dir)
            self.view.create_label_files()