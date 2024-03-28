# inner functions

def mensagem(nome):
    print('eecutando mensagem')
    return f"oi {nome}"

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f"Olá {nome}! Tudo bem com você?"

# Funções internas

def funcao(nome):
    def mensagem_interna(nome):
        print('eecutando mensagem interna')
        return f"oi {nome}"

    def mensagem_longa_interna(nome):
        print('executando mensagem longa interna')
        return f"Olá {nome}! Tudo bem com você?"

    mensagem_interna(nome)
    mensagem_longa_interna(nome)

def calculadora(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        return a / b

    match operacao:
        case "+":
            return somar
        case "-":
            return subtrair
        case "*":
            return multiplicar
        case "/":
            return dividir
        

def executar(funcao, nome):
    print('executando executar')
    return funcao(nome)



print(executar(mensagem_longa, "Filipe"))

print(executar(funcao, "Filipe"))

print(calculadora("+")(1, 2))
print(calculadora("-")(1, 2))
print(calculadora("*")(1, 2))
print(calculadora("/")(1, 2))