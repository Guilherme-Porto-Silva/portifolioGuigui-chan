from flask import Flask, request, jsonify

from groq import Groq

import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))



def analise_de_interesse(dados):
    
    completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "system",
        "content": """
        
        Você é um analista de interesses do grupo de recursos humanos de uma empresa.
        Seu trabalho é descobrir se as pessoas que enviaram respostas de um formulário para essa 
        empresa querem contratar os serviços dela e classificar o nível de interesse delas.
        
        Quando uma pessoa que enviou uma resposta do formulário da sua empresa quer muito contratar 
        os serviços dela, você envia 'interesse alto' (para outro trabalhador da empresa).
        
        Quando uma pessoa que enviou uma resposta para a sua empresa nem quer contratar os serviços dela, 
        você envia 'não quer' (para outro trabalhador da empresa).
        
        Se quem enviou a resposta até quer contratar os serviços mais seu interesse não é lá dos maiores, 
        você envia 'interesse baixo'.
        
        Vou te dar alguns exemplos, para você entender melhor:
        
        respostas do um formulário: 

            interesse: ,

            oferta: ,

            frequencia: ,

            email: 
        
        o que você responderia:
        
        interesse alto
        
        respostas do um formulário: 

            interesse: ,

            oferta: ,

            frequencia: ,

            email: 
        
        o que você responderia:
        
        não quer
        
        respostas do um formulário: 

            interesse: ,

            oferta: ,

            frequencia: ,

            email: 
        
        o que você responderia:
        
        interesse baixo
        
        """
      },
      {
        "role": "user",
        "content": f"respostas do um formulário: {dados}"
      }
    ],
    temperature=1,
    max_completion_tokens=50,
    top_p=1,
    reasoning_effort="medium",
    stream=False,
    stop=None
    
    )

    return completion.choices[0].message.content



def interesse_alto(email_endereco, interesse):
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
        {
            "role": "system",
            "content": """Você é um redator de e-mails profissional.
            Seu trabalho é estabelecer contatos diretos, profissionais,
            educados e humanizados entre vendedores e consumidores."""
        },
        {
            "role": "user",
            "content": f"""Eu fiz um formulário que pedia
            informações referentes ao interesse tido pelas
            pessoas que vissem em contratar meus serviços.
            
            O usuário do e-mail '{email_endereco}' preencheu o campo que
            perguntava quais serviços meus ele queria utilizar da
            seguinte forma: {interesse}
            
            Redija o corpo - e apenas o corpo - de um e-mail que eu
            possa mandar para essa pessoa, para terminar de fechar um
            contrato com ela.
            
            Não feche o contrato em si nesse e-mail, apenas deixe bem claro
            o meu interesse em dar prosseguimento à conversa.
            
            Peça à pessoa para enviar um e-mail para 
            guiportosilva2@gmail.com, que é o meu e-mail pessoal,
            para darmos prosseguimento à conversa.
            
            Mantenha em mente que será uma mensagem de negócios, o que exige um
            tom de fala formal e educado.
            
            Se e somente se o e-mail '{email_endereco}' te fizer lembrar de algum 
            nome de pessoa específico, então utilize esse nome para chamar o 
            leitor da mensagem, quando e somente quando chamar o nome dele fizer
            sentido no contexto da mensagem escrita."""
        }
        ],
        temperature=1,
        max_completion_tokens=500,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )
    
    email_corpo = completion.choices[0].message.content
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
        {
            "role": "system",
            "content": """Você é um redator de e-mails profissional.
            Seu trabalho é estabelecer contatos diretos, profissionais,
            educados e humanizados entre vendedores e consumidores."""
        },
        {
            "role": "user",
            "content": f"""Redija o que será colocado no campo 'Assunto' de uma mensagem de e-mail.
            
            Não redija nada além do que será colocado no campo 'Assunto' dessa mensagem de e-mail.
            
            O corpo dessa mensagem de e-mail é o seguinte:
            
            {email_corpo}"""
        }
        ],
        temperature=1,
        max_completion_tokens=50,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )
    
    email_assunto = completion.choices[0].message.content
    
    return {
    "assunto": email_assunto,
    "corpo": email_corpo,
    "para_quem_mandar": email_endereco
}



