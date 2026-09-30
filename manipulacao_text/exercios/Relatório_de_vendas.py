def gerar_relatorio():
    vendas = []
    with open('vendas.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 3:
                vendas.append({
                    "vendedor": partes[0],
                    "produto": partes[1],
                    "valor": float(partes[2])
                })

    total_geral = 0.0
    contagem_vendedores = {}
    totais_vendedores = {}

    for v in vendas:
        total_geral += v["valor"]
        vendedor = v["vendedor"]

        contagem_vendedores[vendedor] = contagem_vendedores.get(vendedor, 0) + 1
        totais_vendedores[vendedor] = totais_vendedores.get(vendedor, 0.0) + v["valor"]

    print(f"TOTAL DE VENDAS: R$ {total_geral:.2f}\n")
    print("Quantidade de vendas:")
    for v, qtd in contagem_vendedores.items():
        print(f"{v}: {qtd}")

    # Desafio adicional: Maior valor total em vendas
    top_vendedor = max(totais_vendedores, key=totais_vendedores.get)
    print(f"\nMaior valor em vendas: {top_vendedor} (R$ {totais_vendedores[top_vendedor]:.2f})")


gerar_relatorio()