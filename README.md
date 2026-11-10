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

**English** | [Português](README.pt-BR.md)

---

## About

Hands-on Python projects built during the 2nd semester of 2026 in the Technology in Artificial Intelligence degree. They cover terminal programs, string manipulation, API integration with language models and function calling.

---

## Projects

| Project | Description | Stack |
|---|---|---|
| [Projeto Agente IA](projeto-agente-ia) | Terminal assistant that uses function calling to run local Python tools (current time) | Python, OpenRouter |
| [Projeto Assistente IA](projeto-assistente-ia) | Terminal chatbot with a patient programming-teacher persona and conversation history | Python, OpenRouter |
| [Projeto Criptografia](projeto-criptografia) | Caesar cipher: encrypt with a custom key and decrypt by brute force | Python |
| [Projeto Jogo do Adivinha](projeto-jogo-adivinha) | Number guessing game with hints and a best-score record | Python |

---

## How to run

```bash
git clone https://github.com/pedro-vignoli/Projetos-Python.git
cd Projetos-Python
pip install -r requirements.txt
```

Run any project from its folder:

```bash
cd projeto-criptografia
python main.py
```

The two AI projects need an OpenRouter API key in the `OPENROUTER_API_KEY` environment variable.

---

## Structure

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

Technology in Artificial Intelligence, 2nd semester of 2026.
