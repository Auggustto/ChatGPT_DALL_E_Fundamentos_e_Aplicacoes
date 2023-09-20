import openai

class MyOpenIA():

    def __init__(self, prompt, model_ia, number_response, max_tokens, temperature, key):
        self.prompt = prompt
        self.model_ia = model_ia
        self.n = number_response
        self.max_tokens = max_tokens
        self.temperature = temperature
        # passando direto o atributo de key
        openai.api_key = key

    # Criando um metodo que le todas as propriedade acima e retorna o resultado
    def CallGpt(self):
        response = openai.Completion.create(
            prompt = self.prompt,
            model = self.model_ia,
            n = self.n,
            max_tokens = self.max_tokens,
            temperature = self.temperature   
        )

        return_response = []
        for a in range(len(response.choices)):
            return_response.append(response.choices[a].text)
            
        return return_response

