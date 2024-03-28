import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a funcao.")

    return envelope

@meu_decorador
def ola_mundo():
    print("Olá mundo!")

def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        resultado = func(*args, **kwargs)
        return resultado
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

ola_mundo()
resultado = aprender("Python")
print(resultado)
print(ola_mundo.__name__)