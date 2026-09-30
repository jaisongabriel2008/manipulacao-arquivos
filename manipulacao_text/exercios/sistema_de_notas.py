def gerenciar_notas():
    alunos = []
    with open('notas.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 4:
                alunos.append({
                    "nome": partes[0],
                    "n1": float(partes[1]),
                    "n2": float(partes[2]),
                    "n3": float(partes[3])
                })

    for a in alunos:
        media = (a["n1"] + a["n2"] + a["n3"]) / 3
        status = "Aprovado" if media >= 6.0 else "Reprovado"
        print(f"{a['nome']} - Média: {media:.2f} - {status}")


gerenciar_notas()