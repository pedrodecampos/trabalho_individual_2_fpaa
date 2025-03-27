# Algoritmo MaxMin Select - Seleção Simultânea do Maior e Menor Elementos

Este projeto implementa o algoritmo de seleção simultânea do maior e menor elementos (MaxMin Select) utilizando a técnica de divisão e conquista em Python.

## Descrição do Projeto

O algoritmo MaxMin Select é uma implementação eficiente para encontrar simultaneamente o maior e o menor elemento de uma sequência de números. A abordagem utiliza a técnica de divisão e conquista, onde o problema é dividido em subproblemas menores que são resolvidos recursivamente.

### Lógica de Implementação

O algoritmo funciona da seguinte forma:

1. **Caso Base 1**: Se a sequência contiver apenas um elemento, este elemento é tanto o maior quanto o menor.
2. **Caso Base 2**: Se a sequência contiver dois elementos, comparamos uma vez para determinar qual é o maior e qual é o menor.
3. **Caso Recursivo**: Para sequências maiores:
   - Dividimos a sequência em duas partes iguais
   - Resolvemos recursivamente cada parte
   - Combinamos os resultados comparando os menores e maiores elementos de cada parte

### Exemplo de Execução

Para a sequência [5, 2, 8, 1, 9, 3, 7, 4, 6]:

1. A sequência é dividida em [5, 2, 8, 1] e [9, 3, 7, 4, 6]
2. Cada parte é processada recursivamente
3. Os resultados são combinados para encontrar o menor (1) e o maior (9) elementos

## Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/trabalho_individual_2_FPAA.git
```

2. Navegue até o diretório do projeto:

```bash
cd trabalho_individual_2_FPAA
```

3. Execute o programa:

```bash
python main.py
```

## Relatório Técnico

### Análise da Complexidade Assintótica

#### Método de Contagem de Operações

Para uma sequência de n elementos:

1. **Divisão do Problema**:

   - O problema é dividido em duas partes de tamanho n/2
   - Cada divisão requer uma operação de cálculo do meio (O(1))

2. **Chamadas Recursivas**:

   - São feitas duas chamadas recursivas, cada uma com n/2 elementos
   - O número de níveis de recursão é log₂(n)

3. **Combinação dos Resultados**:
   - Em cada nível, são feitas 2 comparações para combinar os resultados
   - No total, são feitas 2n - 2 comparações

Portanto, a complexidade temporal é O(n).

#### Aplicação do Teorema Mestre

A recorrência do MaxMin Select é:
T(n) = 2T(n/2) + O(1)

1. **Identificação dos valores**:

   - a = 2 (número de subproblemas)
   - b = 2 (tamanho de cada subproblema)
   - f(n) = O(1) (custo da combinação)

2. **Cálculo de log_b(a)**:

   - log₂(2) = 1

3. **Caso do Teorema Mestre**:

   - Como f(n) = O(1) = O(n^log_b(a)) = O(n¹)
   - Estamos no caso 1 do Teorema Mestre

4. **Solução**:
   - T(n) = O(n^log_b(a)) = O(n¹) = O(n)

## Diagrama Visual

O diagrama visual do algoritmo pode ser encontrado na pasta `assets/maxmin_diagram.png`. Este diagrama ilustra:

1. A divisão do problema em subproblemas menores
2. A estrutura hierárquica da recursão
3. O processo de combinação dos resultados
4. O número de comparações em cada nível
