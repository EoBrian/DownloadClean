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

    for value in extension:
        try:
            if value in arquivo:
                shutil.move(arquivo, pasta)

            elif value not in arquivo:
                None
            
        except:
            os.remove(arquivo)

