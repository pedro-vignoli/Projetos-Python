```
 ____  __   __ _____  _   _   ___   _   _
|  _ \ \ \ / /|_   _|| | | | / _ \ | \ | |
| |_) | \ V /   | |  | |_| || | | ||  \| |
|  __/   | |    | |  |  _  || |_| || |\  |
|_|      |_|    |_|  |_| |_| \___/ |_| \_|

 ____   ____    ___       _  _____   ____  _____  ____
|  _ \ |  _ \  / _ \     | || ____| / ___||_   _|/ ___|
| |_) || |_) || | | | _  | ||  _|  | |      | |  \___ \
|  __/ |  _ < | |_| || |_| || |___ | |___   | |   ___) |
|_|    |_| \_\ \___/  \___/ |_____| \____|  |_|  |____/
```

[English](README.md) | **Português**

---

## Sobre

Projetos práticos em Python feitos no 2º semestre de 2026 do curso de Tecnologia em Inteligência Artificial. Cobrem programas de terminal, manipulação de strings, integração de APIs com modelos de linguagem e function calling.

---

## Projetos

| Projeto | Descrição | Stack |
|---|---|---|
| [Projeto Agente IA](projeto-agente-ia) | Assistente de terminal que usa function calling para executar ferramentas locais em Python (hora atual) | Python, OpenRouter |
| [Projeto Assistente IA](projeto-assistente-ia) | Chatbot de terminal com persona de professor de programação e histórico de conversa | Python, OpenRouter |
| [Projeto Criptografia](projeto-criptografia) | Cifra de César: criptografa com chave personalizada e descriptografa por força bruta | Python |
| [Projeto Jogo do Adivinha](projeto-jogo-adivinha) | Jogo de adivinhar número com dicas e recorde de tentativas | Python |

---

## Como executar

```bash
git clone https://github.com/pedro-vignoli/Projetos-Python.git
cd Projetos-Python
pip install -r requirements.txt
```

Rode qualquer projeto a partir da sua pasta:

```bash
cd projeto-criptografia
python main.py
```

Os dois projetos de IA precisam de uma chave do OpenRouter na variável de ambiente `OPENROUTER_API_KEY`.

---

## Estrutura

```
Projetos-Python/
|-- projeto-agente-ia/
|-- projeto-assistente-ia/
|-- projeto-criptografia/
|-- projeto-jogo-adivinha/
|-- requirements.txt
|-- README.md
`-- README.pt-BR.md
```

---

Tecnologia em Inteligência Artificial, 2º semestre de 2026.
