def contar_caracteres():
    with open('texto.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(f"Quantidade de caracteres: {len(conteudo)}")

contar_caracteres()