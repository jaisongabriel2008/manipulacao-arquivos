import csv


def consultar_pokemons_treinador():
  while True:
    print("\n===== POKÉMON DOS TREINADORES =====")
    print("1 - Listar Pokémon de um treinador")
    print("2 - Contar Pokémon de um treinador")
    print("3 - Mostrar Pokémon de maior nível")
    print("4 - Mostrar Pokémon de menor nível")
    print("5 - Listar Pokémon de determinado tipo")
    print("6 - Voltar ao menu")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "6":
      break

    try:
      with open("treinadores.csv", mode="r", encoding="utf-8") as f_t:
        treinadores = list(csv.DictReader(f_t))
      with open("pokemons.csv", mode="r", encoding="utf-8") as f_p:
        pokemons = list(csv.DictReader(f_p))
    except FileNotFoundError:
      print("Erro: Arquivos CSV não encontrados.")
      continue

    if opcao in ["1", "2", "3", "4"]:
      nome_treinador = input("Digite o nome do treinador: ").strip()
      treinador_existe = any(
          t["nome"].strip().lower() == nome_treinador.lower()
          for t in treinadores
      )

      if not treinador_existe:
        print("Treinador não encontrado.")
        continue

      pokemons_treinador = [
          p
          for p in pokemons
          if p["treinador"].strip().lower() == nome_treinador.lower()
      ]

      if not pokemons_treinador:
        print("Este treinador não possui Pokémon cadastrados.")
        continue

      if opcao == "1":
        print(f"\n--- Pokémon de {nome_treinador} ---")
        for p in pokemons_treinador:
          print(
              f"- {p['nome']} | Tipo: {p['tipo']} | Nível: {p['nivel']}"
          )
      elif opcao == "2":
        print(
            f"\nO treinador {nome_treinador} possui"
            f" {len(pokemons_treinador)} Pokémon(s)."
        )
      elif opcao == "3":
        maior = max(pokemons_treinador, key=lambda x: int(x["nivel"]))
        print(
            f"\nPokémon de maior nível: {maior['nome']} (Nível"
            f" {maior['nivel']})"
        )
      elif opcao == "4":
        menor = min(pokemons_treinador, key=lambda x: int(x["nivel"]))
        print(
            f"\nPokémon de menor nível: {menor['nome']} (Nível"
            f" {menor['nivel']})"
        )

    elif opcao == "5":
      tipo_busca = input("Digite o tipo do Pokémon: ").strip().lower()
      encontrados = [
          p for p in pokemons if p["tipo"].strip().lower() == tipo_busca
      ]
      if encontrados:
        print(f"\n--- Pokémon do tipo {tipo_busca.title()} ---")
        for p in encontrados:
          print(
              f"- {p['nome']} (Nível {p['nivel']}) - Treinador:"
              f" {p['treinador']}"
          )
      else:
        print("Nenhum Pokémon encontrado para este tipo.")
    else:
      print("Opção inválida.")