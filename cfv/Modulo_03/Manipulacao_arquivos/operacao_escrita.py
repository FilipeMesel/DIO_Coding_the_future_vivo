file = open('example2.txt', 'w')
file.write("uma nova linha com metodo write")
file.writelines(["Escrevendo", "um", "novo", "texto"])
file.writelines(["\n", "Escrevendo","\n", "um","\n", "novo","\n", "texto"])
file.close