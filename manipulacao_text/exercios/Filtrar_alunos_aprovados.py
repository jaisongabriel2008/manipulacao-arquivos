def listar_aprovados():
    print("Alunos aprovados:")
    with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, nota_str = linha.strip().split(";")
            nota = float(nota_str)
            if nota >= 6.0:
                print(f"{nome} - {nota}")

listar_aprovados()