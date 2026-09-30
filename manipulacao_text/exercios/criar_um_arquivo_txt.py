def criar_arquivo():
    frase = input("Digite uma frase: ")
    with open('frase.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(frase)

# Chamada da função ao final do programa
criar_arquivo()