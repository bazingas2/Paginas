import tkinter as tk
import random
from math import pi, sin, cos
import time


def gerar_numero_roleta():
    return random.randint(1, 20)


def animar_giro():
    resultado_final = gerar_numero_roleta()
    angulo_atual = 0
    voltas_totais = 30 + resultado_final  # Total de passos do giro

    # Loop para realizar a animação de giro
    for i in range(voltas_totais):
        canvas.delete("all")
        desenhar_seta()

        # Atualiza o ângulo atual para criar o movimento
        angulo_atual += 18  # Incremento por divisão (18°)

        # Chama a função de desenho com o ângulo atualizado
        desenhar_roleta(angulo_atual % 360)

        # Ajusta o tempo para criar a desaceleração natural
        delay = 0.01 + (i / voltas_totais) * 0.05
        window.update()
        time.sleep(delay)

    # Mostra o número final sorteado
    canvas.delete("all")
    desenhar_seta()
    desenhar_roleta((resultado_final - 1) * 18)  # Ajusta para o número final
    label_resultado.config(text=f"Número sorteado: {resultado_final}")


def desenhar_roleta(angulo):
    # Desenha o círculo da roleta com divisões estilizadas
    canvas.create_oval(50, 50, 250, 250, fill="lightblue", outline="blue", width=3)
    for i in range(20):
        angulo_inicio = pi / 180 * (i * 18 + angulo)
        angulo_fim = pi / 180 * ((i + 1) * 18 + angulo)

        # Calcula coordenadas para as divisões da roleta
        x1 = 150 + 100 * cos(angulo_inicio)
        y1 = 150 + 100 * sin(angulo_inicio)
        x2 = 150 + 100 * cos(angulo_fim)
        y2 = 150 + 100 * sin(angulo_fim)

        # Define cores alternadas para as divisões
        cor = "white" if i % 2 == 0 else "lightgreen"
        canvas.create_polygon(150, 150, x1, y1, x2, y2, fill=cor, outline="black")

        # Adiciona números rotativos corretamente
        x_texto = 150 + 70 * cos(angulo_inicio + pi / 20)
        y_texto = 150 + 70 * sin(angulo_inicio + pi / 20)
        canvas.create_text(x_texto, y_texto, text=str(i + 1), fill="black", font=("Arial", 10, "bold"))


def desenhar_seta():
    # Desenha uma seta fixa no topo da roleta
    canvas.create_polygon(140, 30, 150, 50, 160, 30, fill="red", outline="black")


# Configuração da janela principal
window = tk.Tk()
window.title("Roleta Dinâmica")

# Canvas para desenhar a roleta
canvas = tk.Canvas(window, width=300, height=300, bg="white")
canvas.pack()

# Botão para rodar a roleta
botao = tk.Button(window, text="Rodar Roleta", command=animar_giro, font=("Arial", 14), bg="green", fg="white")
botao.pack(pady=10)

# Label para exibir o resultado
label_resultado = tk.Label(window, text="Clique no botão para rodar a roleta!", font=("Arial", 14))
label_resultado.pack()

# Desenha a roleta inicialmente
desenhar_seta()
desenhar_roleta(0)

# Executa a interface gráfica
window.mainloop()
