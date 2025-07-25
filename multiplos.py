def soma_multiplos(n):
    soma = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            soma += i
    return soma


if __name__ == "__main__":
    import sys

    try:
        numero = int(sys.argv[1])
        resultado = soma_multiplos(numero)
        print(f"A soma dos múltiplos de 3 ou 5 abaixo de {numero} é {resultado}")
    except IndexError:
        print("Por favor, forneça um número como argumento.")
    except ValueError as e:
        print(e)
