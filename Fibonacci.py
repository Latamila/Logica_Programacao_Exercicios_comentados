def fibonacci(n):
 if n <= 1:
   return n
 else:
   return fibonacci(n-1) + fibonacci(n-2)
   
num = int(input('Digite um numero para encontrar seu Fibonacci: '))
resposta = fibonacci(num-1)
print('\t', resposta)

'''
Uma solução mais eficiente para o cálculo da sequência de Fibonacci em 
Python é utilizar programação dinâmica, evitando assim recalculos 
desnecessários que ocorrem na abordagem recursiva simples. Aqui está um 
exemplo de como você pode implementar isso usando uma lista para armazenar 
os resultados intermediários:

'''
def fibonacci(n):
    # Inicializa uma lista para armazenar os resultados intermediários
    fib_list = [0] * (n + 1)

    # Casos base
    fib_list[0] = 0
    if n > 0:
        fib_list[1] = 1

    # Calcula os números Fibonacci de forma iterativa
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]

    return fib_list[n]

# Solicita ao usuário para inserir um número para encontrar seu número 
Fibonacci
num = int(input('Digite um numero para encontrar seu Fibonacci: '))

# Chama a função fibonacci para calcular o número Fibonacci correspondente
resposta = fibonacci(num)

# Imprime o resultado
print('\t', resposta)

'''
**Explicação:**

1. **Lista para Armazenar Resultados Intermediários:**
   - Utiliza uma lista chamada `fib_list` para armazenar os resultados 
   intermediários. Cada elemento da lista `fib_list` representa o 
   número Fibonacci correspondente.

2. **Casos Base e Inicialização:**
   - Define os casos base da sequência de Fibonacci (0 e 1).
   - Inicializa a lista `fib_list` com os valores dos casos base.

3. **Cálculo Iterativo:**
   - Utiliza um loop `for` para calcular iterativamente os números 
   Fibonacci de 2 até `n`.
   - Evita a repetição de cálculos desnecessários ao armazenar os
   resultados intermediários na lista.

4. **Retorno do Resultado Final:**
   - Retorna o número Fibonacci correspondente ao valor de `n`.

**Exemplo de Execução:**
```
Digite um numero para encontrar seu Fibonacci: 5
     5
```
Neste exemplo, a saída é a mesma que a abordagem recursiva simples, 
mas a implementação é mais eficiente para valores grandes de `n`. 
Isso ocorre porque evitamos recalcular os números Fibonacci várias 
vezes ao armazenar os resultados intermediários na lista.
'''
