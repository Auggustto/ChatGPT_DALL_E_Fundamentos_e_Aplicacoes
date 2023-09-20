# Fine-tuning

O ajuste fino permite que você aproveite melhor os modelos disponíveis por meio da API, fornecendo:

1° Resultados de maior qualidade do que solicitar
2° Capacidade de treinar com mais exemplos do que cabem em um prompt
3° 2Economia de token devido a prompts mais curtos
4° Solicitações de menor latência

O ajuste fino melhora o aprendizado em poucas tentativas, treinando em muito mais exemplos do que cabem no prompt, permitindo que você obtenha melhores resultados em um amplo número de tarefas. Depois que um modelo tiver sido ajustado, você não precisará fornecer tantos exemplos no prompt. Isso economiza custos e permite solicitações de menor latência.

Em alto nível, o ajuste fino envolve as seguintes etapas:

1° Preparar e fazer upload de dados de treinamento
2° Treine um novo modelo ajustado
3° Use seu modelo ajustado

Quais modelos podem ser ajustados?

O ajuste fino está atualmente disponível para os seguintes modelos:

    gpt-3.5-turbo-0613(recomendado)
    babbage-002
    davinci-002

Esperamos gpt-3.5-turboser o modelo certo para a maioria dos usuários em termos de resultados e facilidade de uso, a menos que você esteja migrando um modelo herdado e ajustado.

Quando usar o ajuste fino

O ajuste fino dos modelos GPT pode torná-los melhores para aplicações específicas, mas requer um investimento cuidadoso de tempo e esforço. Recomendamos primeiro tentar obter bons resultados com engenharia de prompt, encadeamento de prompt (dividindo tarefas complexas em vários prompts) e chamada de função , sendo os principais motivos:

    Há muitas tarefas para as quais nossos modelos podem inicialmente parecer não ter um bom desempenho, mas com melhor orientação podemos alcançar resultados muito melhores e potencialmente não precisamos de ajustes finos
    A iteração sobre prompts e outras táticas tem um ciclo de feedback muito mais rápido do que a iteração com ajuste fino, que requer a criação de conjuntos de dados e a execução de jobs de treinamento
    Nos casos em que o ajuste fino ainda é necessário, o trabalho inicial de engenharia imediata não é desperdiçado - normalmente vemos melhores resultados quando usamos um bom prompt nos dados de ajuste fino (ou combinando encadeamento de prompt/uso de ferramenta com ajuste fino)

Nosso guia de práticas recomendadas de GPT fornece informações básicas sobre algumas das estratégias e táticas mais eficazes para obter melhor desempenho sem ajustes finos. Você pode achar útil iterar rapidamente os prompts em nosso playground .