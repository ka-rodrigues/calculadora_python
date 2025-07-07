# Calculadora Simples em Python

Este é um programa de calculadora interativa desenvolvido em Python, que permite ao usuário realizar operações aritméticas básicas. O projeto demonstra conceitos fundamentais de entrada/saída de dados, laços de repetição e estruturas condicionais.

## Funcionalidades

O programa oferece um menu interativo com as seguintes operações:

*   **[1] Soma:** Realiza a adição de dois números.
*   **[2] Subtração:** Realiza a subtração de dois números.
*   **[3] Multiplicação:** Realiza a multiplicação de dois números.
*   **[4] Divisão:** Realiza a divisão de dois números, com tratamento para divisão por zero.
*   **[5] Sair:** Encerra a aplicação.

O sistema também inclui validação para garantir que o usuário escolha uma operação válida.

## Tecnologias Utilizadas

*   **Python 3:** Linguagem de programação principal.

## Estrutura do Código

O código é estruturado em um laço `while True` que mantém o menu da calculadora ativo até que o usuário escolha a opção de sair. As operações são controladas por uma série de `if/elif` que verificam a escolha do usuário e executam a operação correspondente. Há um tratamento específico para evitar divisão por zero.

## Próximos Passos e Melhorias

Este projeto pode ser expandido e aprimorado de diversas formas, como:

*   **Tratamento de Erros:** Adicionar tratamento de exceções para entradas não numéricas (ex: se o usuário digitar texto em vez de números).
*   **Refatoração para POO (Programação Orientada a Objetos):** Organizar as operações em métodos de uma classe `Calculadora` para melhor modularidade.
*   **Funções Dedicadas:** Criar funções separadas para cada operação (soma, subtração, etc.) para tornar o código mais legível e reutilizável.
*   **Interface Gráfica:** Desenvolver uma interface de usuário mais amigável (GUI) usando bibliotecas como Tkinter, PyQt ou Kivy.
*   **Operações Avançadas:** Adicionar mais operações matemáticas (potência, raiz quadrada, etc.).

---
