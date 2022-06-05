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
    MIDIA = 'FOTOS', 'VIDEOS', 'MUSICAS'
    ARQUIVOS = 'XLSX', 'EXECUTAVEIS', 'ZIPADOS', 'PDF'
    directory = pathDir()

    for value in extension:
        try:
            if value in arquivo:
                try:
                    shutil.move(arquivo, pasta)
                except:
                    os.makedirs('ARQUIVOS')
                    os.makedirs('MIDIA')
                    os.chdir('ARQUIVOS')
                    
                    for item in ARQUIVOS:
                        os.makedirs(item)

                    os.chdir(directory)
                    os.chdir('MIDIA')

                    for item in MIDIA:
                        os.makedirs(item)
                        
                    os.chdir(directory)
                    shutil.move(arquivo, pasta)

            elif value not in arquivo:
                None
            
        except:
            os.remove(arquivo)

