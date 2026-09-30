def calcular_estoque():
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

    valor_total = 0.0
    for p in produtos:
        valor_total += p["preco"] * p["quantidade"]

    print(f"Valor total do estoque: R$ {valor_total:.2f}")


calcular_estoque()