import openai
from CriandoumaClasseReutilizavelemPython import MyOpenIA

# openai.api_key = "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"
models_ia = "text-davinci-003"

chat = MyOpenIA("Aonde fica o Rio de Janeiro?", 
                models_ia, 
                1, 
                3000, 
                0, 
                "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"
                )

response = chat.CallGpt()
# print(response)

for value in response:
    print(value)