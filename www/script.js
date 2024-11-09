async function getDados() {
    // faz a chamada ao endpoint Flask
    const response = await fetch('http://127.0.0.1:5000/soma')

    // verificar se a resposta foi bem sucedida
    if (response.ok){
        const dados = await response.text()
        console.log(dados)
        document.getElementById('saida').textContent = dados
    }

}