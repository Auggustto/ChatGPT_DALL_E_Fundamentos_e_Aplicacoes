import openai

openai.api_key = "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"

response = openai.Completion.create(model="text-davinci-003", prompt="Você pode explicar o que é um transformer no contexto de NLP")
print(response.choices[0].text)