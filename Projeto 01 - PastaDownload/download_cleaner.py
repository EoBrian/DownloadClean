from apps import *

diretório =pathDir()

#PASTAS
PASTAS = {
    #MIDIAS
    'musicas': diretório + r'\MIDIA\MUSICAS',
    'videos': diretório + r'\MIDIA\VIDEOS',
    'fotos': diretório + r'\MIDIA\FOTOS',
    
    #ARQUIVOS
    'planilhas': diretório + r'\ARQUIVOS\XLSX',
    'executaveis': diretório + r'\ARQUIVOS\EXECULTAVEIS',
    'documento': diretório + r'\ARQUIVOS\PDF',
    'zipados': diretório + r'\ARQUIVOS\ZIPADOS',
}

#EXTENSÕES DE ARQUIVOS
EXTENSION = {
    'musicas': ['.mp3', '.m4a', '.aac', '.flac', '.wma', '.wav', '.pcm'],
    'videos': ['.mp4', '.m4v', '.mov', '.avi', '.mkv', '.wmv', '.mpg', '.mpeg'],
    'imagens': ['.png', '.jpeg', '.jpg', '.gif'],
    'planilhas': ['.xlsx', '.xls', '.csv', '.sql', '.bat'],
    'execultaveis': ['.exe', '.bash', '.msi', '.sh'],
    'documento': ['.pdf', '.txt', '.doc', '.docx', '.ppt', '.pps'],
    'zipados': ['.tar', '.z', '.gz', '.taz', '.tgz', '.rar', '.zip', '.cab', '.arj'],
}

if __name__ == '__main__':

    arquivos = pathDownload(diretório)

    for archives in arquivos:
        pass
        for extension, path in zip(EXTENSION, PASTAS):
            archiveID(archives, EXTENSION[extension], PASTAS[path])
        
