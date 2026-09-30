def buscar_produto():
    produtos = []
    with open('produtos.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 3:
                produtos.append({
                    "nome": partes[0],
                    "preco": float(partes[1]),
                    "quantidade": int(partes[2])
                })

    termo = input("Digite o produto: ")
    encontrado = False

    for p in produtos:
        if p["nome"].lower() == termo.lower():
            print("\nProduto encontrado!")
            print(f"Nome: {p['nome']}")
            print(f"Preço: R$ {p['preco']:.2f}")
            print(f"Quantidade: {p['quantidade']}")
            encontrado = True
            break

    if not encontrado:
        print("\nProduto não encontrado!")


buscar_produto()