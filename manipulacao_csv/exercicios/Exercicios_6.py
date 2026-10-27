import csv


def campeonato_pokemon():
  try:
    with open("treinadores.csv", mode="r", encoding="utf-8") as f_t:
      treinadores = list(csv.DictReader(f_t))
    with open("pokemons.csv", mode="r", encoding="utf-8") as f_p:
      pokemons = list(csv.DictReader(f_p))
  except FileNotFoundError:
    print("Arquivos de base não encontrados.")
    return

  classificacao_cache = []

  while True:
    print("\n===== CAMPEONATO POKÉMON =====")
    print("1 - Listar treinadores")
    print("2 - Consultar equipe")
    print("3 - Calcular pontuação")
    print("4 - Mostrar classificação")
    print("5 - Gerar arquivo CSV do campeonato")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
      for t in treinadores:
        print(f"- {t['nome']} ({t['regiao']}) - Nível {t['nivel']}")

    elif opcao == "2":
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
      print(f"Nível: {t['nivel']}\n")
      print("Pokémon da equipe:")
      pokes = [
          p for p in pokemons if p["treinador"].strip().lower() == nome.lower()
      ]
      for i, p in enumerate(pokes, 1):
        print(f"{i} - {p['nome']} - {p['tipo']} - {p['nivel']}")

    elif opcao == "3":
      classificacao_cache = []
      for t in treinadores:
        tr_nome = t["nome"]
        pokes = [
            p
            for p in pokemons
            if p["treinador"].strip().lower() == tr_nome.lower()
        ]
        soma_niveis = sum(int(p["nivel"]) for p in pokes)
        nivel_treinador = int(t["nivel"])
        pontuacao = nivel_treinador + soma_niveis

        dados = {
            "treinador": tr_nome,
            "regiao": t["regiao"],
            "nivel_treinador": nivel_treinador,
            "quantidade_pokemons": len(pokes),
            "soma_niveis": soma_niveis,
            "pontuacao": pontuacao,
        }
        classificacao_cache.append(dados)
      print("Pontuações calculadas com sucesso!")

    elif opcao == "4":
      if not classificacao_cache:
        print("Calcule a pontuação primeiro (Opção 3).")
        continue
      classificacao_ordenada = sorted(
          classificacao_cache, key=lambda x: x["pontuacao"], reverse=True
      )
      print("\n--- CLASSIFICAÇÃO DO CAMPEONATO ---")
      for i, c in enumerate(classificacao_ordenada, 1):
        print(
            f"{i}º lugar: {c['treinador']} | Pontuação: {c['pontuacao']} (Nível"
            f" Treinador: {c['nivel_treinador']} + Soma Pokémon:"
            f" {c['soma_niveis']})"
        )

    elif opcao == "5":
      if not classificacao_cache:
        print("Calcule a pontuação primeiro (Opção 3).")
        continue
      classificacao_ordenada = sorted(
          classificacao_cache, key=lambda x: x["pontuacao"], reverse=True
      )
      campos = [
          "treinador",
          "regiao",
          "nivel_treinador",
          "quantidade_pokemons",
          "soma_niveis",
          "pontuacao",
      ]
      with open(
          "resultado_campeonato.csv", mode="w", newline="", encoding="utf-8"
      ) as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(classificacao_ordenada)
      print("Arquivo 'resultado_campeonato.csv' gerado com sucesso!")

    elif opcao == "6":
      break
    else:
      print("Opção inválida.")