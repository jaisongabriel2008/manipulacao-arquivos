import csv


def consultar_treinadores():
  while True:
    print("\n===== TREINADORES POKÉMON =====")
    print("1 - Listar todos os treinadores")
    print("2 - Buscar treinador pelo nome")
    print("3 - Listar treinadores de uma região")
    print("4 - Mostrar treinador com maior nível")
    print("5 - Mostrar treinador com menor nível")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    try:
      with open(
          "treinadores.csv", mode="r", encoding="utf-8"
      ) as arquivo_csv:
        treinadores = list(csv.DictReader(arquivo_csv))
    except FileNotFoundError:
      print("Erro: O arquivo 'treinadores.csv' não foi encontrado.")
      return

    if opcao == "1":
      print("\n--- Lista de Treinadores ---")
      for t in treinadores:
        print(f"Nome: {t['nome']} | Região: {t['regiao']} | Nível: {t['nivel']}")

    elif opcao == "2":
      nome_busca = input("Digite o nome do treinador: ").strip().lower()
      encontrado = False
      for t in treinadores:
        if t["nome"].strip().lower() == nome_busca:
          print(
              f"\nEncontrado! Nome: {t['nome']} | Região: {t['regiao']} | Nível:"
              f" {t['nivel']}"
          )
          encontrado = True
          break
      if not encontrado:
        print("Treinador não encontrado.")

    elif opcao == "3":
      regiao_busca = input("Digite a região: ").strip().lower()
      encontrado = False
      print(f"\n--- Treinadores da região: {regiao_busca.title()} ---")
      for t in treinadores:
        if t["regiao"].strip().lower() == regiao_busca:
          print(f"Nome: {t['nome']} | Nível: {t['nivel']}")
          encontrado = True
      if not encontrado:
        print("Nenhum treinador encontrado para esta região.")

    elif opcao == "4":
      if not treinadores:
        print("Nenhum treinador cadastrado.")
        continue
      maior = max(treinadores, key=lambda x: int(x["nivel"]))
      print(
          f"\nTreinador com maior nível: {maior['nome']} (Nível"
          f" {maior['nivel']})"
      )

    elif opcao == "5":
      if not treinadores:
        print("Nenhum treinador cadastrado.")
        continue
      menor = min(treinadores, key=lambda x: int(x["nivel"]))
      print(
          f"\nTreinador com menor nível: {menor['nome']} (Nível"
          f" {menor['nivel']})"
      )

    elif opcao == "6":
      print("Saindo do programa...")
      break
    else:
      print("Opção inválida! Escolha entre 1 e 6.")


# consultar_treinadores()