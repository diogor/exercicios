def fatorial(n):
    if n < 0:
        raise ValueError("Não é possível calcular o fatorial de números negativos")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    import sys

    try:
        number = int(sys.argv[1])
        print(f"O fatorial de {number} é {fatorial(number)}")
    except IndexError:
        print("Por favor, forneça um número como argumento.")
    except ValueError as e:
        print(e)
