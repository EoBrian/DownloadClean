import os
import shutil
import PySimpleGUI as sg


class Organize:
    def __init__(self):
        
        self.user_info = os.environ["USERPROFILE"]
        self.default_dir = ""
        self.default_path = ["Musicas", "Videos", "Imagens", "Executaveis", "Documentos", "Compactados", "Codigos"]
        self.PATH = {
            #MIDIAS
            'musicas': f"{self.default_dir}\\Musicas",
            'videos': f"{self.default_dir}\\Videos",
            'fotos': f"{self.default_dir}\\Imagens",
            'executaveis': f"{self.default_dir}\\Executaveis",
            'documento': f"{self.default_dir}\\Documentos",
            'zipados': f"{self.default_dir}\\Compactados",
            'python': f"{self.default_dir}\\Codigos",
        }
        
        #EXTENSÕES DE ARQUIVOS
        self.EXTENSION = {
            'musicas': ['.mp3', '.m4a', '.aac', '.flac', '.wma', '.wav', '.pcm'],
            'videos': ['.mp4', '.m4v', '.mov', '.avi', '.mkv', '.wmv', '.mpg', '.mpeg'],
            'imagens': ['.png', '.jpeg', '.jpg', '.gif', '.jfif'],
            'execultaveis': ['.exe', '.bash', '.msi', '.sh'],
            'documento': ['.pdf', '.txt', '.doc', '.docx', '.ppt', '.pps', '.xlsx', '.xls', '.csv', '.sql', '.bat'],
            'zipados': ['.tar', '.z', '.gz', '.taz', '.tgz', '.rar', '.zip', '.cab', '.arj','.7z', ".iso"],
            'python': ['.py', '.pip', '.pipe', '.pype','.html', '.css', '.js', '.json', '.text'],
        }
        
    
    def cache_data(self):
        layout = [
            [sg.Input("", key="-fold-", expand_x=1), sg.FolderBrowse("Fold", key="-fold-button-", auto_size_button=True)],
            [sg.Button("Save", key="-save-button-", expand_x=1)]
        ]
        window = sg.Window("Organize", layout, size=(400, 100))
        
        while True:
            event, values = window.read(timeout=1)
            
            if event == "-save-button-":
                if os.path.isdir(f"{self.user_info}\\OneDrive\\Documentos\\Organize") == False:
                    os.chdir(f"{self.user_info}\\OneDrive\\Documentos")
                    os.mkdir("Organize")
                    os.chdir("Organize")
                
                    with open("cache_data.txt", 'w') as data:
                        
                        data.write(values["-fold-"])
                
                    break

                else:
                    break
                
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break 
            
    
    def check_dir(self):
        os.chdir(self.default_dir)
        for path in self.default_path:
            if os.path.isdir(path) == False:
                os.mkdir(path)
        return
         
            
    def pathDownload(self, diretório):
        #navegando até a pasta download
        os.chdir(diretório)
        return os.listdir()


    def archiveID(self, arquivo, extension, pasta):
        for value in extension:
            try:
                if value in arquivo:      
                    shutil.move(arquivo, f"{self.default_dir}\\{pasta}")
                
            except:
                os.remove(arquivo)

   
    
    def run(self):
        if os.path.isfile(f"{self.user_info}\\OneDrive\\Documentos\\Organize\\cache_data.txt") == True:
            os.chdir(f"{self.user_info}\\OneDrive\\Documentos\\Organize")
            with open('cache_data.txt', "r") as data:
                self.default_dir = data.read()
        else:
            self.cache_data()

        self.check_dir()
        
        arquivos = self.pathDownload(self.default_dir)

        for archives in arquivos:
            for extension, path in zip(self.EXTENSION, self.PATH):
                self.archiveID(archives, self.EXTENSION[extension], self.PATH[path])
                
    

if __name__ == '__main__':
    clean = Organize()
    clean.run()
            
