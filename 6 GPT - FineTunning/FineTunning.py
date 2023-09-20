import openai

openai.api_key = "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"

# Passando um contexto
contexto = """
Carl Segan foi um astrônomo americano, astrofísico e escritor. Ele foi um dos principais responsáveis pela popularização da astronomia moderna, escrevendo livros e aparecendo em programas de televisão. Segan foi um dos principais proponentes da missão Apollo 11, que levou os primeiros homens à Lua. Ele também foi um dos principais defensores da exploração espacial, acreditando que a humanidade deveria explorar o espaço para encontrar novas formas de vida. Segan foi um dos principais responsáveis pela criação do Observatório de Palomar, um dos maiores telescópios do mundo.
"""

response = openai.Completion.create(
    # Definindo o modelo que vaiser utilizado
    model="text-davinci-003",
    # Passando o que vai ser perguntado
    prompt= contexto + "Quantos livros ele escreveu",
    # Aumentando o maximo de tokens, com isso as respostas vem completas
    max_tokens=1000,
    # Ajustando a temperatura
    temperature=0,
    # Aumentando o numero de respostas
    n=4
)

print(response.choices[0].text)
