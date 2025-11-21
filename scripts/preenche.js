const recipientePrincipal = document.getElementById('principal');

let certificados = [
    {
        titulo: "Carreira de Especialista em IA: Boas-vindas e primeiros passos da empresa - Alura",
        descricao1: "Gostaria de compartilhar que recebi uma nova certificação: Carreira Especialista em IA: Boas-vindas e primeiros passos da empresa Alura!",
        descricao2: "Essa é uma das 22 carreiras da plataforma de cursos online Alura, que oferece uma formação completa em Inteligência Artificial. A imagem que está ao lado é o certificado que recebi ao concluir essa etapa da carreira, a \"Boas-vindas e primeiros passos da empresa\".",
        origemImagem: "./imagens/especialistaIAboasVindas.png"
    },
    {
        titulo: "Java: criando a sua primeira aplicação da empresa - Alura",
        descricao1: "Gostaria de compartilhar que recebi uma nova certificação: Java: criando a sua primeira aplicação da empresa Alura!",
        descricao2: "Esse é um dos cursos da plataforma de cursos online Alura, que oferece uma formação completa em Java, com programação orientada a objetos. A imagem que está ao lado é o certificado que recebi ao concluir esse etapa do curso, a \"criando a sua primeira aplicação da empresa\".",
        origemImagem: "./imagens/javaPrimeiraAplicacao.png"
    },
    {
        titulo: "Java: Alura - primeiro da empresa",
        descricao1: "Gostaria de compartilhar que recebi uma nova certificação: Java: Alura - primeiro da empresa!",
        descricao2: "Esse é um dos cursos da plataforma de cursos online Alura, que oferece uma formação completa em Java, com programação orientada a objetos. A imagem que está ao lado é o certificado que recebi ao concluir esse etapa do curso, a \"primeiro da empresa\".",
        origemImagem: "./imagens/javaPrimeiroEmpresa.png"
    },
    {
        titulo: "Java: aplicando programação orientada a objetos - Alura",
        descricao1: "Gostaria de compartilhar que recebi uma nova certificação: Java: aplicando programação orientada a objetos Alura!",
        descricao2: "Esse é um dos cursos da plataforma de cursos online Alura, que oferece uma formação completa em Java, com programação orientada a objetos. A imagem que está ao lado é o certificado que recebi ao concluir esse etapa do curso, a \"aplicando programação orientada a objetos\".",
        origemImagem: "./imagens/aplicandoOOjava.png"
    },
    {
        titulo: "Python: aplicando programação orientada a objetos - Alura",
        descricao1: "Gostaria de compartilhar que recebi uma nova certificação: Python: aplicando programação orientada a objetos Alura!",
        descricao2: "Esse é um dos cursos da plataforma de cursos online Alura, que oferece uma formação completa em Python, com programação orientada a objetos. A imagem que está ao lado é o certificado que recebi ao concluir esse etapa do curso, a \"aplicando programação orientada a objetos\".",
        origemImagem: "./imagens/pythonOO.png"
    },
    {
        titulo: "Python: primeira aplicação - Alura",
        descricao1: "Gostaria de compartilhar que recebi uma nova certificação: Python: primeira aplicação Alura!",
        descricao2: "Esse é um dos cursos da plataforma de cursos online Alura, que oferece uma formação completa em Python, com programação orientada a objetos. A imagem que está ao lado é o certificado que recebi ao concluir esse etapa do curso, a \"primeira aplicação\".",
        origemImagem: "./imagens/pythonPrimeiraAplicacao.png"
    },
    {
        titulo: "Python: aplicando programação orientada a objetos - Alura",
        descricao1: "Gostaria de compartilhar que recebi uma nova certificação: Python: aplicando programação orientada a objetos Alura!",
        descricao2: "Esse é um dos cursos da plataforma de cursos online Alura, que oferece uma formação completa em Python, com programação orientada a objetos. A imagem que está ao lado é o certificado que recebi ao concluir esse etapa do curso, a \"aplicando programação orientada a objetos\".",
        origemImagem: "./imagens/pythonIAaplicada.png"
    },
    {
        titulo: "Engenharia de Prompt - Alura",
        descricao1: "Gostaria de compartilhar que recebi uma nova certificação: Engenharia de Prompt da Alura!",
        descricao2: "Esse é um dos cursos da plataforma de cursos online Alura, que ensina a conversar com as inteligências artificiais.",
        origemImagem: "./imagens/engenhariaPrompt.png"
    },
    {
        titulo: "JavaScript: programando a Orientação a Objetos - Alura",
        descricao1: "Gostaria de compartilhar que recebi uma nova certificação: JavaScript: programando a Orientação a Objetos da empresa Alura!",
        descricao2: "Esse é um dos cursos da plataforma de cursos online Alura, que ensina a usar a programação orientada a objetos em JavaScript.",
        origemImagem: "./imagens/objetosJavaScript.png"
    }
];


function criarCaixaCertificado(certificado) {

    const divLinha = document.createElement('div');

    divLinha.className = 'linha caixaCinzenta';

    const divColuna = document.createElement('div');
    
    divColuna.className = 'coluna';

    const h3 = document.createElement('h3');

    h3.textContent = certificado.titulo;

    const p1 = document.createElement('p');

    p1.textContent = certificado.descricao1;

    const p2 = document.createElement('p');

    p2.textContent = certificado.descricao2;

    divColuna.appendChild(h3);

    divColuna.appendChild(p1);

    divColuna.appendChild(p2);

    const imagem = document.createElement('img');

    imagem.src = certificado.origemImagem;

    imagem.alt = 'imagem do projeto';

    divLinha.appendChild(divColuna);
    
    divLinha.appendChild(imagem);

    return divLinha;
}


function preencherCertificados() {

    certificados.forEach( (certificado) => {
        
        recipientePrincipal.appendChild(criarCaixaCertificado(certificado));
    });
}

document.addEventListener('DOMContentLoaded', preencherCertificados);
