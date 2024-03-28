import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / 'novo-diretorio')

# arquivo = open('novo-arquivo.txt', 'a')
# arquivo.close()

# os.rename(ROOT_PATH/ 'novo-arquivo.txt', ROOT_PATH/ 'alterado.txt')

#os.remove(ROOT_PATH/ 'alterado.txt')

shutil.move(ROOT_PATH/ 'novo-arquivo.txt', ROOT_PATH/ 'novo-diretorio' / 'novo-arquivo.txt')