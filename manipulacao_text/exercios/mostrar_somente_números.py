def mostrar_numeros():
    numeros = []
    with open('numeros.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            numeros.append(int(linha.strip()))

    for num in numeros:
        if num % 2 == 0:
            print(num)


mostrar_numeros()