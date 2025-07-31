# Jogo P3 - Avaliação Algoritmos I

## Descrição

Este projeto foi desenvolvido como parte da 3ª avaliação da disciplina de **Algoritmos I**.  
É um jogo simples feito em **Python**, usando a biblioteca **Pygame**.  
O jogador pode escolher entre dois modos diferentes para se desafiar:

- **Jogo 1:** Pular obstáculos
- **Jogo 2:** Desviar lateralmente dos obstáculos

A seguir, a tela inicial do jogo:

![Tela Inicial](imagens/menu.jpg)

---

## Como Executar

- **Python 3.x**
- **Biblioteca Pygame** instalada:  
  ```bash
  pip install pygame
  ```

1. Clone o repositório:
   ```bash
   git clone https://github.com/marina-veiga/pygame
   cd PYGAME
   ```

2. Execute o jogo:
   ```bash
   python jogo.py
   ```

---

## Estrutura do Código

- `jogo.py`: Arquivo principal que inicia o jogo e gerencia os modos.
- `audios/`: Contém os sons utilizados no jogo.
- `font/`: Arquivos de fontes personalizadas.
- `imagens/`: Recursos gráficos, como plano de fundo, personagem e obstáculos.

---

## Funcionalidades do Jogo

- **Tela inicial** com seleção entre dois modos.
- **Movimentação por teclado** (pular ou mover para os lados).
- **Sistema de colisão** entre personagem e obstáculos.
- **Trilha sonora** e efeitos sonoros.
- **Sistema de pontuação** (se implementado).

---

## Exemplo de Interação com o Jogo

```plaintext
>>> Início do jogo
Selecione um modo:
1 - Jogo de Pular Obstáculos
2 - Jogo de Desviar Obstáculos

>>> Jogador escolhe: 1

Jogo iniciado!
Use a tecla ESPAÇO para saltar os obstáculos.

Bateu! Game Over.
```

---

## Autores

Este projeto foi desenvolvido por:  
**Marina Veiga** e **Diogo Costa**
