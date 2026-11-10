**English** | [Português](#português)

# Projeto Assistente IA

Terminal chatbot built on the OpenRouter API with a programming-teacher persona: patient, didactic and focused on good practices.

- Persona set through the system prompt.
- Keeps the conversation history, so follow-up questions work.
- Interactive loop until you type `sair`.
- If `OPENROUTER_API_KEY` is not set, the script asks for the key on start.

Run:

```bash
pip install openai
export OPENROUTER_API_KEY="your_key"     # PowerShell: $env:OPENROUTER_API_KEY="your_key"
python main.py
```

---

# Português

Chatbot de terminal feito com a API do OpenRouter, com persona de professor de programação: paciente, didático e focado em boas práticas.

- Persona definida pelo prompt de sistema.
- Mantém o histórico da conversa, então perguntas em sequência funcionam.
- Loop interativo até você digitar `sair`.
- Se `OPENROUTER_API_KEY` não estiver definida, o script pede a chave ao iniciar.

Executar:

```bash
pip install openai
export OPENROUTER_API_KEY="sua_chave"     # PowerShell: $env:OPENROUTER_API_KEY="sua_chave"
python main.py
```