def interesse_baixo(email_endereco, oferta, frequencia):
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": """Você é um redator de e-mails profissional.
                Seu trabalho é escrever mensagens educadas, formais e humanizadas,
                ajudando empresas a estabelecer contato com potenciais clientes."""
            },
            {
                "role": "user",
                "content": f"""Estou entrando em contato com uma pessoa que demonstrou
                algum interesse em contratar meus serviços, mas cujo nível de interesse
                não foi muito alto. Ela respondeu o formulário da seguinte forma:

                - E-mail do potencial cliente: {email_endereco}
                - Oferta que ela descreveu: {oferta}
                - Frequência desejada: {frequencia}

                Quero que você escreva o corpo — e apenas o corpo — de um e-mail com tom
                educado, formal e cordial. A mensagem deve:

                1. Reconhecer que o interesse dela existe, mas é baixo.
                2. De modo gentil, sugerir que ela explore mais sobre meu trabalho, meu portfólio,
                   ou outras ofertas, para ajudá-la a descobrir se há algo que realmente combine
                   com suas necessidades.
                3. Mostre disposição para conversar mais caso ela queira.
                4. Não feche contrato nem pressione; apenas incentive.
                5. Não trate a oferta como “bosta”, mas capture o espírito da docstring
                   (uma oferta fraca → resposta educada que aponta caminhos melhores).
                6. Manter tom profissional e respeitoso.

                Por fim, peça que ela responda diretamente para meu e-mail pessoal:
                guiportosilva2@gmail.com, caso queira conversar mais."""
            }
        ],
        temperature=1,
        max_completion_tokens=500,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )

    email_corpo = completion.choices[0].message.content

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": """Você é um redator de e-mails profissional.
                Seu trabalho é escrever títulos claros, objetivos e compatíveis
                com o tom profissional do corpo do e-mail."""
            },
            {
                "role": "user",
                "content": f"""Redija apenas o que será colocado no campo 'Assunto' de um e-mail.
                O corpo da mensagem é o seguinte:

                {email_corpo}"""
            }
        ],
        temperature=1,
        max_completion_tokens=80,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )

    email_assunto = completion.choices[0].message.content

    return {
        "assunto": email_assunto,
        "corpo": email_corpo,
        "para_quem_mandar": email_endereco
    }



def obrigado_mas_tchau(email_endereco):
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": """Você é um redator de e-mails profissional.
                Seu trabalho é escrever mensagens gentis, educadas e
                humanizadas, mantendo sempre um tom cordial."""
            },
            {
                "role": "user",
                "content": f"""Quero enviar um e-mail de despedida para uma pessoa que,
                ao preencher meu formulário, deixou claro que não deseja contratar
                nenhum dos meus serviços. 

                - E-mail do potencial cliente: {email_endereco}

                Redija o corpo — e apenas o corpo — de um e-mail curto, educado,
                cordial e simpático, agradecendo pelo tempo da pessoa e reconhecendo
                claramente que ela não deseja prosseguir. A mensagem deve:

                1. Ser amigável, sem piadas internas ou gírias excessivas.
                2. Ter leveza e simpatia (um “fofo” profissional).
                3. Mostrar que a porta segue aberta, caso ela mude de ideia no futuro.
                4. Transmitir positividade na despedida.
                5. Não tentar vender nada.

                Não utilize tom informal demais, nem linguagem ríspida. 
                Apenas mantenha um clima amistoso e bem educado."""
            }
        ],
        temperature=1,
        max_completion_tokens=400,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )

    email_corpo = completion.choices[0].message.content

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": """Você é um redator de e-mails profissional.
                Seu trabalho é escrever títulos adequados, respeitosos,
                simples e compatíveis com o corpo de uma mensagem formal."""
            },
            {
                "role": "user",
                "content": f"""Redija apenas o campo 'Assunto' de um e-mail.
                O corpo da mensagem é:

                {email_corpo}"""
            }
        ],
        temperature=1,
        max_completion_tokens=80,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )

    email_assunto = completion.choices[0].message.content

    return {
        "assunto": email_assunto,
        "corpo": email_corpo,
        "para_quem_mandar": email_endereco
    }
           
            

app = Flask(__name__)
    
@app.route('/api/forms', methods=['POST'])# referência vista pelo lidaComForms.js

def handle_analise():
    
    dados = request.json# aquela const dadosFormulario do lidaComForms.js
    
    if not dados:
        
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    interesse = dados.get("interesse")

    if not interesse:
        
        return jsonify({"temosUmProblema": "Campo 'interesse' não foi preenchido"}), 400

    classeInteresse = analise_de_interesse(dados).lower()

    if "alto" in classeInteresse:
        
        response = interesse_alto(dados.get("email"), dados.get("interesse"))
        
    elif "baixo" in classeInteresse:
        
        response = interesse_baixo(dados.get("email"), dados.get("oferta"), dados.get("frequencia"))
        
    elif "não quer" in classeInteresse or "nao quer" in classeInteresse or "nem quer" in classeInteresse:
        
        response = obrigado_mas_tchau(dados.get("email"))
        
    else:
        
        response = {"temosUmProblema": "Nem com a condicional mais robusta a resposta do modelo se encaixou no que eu precisava"}
    
    return jsonify(response)