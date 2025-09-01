import math


def es_primo(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False

    raiz = int(math.sqrt(num))+1
    for i in range(3, raiz, 2):
        if num % i == 0:
            return False
    return True


def primos(num: int) -> list[int]:
    if num < 2:
        return []

    lista = [2]

    for n in range(3, num + 1, 2):
        if es_primo(n):
            lista.append(n)
    return lista


print(primos(20))
