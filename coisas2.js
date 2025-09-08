const cliente = {
    nome: "Robson",
    idade: 29,
    cpf: "05086678086",
    email: "robinho@polo.com.br",
};

const cliente2 = {
    nome: "Nãosei",
    idade: 50,
    cpf: "12345678998",
    email: "vaisaber@polo.com.br"
};

const cliente3 = {
    nome: "Carlos",
    idade: 35,
    cpf: "98765432100",
    email: "carlos@polo.com.br"
};

const cliente4 = {
    nome: "Amanda",
    idade: 27,
    cpf: "45678912344",
    email: "amanda@polo.com.br"
};

const clientes = [cliente, cliente2, cliente3, cliente4];

const chaves = ["nome", "idade", "cpf", "email"];
clientes.forEach((cliente) => {
    chaves.forEach((chave) => {
        console.log(`O campo ${chave} tem valor ${cliente[chave]}`);
    });
});
