# Jogo de Adivinhação de Número

Projeto acadêmico desenvolvido no curso de **Tecnologia em Inteligência Artificial**. Um jogo de terminal em Python onde o usuário tenta adivinhar um número aleatório entre 1 e 100, com dicas de "sobe" ou "desce" a cada palpite e um sistema de recorde de menor número de tentativas.

## Como funciona

1. O programa sorteia um número aleatório entre 1 e 100.
2. O jogador vai digitando palpites até acertar, recebendo uma dica a cada tentativa:
   - **"Sobe um pouco mais"** se o palpite foi menor que o número sorteado
   - **"Desce um pouco"** se foi maior
   - Uma mensagem de aviso se o número estiver fora do intervalo válido
3. Ao acertar, o jogo mostra quantas tentativas foram usadas e compara com o recorde da sessão (inicia em 1000, mas na prática é batido logo na primeira rodada).
4. Pergunta se o jogador quer jogar de novo, repetindo o ciclo enquanto a resposta for "s".

## Conceitos praticados

- Laços de repetição aninhados (`while` externo para as rodadas, `while` interno para as tentativas dentro de uma rodada)
- Estruturas condicionais (`if`/`elif`/`else`) para lógica de comparação
- Geração de números aleatórios com o módulo `random`
- Entrada e validação básica de dados do usuário
- Controle de estado entre rodadas (variável de recorde persistindo entre partidas)

## Como executar

```bash
python3 jogo.py
```

## Stack

`Python 3` (biblioteca padrão apenas — `random`)
