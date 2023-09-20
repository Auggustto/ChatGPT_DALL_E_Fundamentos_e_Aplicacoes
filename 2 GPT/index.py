import openai

openai.api_key = "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"

response = openai.Completion.create(
    # Definindo o modelo que vaiser utilizado
    model="text-davinci-003", 
    # Passando o que vai ser perguntado
    prompt="Você pode explicar o que é um transformer no contexto de NLP",
    # Aumentando o maximo de tokens, com isso as respostas vem completas
    max_tokens=1000
    )
print(response.choices[0].text)