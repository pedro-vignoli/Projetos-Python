**English** | [Português](#português)

# Projeto Agente IA

Terminal assistant built on the OpenRouter API that uses function calling. The model can ask the program to run a local Python function (`obter_hora_atual`) and use the result in its answer.

- Study-assistant persona with simple, didactic explanations.
- Function calling: the model requests the local tool when it needs the current time.
- Interactive loop until you type `sair`.

Run:

```bash
pip install openai
export OPENROUTER_API_KEY="your_key"     # PowerShell: $env:OPENROUTER_API_KEY="your_key"
python main.py
```

Example:

```text
You: What time is it?
Assistant: It is 14:35.
```

---

# Português

Assistente de terminal feito com a API do OpenRouter que usa function calling. O modelo pode pedir para o programa executar uma função local em Python (`obter_hora_atual`) e usar o resultado na resposta.

- Persona de assistente de estudos, com explicações simples e didáticas.
- Function calling: o modelo chama a ferramenta local quando precisa da hora atual.
- Loop interativo até você digitar `sair`.

Executar:

```bash
pip install openai
export OPENROUTER_API_KEY="sua_chave"     # PowerShell: $env:OPENROUTER_API_KEY="sua_chave"
python main.py
```

Exemplo:

```text
Você: Que horas são agora?
Assistente: Agora são 14:35.
```
