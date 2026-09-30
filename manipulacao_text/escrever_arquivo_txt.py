# Modo "r" - Abre o arquivo para leitura
# Modo "w" - Abre para escrita a apaga o conteudo  existente [
# Modo "a" - Adiciona novo conteúdo no final arquivo
# Modo "x" - Cria um arquivo novo e gera erro se ele já existir

def criar_arquivo_txt():
    # O "with" fecha o arquivo automaticamente
    # O "open"() função para leitura ou escrita de arquivos
    with open('arquivo_text.txt', 'w', encoding="utf-8") as arquivo:
        arquivo.write("Jaison\n")
        arquivo.write("Gabriel\n")
        arquivo.write("Davi\n")


# criar_arquivo_txt()

def adicionar_aluno(nome):
    with open("arquivo_text.txt", 'a', encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")


adicionar_aluno("Neymar")
adicionar_aluno("Pele")
adicionar_aluno("Maradona"

def listar_alunos():
    with open("arquivo_text.txt", 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(f"O conteudo do arquivos alunos é: {conteudo}")

        def listar_alunos_individuas():
        #Listar_alunos = []
        with open("arquivo_text.txt", 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            lista_alunos.append(linha.strip())

            nomes_alunos = [nome.strip() for nome in arquivo]

            print(f"lista de alunos: {nomes_alunos}")


            #Listar_aluno_individual()

            def cadastrar_aluno():
                nome = input ("Digite o nome do aluno: ")
                idade = int(input("Digite a idade do aluno: "))

                with open("arquivo_text.txt", 'a', encoding="utf-8") as arquivo:
                    arquivo.write(f"arquivo")



            #cadastrar_aluno()
            def listar_cadastro = []
            for linha in arquivo:
                nome, idade = linha.strip().split(",")
                obj = {
                    "nome": nome,
                    "idade": idade
                }

                itens_cadastro.append(obj)
                print(f"itens cadastrados: {itens_cadastro}")

                listar_castro