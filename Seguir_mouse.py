import turtle

# Configurar a tela
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Objeto Seguindo o Mouse")
screen.tracer(0)  # Desativar animação automática para melhor desempenho

# Criar o "animal"
follower = turtle.Turtle()
follower.shape("turtle")  # Formato de tartaruga
follower.color("lime")
follower.penup()  # Não desenha enquanto se move
follower.speed(0)  # Velocidade máxima

# Função para atualizar a posição do seguidor suavemente
def follow_mouse():
    x, y = screen._root.winfo_pointerx() - screen.window_width() // 2, \
           -(screen._root.winfo_pointery() - screen.window_height() // 2)
    current_x, current_y = follower.position()
    follower.setx(current_x + (x - current_x) * 0.1)
    follower.sety(current_y + (y - current_y) * 0.1)
    screen.update()
    screen.ontimer(follow_mouse, 20)  # Chamar a função a cada 20ms

# Iniciar o movimento automático
follow_mouse()

# Manter a janela aberta
screen.mainloop()
