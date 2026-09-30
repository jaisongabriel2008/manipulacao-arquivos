def classificar_alunos():
    with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, nota_str = linha.strip().split(";")
            nota = float(nota_str)

            if nota >= 6.0:
                status = "Aprovado"
            elif nota >= 4.0:
                status = "Recuperação"
            else:
                status = "Reprovado"

            print(f"{nome} - {nota} - {status}")


classificar_alunos()