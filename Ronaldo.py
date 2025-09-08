import turtle

# Configurar a tela
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Seguindo o Mouse Automaticamente")
screen.tracer(0)  # Desativar animação automática para mais fluidez

# Criar a tartaruga
follower = turtle.Turtle()
follower.shape("circle")  # Forma do objeto que segue o mouse
follower.color("cyan")
follower.penup()  # Não desenha enquanto se move
follower.speed(0)  # Velocidade máxima

# Função para mover a tartaruga suavemente em direção ao mouse
def follow_mouse():
    x, y = screen._root.winfo_pointerx() - screen.window_width() // 2, -(screen._root.winfo_pointery() - screen.window_height() // 2)
    current_x, current_y = follower.position()
    # Atualizar posição com suavidade
    follower.setx(current_x + (x - current_x) * 0.2)
follow-mouse
 seguir ncurrent.linear .
