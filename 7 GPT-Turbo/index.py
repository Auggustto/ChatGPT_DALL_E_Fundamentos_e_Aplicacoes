import openai

# openai.api_key = "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"
openai.api_key = "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" # Emp

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        # Indicar a função ou comportamento do modelo
        {"role":"system","content":"Você está respondendo perguntas"},
        # Passa a pergunta gerada por modelos ou usuarios 
        {"role":"user","content":"Quem foi Carl Sagan?"},
        # Passa o contexto do chat
        {"role":"assistant","content":"Carl Sagan foi um cientista"},
        # # Passa a pergunta gerada por modelos ou usuarios 
        {"role":"user","content":"Quais livros ele publicou ?"},
        ],
    temperature = 0
)
# print(response)
print(response["choices"][0]["message"]["content"])
