import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH/ 'example03.txt', 'r') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print("Erro ao abrir o arquivo ")
    print(exc)

try:
    with open(ROOT_PATH/ 'arquivo-utf-8.txt', 'r', encoding='ascii') as arquivo:
        #arquivo.write("Aprendendo a manipular arquivos usando Python")
        print(arquivo.read())
except IOError as exc:
    print("Erro ao abrir o arquivo ")
    print(exc)