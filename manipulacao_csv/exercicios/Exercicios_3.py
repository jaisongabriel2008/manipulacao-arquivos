import csv


def gerar_relatorios():
  with open("treinadores.csv", mode="r", encoding="utf-8") as f_t:
    treinadores = list(csv.DictReader(f_t))
  with open("pokemons.csv", mode="r", encoding="utf-8") as f_p:
    pokemons = list(csv.DictReader(f_p))

  while True:
    print("\n===== RELATÓRIOS =====")
    print("1 - Relatório de um treinador")
    print("2 - Média de nível dos Pokémon de um treinador")
    print("3 - Média de nível dos Pokémon por tipo")
    print("4 - Quantidade de Pokémon por treinador")
    print("5 - Quantidade de Pokémon por tipo")
    print("6 - Treinadores com nível acima de um valor")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
      nome = input("Digite o nome do treinador: ").strip()
      t = next(
          (
              item
              for item in treinadores
              if item["nome"].strip().lower() == nome.lower()
          ),
          None,
      )
      if not t:
        print("Treinador não encontrado.")
        continue
      print(f"\nTreinador: {t['nome']}")
      print(f"Região: {t['regiao']}")
      print(f"Nível do treinador: {t['nivel']}\n")
      print("Pokémon:")
      pokes = [
          p for p in pokemons if p["treinador"].strip().lower() == nome.lower()
      ]
      for p in pokes:
        print(f"- {p['nome']} - {p['tipo']} - Nível {p['nivel']}")

    elif opcao == "2":
      nome = input("Digite o nome do treinador: ").strip()
      pokes = [
          p for p in pokemons if p["treinador"].strip().lower() == nome.lower()
      ]
      if not pokes:
        print("Nenhum Pokémon encontrado.")
        continue
      media = sum(int(p["nivel"]) for p in pokes) / len(pokes)
      print(f"Média de nível dos Pokémon de {nome}: {media:.2f}")

    elif opcao == "3":
      tipo = input("Digite o tipo: ").strip().lower()
      pokes = [p for p in pokemons if p["tipo"].strip().lower() == tipo]
      if not pokes:
        print("Nenhum Pokémon encontrado para este tipo.")
        continue
      media = sum(int(p["nivel"]) for p in pokes) / len(pokes)
      print(f"Média de nível dos Pokémon do tipo {tipo.title()}: {media:.2f}")

    elif opcao == "4":
      contagem = {}
      for p in pokemons:
        tr = p["treinador"]
        contagem[tr] = contagem.get(tr, 0) + 1
      ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
      print("\n--- Quantidade de Pokémon por Treinador ---")
      for tr, qtd in ordenado:
        print(f"{tr}: {qtd}")

    elif opcao == "5":
      contagem = {}
      for p in pokemons:
        tp = p["tipo"]
        contagem[tp] = contagem.get(tp, 0) + 1
      ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
      print("\n--- Quantidade de Pokémon por Tipo ---")
      for tp, qtd in ordenado:
        print(f"{tp}: {qtd}")

    elif opcao == "6":
      try:
        val = int(input("Digite o nível mínimo: "))
      except ValueError:
        print("Valor inválido.")
        continue
      print(f"\n--- Treinadores com nível acima de {val} ---")
      for t in treinadores:
        if int(t["nivel"]) > val:
          print(f"- {t['nome']} (Nível {t['nivel']})")

    elif opcao == "7":
      break
    else:
      print("Opção inválida.")