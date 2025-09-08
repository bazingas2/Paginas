from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Cardápio de lanches
cardapio = {
    "1": {"nome": "X-Burger", "preco": 10.00},
    "2": {"nome": "X-Salada", "preco": 12.00},
    "3": {"nome": "Hot Dog", "preco": 8.00},
    "4": {"nome": "Refrigerante", "preco": 5.00},
    "5": {"nome": "Suco Natural", "preco": 6.00},
}

# Rota principal (cardápio)
@app.route("/")
def index():
    return render_template("index.html", cardapio=cardapio)

# Rota para processar o pedido
@app.route("/pedido", methods=["POST"])
def pedido():
    lanche_id = request.form.get("lanche_id")
    quantidade = int(request.form.get("quantidade", 1))

    if lanche_id in cardapio:
        lanche = cardapio[lanche_id]
        total = lanche["preco"] * quantidade
        return render_template("pedido.html", lanche=lanche, quantidade=quantidade, total=total)
    else:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)