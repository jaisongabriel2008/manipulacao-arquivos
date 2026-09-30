def contar_palavras():
    with open('texto.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        print(f"Quantidade de palavras: {len(palavras)}")

contar_palavras()