# Tarea 0.2 
El codigo que la Ia genero es el siguiente:

```
let message = 'Hello world';
def primos_criba(num: int) -> list[int]:
    lista = []
    """Implementación con Criba de Eratóstenes - más eficiente para rangos grandes."""
    if num < 2:
        return []

    # Crear array booleano inicializado en True
    es_primo_arr = [True] * (num + 1)
    es_primo_arr[0] = False
    es_primo_arr[1] = False

    # Criba de Eratóstenes
    for i in range(2, int(math.sqrt(num)) + 1):
        print(i)
        if es_primo_arr[i]:
            # Marcar múltiplos como no primos
            for j in range(i * i, num + 1, i):
                print(f"J {j}")
                es_primo_arr[j] = False

    for i in range(2, num+1):
        if es_primo_arr[i]:
            lista.append(i)
    return lista
```

## ¿Lo aceptaria?
Si lo aceptaria ya que mi codigo no es lo mas optimo ya que cada vez que quiero saber si un número es primo, vuelvo a checar todos sus posibles divisores desde cero. Eso significa que repito operaciones que ya hice antes para otros números.

Mientras que el metodo que me dio la IA usando la criba de eratostenes es lo mas optimo ya que no repite trabajo cada numero se checa una vez, elimina mucho rapido y desde el inicio.