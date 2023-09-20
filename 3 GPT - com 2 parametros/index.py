import openai
from calls import call_1, call_2

openai.api_key = "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"

response = openai.Completion.create(
    # Definindo o modelo que vaiser utilizado
    model="text-davinci-003",
    # Passando o que vai ser perguntado
    prompt= f"\
        Com base na cseguinte chamada telefonica,\
        identifique o nome do atendente no inicio da chamada,\
        nome da empresa,\
        nome do cliente,\
        O agente atendeu ao chamado sem deixar o cliente esperando?,\
        O agente fala o valor da divida?,\
        O agente pergunta ao cliente sobre o CPF?,\
        O agente pergunta sobre CNPJ?,\
        O agente informou ao cliente sobre a pesquisa de satisfação?,\
        O agente fala as formas de parcelamentos?,\
        O Cliente aceita o parcelamento?,\
        O agente tentou fazer o cliente encerrar o contato?,\
        O Cliente fala que vai abrir uma reclamação no reclameaqui?,\
        O agente usa expressões de gentileza, como 'por favor', 'obrigado', 'gostaria', 'compreendo'? e retorne a respostas com True e False \
        {call_1}",
    # Aumentando o maximo de tokens, com isso as respostas vem completas
    max_tokens=1000,
    # Ajustando a temperatura
    temperature=0,
    # Aumentando o numero de respostas
    n=4
)

# Pegando a resposta de um retorno
# print(response)
print(response.choices[0].text)


# Pegando a respostas de todos os retornos
# for choice in range(len(response.choices)):
#     print(response.choices[choice].text)