arquivo = open('C:/Users/botto/Documents/projetos_auxiliares/cfv/Modulo_03/Manipulacao_arquivos/example.txt', 'r')

print(arquivo.read())

arquivo.close()

arquivo = open('C:/Users/botto/Documents/projetos_auxiliares/cfv/Modulo_03/Manipulacao_arquivos/example.txt', 'r')

# lendo linha por linha
print(arquivo.readline())
print(arquivo.readline())

for linha in arquivo.readline():
    print(linha)

arquivo.close()

arquivo = open('C:/Users/botto/Documents/projetos_auxiliares/cfv/Modulo_03/Manipulacao_arquivos/example.txt', 'r')

#Criando uma lista de linhas
print(arquivo.readlines())

arquivo.close()

