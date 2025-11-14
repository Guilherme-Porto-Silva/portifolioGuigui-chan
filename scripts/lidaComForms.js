const formulario = document.getElementById("formulario");

const interesseInput = document.getElementById("interesseInput");

const ofertaInput = document.getElementById("ofertaInput");

const frequenciaInput = document.getElementById("frequenciaInput");

const emailInput = document.getElementById("emailInput");



async function manusearFormulario(event) {

    // Impede o formulário de recarregar a página
    event.preventDefault(); 
    
    
    
    const dadosFormulario = {

        interesse: interesseInput.value,

        oferta: ofertaInput.value,

        frequencia: frequenciaInput.value,

        email: emailInput.value
    };

    try {
        
        const response = await fetch('/api/forms', {// referência presente no flask.py

            method: 'POST',

            headers: {

                'Content-Type': 'application/json',

            },

             body: JSON.stringify(dadosFormulario),
        });

        formulario.reset();
        
        return response;

    }
    
    catch (error) {

        console.error('Erro no processamento:', error);

        alert('Ocorreu um erro. Tente novamente.\n\nSe souberes o que é o console do JavaScript, podes lê-lo, para saber qual foi o erro.');
    }
}



async function responderFormulario(manusearFormularioResposta) {

    try {
          const resposta = await manusearFormularioResposta;

        // Pode não ter JSON se houve erro no fetch do backend
        const emailEsqueleto = await resposta.json();

        // Tratamento de erros vindos do Flask
        if (!resposta.ok) {

            alert("O servidor encontrou um problema:\n\n" + JSON.stringify(json, null, 2));
            
            return;
        }

        
        
        console.log("E-mail gerado pelo backend:", emailEsqueleto);

        // Envia o email chamando o endpoint real de envio
        const enviar = await fetch("/api/send_email", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },
            
            body: JSON.stringify(emailEsqueleto) // Passa assunto, corpo e destinatário
        });

        if (!enviar.ok) {

            const erro = await enviar.json();

            alert("Falha ao enviar o e-mail:\n\n" + JSON.stringify(erro, null, 2));

            return;
        }

        alert("E-mail enviado com sucesso!");

    }
    
    catch (erro) {

        console.error("Erro no responderFormulario:", erro);
        
        alert("Erro inesperado ao tentar responder o formulário.");
    }
}



formulario.addEventListener("submit", () => {

        responderFormulario(manusearFormulario(evento));
});

document.getElementById("enviar").addEventListener("keydown", (evento) => {

    if (evento.key === "Enter" || evento.key === " " || evento.key === "z") {

        responderFormulario(manusearFormulario(evento));
    }
});