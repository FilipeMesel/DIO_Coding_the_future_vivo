import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open("arquivo_nao_existente.py")
except FileNotFoundError as exec:
    print("Arquivo não encontrado!")
    print(exec)

try:
    arquivo = open(ROOT_PATH / 'novo-diretorio')
except IsADirectoryError as exec:
    print("Este arquivo é um diretório")
    print(exec)