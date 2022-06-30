from apps import *

diretório = pathDir()
informações = os.environ
usuário = informações['USERPROFILE'] 
#PASTAS
PASTAS = {
    #MIDIAS
    'musicas': usuário + r'\Music',
    'videos': usuário + r'\Videos',
    'fotos': usuário + r'\OneDrive\Imagens',
    'planilhas': diretório + r'\ARQUIVOS\XLSX',
    'executaveis': diretório + r'\ARQUIVOS\EXECUTAVEIS',
    'documento': diretório + r'\ARQUIVOS\PDF',
    'zipados': diretório + r'\ARQUIVOS\ZIPADOS',
    'python': diretório + r'\SCRIPTS\PYTHON',
    'html': diretório + r'\SCRIPTS\HTML-CSS-JS'
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
    'python': ['.py', '.pip', '.pipe', '.pype'],
    'html': ['.html', '.css', '.js', '.json', '.text']
}

if __name__ == '__main__':

    arquivos = pathDownload(diretório)

    for archives in arquivos:
        pass
        for extension, path in zip(EXTENSION, PASTAS):
            archiveID(archives, EXTENSION[extension], PASTAS[path])
        
