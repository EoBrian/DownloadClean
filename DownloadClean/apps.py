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


def pathCreate(local, name_path):
    os.chdir(local)
    for item in name_path:
        os.makedirs(item)
    os.chdir(pathDir())


def archiveID(arquivo, extension, pasta):
    download = pathDir()
    os.chdir(download)
    PASTAS ='ARQUIVOS', 'SCRIPTS'
    ARQUIVOS = 'XLSX', 'EXECUTAVEIS', 'ZIPADOS', 'PDF'
    SCRIPTS = 'PYTHON', 'HTML-CSS-JS'

    for value in extension:
        try:
            if value in arquivo:
                try:
                    shutil.move(arquivo, pasta)
                
                except Exception as error:
                    for item in PASTAS:
                        os.makedirs(item)
                    pathCreate(PASTAS[1], ARQUIVOS)
                    pathCreate(PASTAS[2], SCRIPTS)

                    shutil.move(arquivo, pasta)
                    
                except:
                    pass
            else:
                pass
        except:
            os.remove(arquivo)

