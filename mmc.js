function calcularIMC() {
    const peso = document.getElementById("peso").value;
    const altura = document.getElementById("altura").value;

    if (peso && altura) {
        const imc = peso / (altura * altura);
        alert(`Seu IMC é: ${imc.toFixed(2)}`);
    } else {
        alert("Por favor, insira valores válidos para peso e altura.");
    }
}
