import os
import shutil

    
def pathDir():
    #Pegado diretório padrão do usuário
    informações = os.environ
    usuário = informações['USERPROFILE'] 
    #pasta download
    return rf'{usuário}\Downloads'


def pathDownload(diretório):
    #navegando até a pasta download
    os.chdir(diretório)
    return os.listdir()


def archiveID(arquivo, extension, pasta):
    PASTAS = 'MIDIA', 'ARQUIVOS', 'SCRIPTS'
    MIDIA = 'FOTOS', 'VIDEOS', 'MUSICAS'
    ARQUIVOS = 'XLSX', 'EXECUTAVEIS', 'ZIPADOS', 'PDF'
    SCRIPTS = 'PYTHON', 'HTML-CSS-JS'

    directory = pathDir()

    for value in extension:
        try:
            if value in arquivo:
                try:
                    shutil.move(arquivo, pasta)
                except:
                    for path in PASTAS:
                        os.makedirs(path)     
                    
                    os.chdir('ARQUIVOS')    
                    for item in ARQUIVOS:
                        os.makedirs(item)

                    os.chdir(directory)

                    os.chdir('MIDIA')
                    for item in MIDIA:
                        os.makedirs(item)
                        
                    os.chdir('SCRIPTS')
                    for item in SCRIPTS:
                        os.makedirs(item)

                    os.chdir(directory)
                    shutil.move(arquivo, pasta)

            elif value not in arquivo:
                None
            
        except:
            os.remove(arquivo)

