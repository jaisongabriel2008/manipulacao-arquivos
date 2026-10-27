import csv


def gerador_csv():
  with open("treinadores.csv", mode="r", encoding="utf-8") as f_t:
    treinadores = list(csv.DictReader(f_t))
  with open("pokemons.csv", mode="r", encoding="utf-8") as f_p:
    pokemons = list(csv.DictReader(f_p))

  while True:
    print("\n===== GERADOR DE ARQUIVOS =====")
    print("1 - Listar treinadores")
    print("2 - Gerar CSV de um treinador")
    print("3 - Gerar CSV de todos os treinadores (ordenados)")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
      for t in treinadores:
        print(f"- {t['nome']}")

    elif opcao == "2":
      nome = input("Digite o treinador: ").strip()
      pokes_treinador = [
          p for p in pokemons if p["treinador"].strip().lower() == nome.lower()
      ]
      if not pokes_treinador:
        print("Nenhum Pokémon encontrado para este treinador.")
        continue

      nome_arquivo = (
          f"pokemons_{nome.lower().replace(' ', '_')}.csv"
      )
      campos = ["nome", "tipo", "nivel", "treinador"]

      with open(
          nome_arquivo, mode="w", newline="", encoding="utf-8"
      ) as f_out:
        escritor = csv.DictWriter(f_out, fieldnames=campos)
        escritor.writeheader()
        for p in pokes_treinador:
          escritor.writerow({k: p[k] for k in campos})

      print(
          f"Arquivo '{nome_arquivo}' gerado com sucesso!"
          f" {len(pokes_treinador)} registro(s) gravado(s)."
      )

    elif opcao == "3":
      pokemons_ordenados = sorted(
          pokemons, key=lambda x: int(x["nivel"]), reverse=True
      )
      nome_arquivo = "todos_pokemons_ordenados.csv"
      campos = ["nome", "tipo", "nivel", "treinador"]

      with open(
          nome_arquivo, mode="w", newline="", encoding="utf-8"
      ) as f_out:
        escritor = csv.DictWriter(f_out, fieldnames=campos)
        escritor.writeheader()
        for p in pokemons_ordenados:
          escritor.writerow({k: p[k] for k in campos})

      print(
          f"Arquivo '{nome_arquivo}' gerado com sucesso!"
          f" {len(pokemons_ordenados)} registro(s) gravado(s)."
      )

    elif opcao == "4":
      break
    else:
      print("Opção inválida.")