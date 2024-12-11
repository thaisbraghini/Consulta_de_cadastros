async function getDados() {
    //faz a chamada em ao endpoint Flask
    const response = await fetch('http://127.0.0.1:5000/soma')
    // verificar se a resposta foi bem-sucedida
    if (response.ok) {
        const dados = await response.text()
        console.log(dados)
        document.getElementById('saida').textContent = dados
    }
}

async function buscacliente() {
    const documento = document.getElementById('cpf').value;
    if (!documento){
        alert("Por favor insira um CPF");
        return;
    }
    console.log(documento);
    const response = await fetch(`http://127.0.0.1:5000/consulta?documento=${documento}`);
    const dados = await response.json();
    console.log(dados);
    document.getElementById('face').src = dados.face
    document.getElementById('nome').textContent = dados.nome
    document.getElementById('nascimento').textContent = dados.data_nascimento
    document.getElementById('email').textContent = dados.email
}

async function cadastrarcliente() {
    const documento = document.getElementById('cadcpf').value;
    if (!documento){
        alert("Deseja cadastrar um cliente?");
        return;
    }

    const cpf = document.getElementById('cadcpf').value;
    const nome = document.getElementById('cadnome').value;
    const data_nascimento = document.getElementById('cadnascimento').value;
    const email = document.getElementById('cademail').value;


    // criar a estrutra que definimos no j.son

    const payload = {
        cpf,
        dados:{
            nome,
            data_nascimento,
            email,
        }
    };

    // fazer a requisição no bakend

    const response = await fetch('http://127.0.0.1:5000/cadastro', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });
}