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
    PASTAS = 'MIDIA', 'ARQUIVOS', 'SCRIPTS'
    MIDIA = 'FOTOS', 'VIDEOS', 'MUSICAS'
    ARQUIVOS = 'XLSX', 'EXECUTAVEIS', 'ZIPADOS', 'PDF'
    SCRIPTS = 'PYTHON', 'HTML-CSS-JS'

    for value in extension:
        try:
            if value in arquivo:
                try:
                    shutil.move(arquivo, pasta)
                except:
                    for item in PASTAS:
                        os.makedirs(item)
                    pathCreate(PASTAS[0], MIDIA)
                    pathCreate(PASTAS[1], ARQUIVOS)
                    pathCreate(PASTAS[2], SCRIPTS)

                    shutil.move(arquivo, pasta)

            elif value not in arquivo:
                None
            
        except:
            os.remove(arquivo)

