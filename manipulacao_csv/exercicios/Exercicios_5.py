import csv


def gerenciador_pokemon():
  try:
    with open("pokemons.csv", mode="r", encoding="utf-8") as f:
      lista_pokemons = list(csv.DictReader(f))
    with open("treinadores.csv", mode="r", encoding="utf-8") as f:
      treinadores_validos = [t["nome"].strip().lower() for t in csv.DictReader(f)]
  except FileNotFoundError:
    print("Arquivos de base não encontrados.")
    return

  while True:
    print("\n===== GERENCIADOR DE POKÉMON =====")
    print("1 - Listar Pokémon")
    print("2 - Pesquisar Pokémon")
    print("3 - Adicionar Pokémon")
    print("4 - Alterar nível de um Pokémon")
    print("5 - Remover Pokémon")
    print("6 - Salvar alterações")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
      for p in lista_pokemons:
        print(
            f"{p['nome']} | Tipo: {p['tipo']} | Nível: {p['nivel']} |"
            f" Treinador: {p['treinador']}"
        )

    elif opcao == "2":
      nome = input("Digite o nome do Pokémon: ").strip().lower()
      p = next(
          (
              item
              for item in lista_pokemons
              if item["nome"].strip().lower() == nome
          ),
          None,
      )
      if p:
        print(
            f"\nNome: {p['nome']}\nTipo: {p['tipo']}\nNível:"
            f" {p['nivel']}\nTreinador: {p['treinador']}"
        )
      else:
        print("Pokémon não encontrado.")

    elif opcao == "3":
      nome = input("Nome: ").strip()
      tipo = input("Tipo: ").strip()
      try:
        nivel = int(input("Nível (1-100): "))
      except ValueError:
        print("Nível inválido.")
        continue
      treinador = input("Treinador: ").strip()

      # Validações do desafio
      if not nome or not tipo:
        print("Erro: Nome e tipo não podem ser vazios.")
        continue
      if not (1 <= nivel <= 100):
        print("Erro: O nível deve estar entre 1 e 100.")
        continue
      if treinador.lower() not in treinadores_validos:
        print("Erro: Treinador informado não existe em treinadores.csv.")
        continue
      if any(p["nome"].strip().lower() == nome.lower() for p in lista_pokemons):
        print("Erro: Pokémon já cadastrado.")
        continue

      novo = {
          "nome": nome,
          "tipo": tipo,
          "nivel": str(nivel),
          "treinador": treinador,
      }
      lista_pokemons.append(novo)
      print("Pokémon adicionado com sucesso à memória!")

    elif opcao == "4":
      nome = input("Nome do Pokémon para alterar o nível: ").strip().lower()
      encontrado = False
      for p in lista_pokemons:
        if p["nome"].strip().lower() == nome:
          try:
            novo_nivel = int(input("Novo nível (1-100): "))
            if 1 <= novo_nivel <= 100:
              p["nivel"] = str(novo_nivel)
              print("Nível alterado com sucesso!")
            else:
              print("Nível fora do intervalo permitido.")
          except ValueError:
            print("Valor inválido.")
          encontrado = True
          break
      if not encontrado:
        print("Pokémon não encontrado.")

    elif opcao == "5":
      nome = input("Nome do Pokémon para remover: ").strip().lower()
      tamanho_inicial = len(lista_pokemons)
      lista_pokemons = [
          p for p in lista_pokemons if p["nome"].strip().lower() != nome
      ]
      if len(lista_pokemons) < tamanho_inicial:
        print("Pokémon removido com sucesso.")
      else:
        print("Pokémon não encontrado.")

    elif opcao == "6":
      campos = ["nome", "tipo", "nivel", "treinador"]
      with open(
          "pokemons_atualizados.csv", mode="w", newline="", encoding="utf-8"
      ) as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista_pokemons)
      print("Alterações salvas em 'pokemons_atualizados.csv' com sucesso!")

    elif opcao == "7":
      break
    else:
      print("Opção inválida.")