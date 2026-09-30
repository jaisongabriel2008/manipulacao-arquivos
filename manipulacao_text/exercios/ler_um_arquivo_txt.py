def ler_arquivo():
    with open('mensagem.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

# Chamada da função ao final do programa
ler_arquivo()