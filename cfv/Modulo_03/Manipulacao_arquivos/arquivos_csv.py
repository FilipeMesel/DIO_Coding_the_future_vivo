import os
import shutil
from pathlib import Path
import csv

ROOT_PATH = Path(__file__).parent

# try:
#     with open(ROOT_PATH/ 'usuarios.csv', 'w',  encoding='utf-8') as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(['id', 'nome'])
#         escritor.writerow(['1', 'Maria'])
#         escritor.writerow(['2', 'João'])
# except IOError as exc:
#     print("Erro ao abrir o arquivo ")
#     print(exc)

# try:
#     with open(ROOT_PATH/ 'usuarios.csv', 'r',  encoding='utf-8') as arquivo:
#         leitor = csv.reader(arquivo)
#         for row in leitor:
#             print(row)
# except IOError as exc:
#     print("Erro ao abrir o arquivo ")
#     print(exc)

COLUNA_ID = 0
COLUNA_NOME = 1
try:
    with open(ROOT_PATH/ 'usuarios.csv', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row[COLUNA_ID], row[COLUNA_NOME])
except IOError as exc:
    print("Erro ao abrir o arquivo ")
    print(exc)