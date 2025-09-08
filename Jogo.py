import pygame
import sys

# Inicializar o pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Hollow Knight Simples")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Taxa de atualização
relogio = pygame.time.Clock()

# Carregar sprites
sprite_jogador = pygame.image.load("player.png").convert_alpha()
sprite_inimigo = pygame.image.load("enemy.png").convert_alpha()

# Personagem
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(sprite_jogador, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (100, ALTURA - 100)
        self.vel_y = 0
        self.vel_x = 5
        self.no_chao = False
        self.vida = 3  # Pontos de vida
        self.pontos = 0  # Pontos para progresso

    def atualizar(self, teclas):
        # Movimento horizontal
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.vel_x
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.vel_x

        # Pulo
        if teclas[pygame.K_SPACE] and self.no_chao:
            self.vel_y = -15
            self.no_chao = False

        # Gravidade
        self.vel_y += 0.8
        self.rect.y += self.vel_y

        # Colisão com o chão
        if self.rect.bottom > ALTURA - 50:
            self.rect.bottom = ALTURA - 50
            self.no_chao = True
            self.vel_y = 0

        # Limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA

# Inimigos
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(sprite_inimigo, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel_x = 2

    def atualizar(self):
        self.rect.x += self.vel_x
        if self.rect.left < 0 or self.rect.right > LARGURA:
            self.vel_x *= -1

# Plataformas
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Coletáveis
class Coletavel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Sistema de combate e coleta
def checar_eventos(jogador, inimigos, coletaveis):
    if pygame.sprite.spritecollide(jogador, inimigos, False):
        jogador.vida -= 1
        print(f"Vida do jogador: {jogador.vida}")
        if jogador.vida <= 0:
            print("Você perdeu!")
            pygame.quit()
            sys.exit()

    if pygame.sprite.spritecollide(jogador, coletaveis, True):
        jogador.pontos += 1
        print(f"Pontos: {jogador.pontos}")

# Grupos de sprites
jogador = Jogador()
todas_sprites = pygame.sprite.Group()
todas_sprites.add(jogador)

inimigos = pygame.sprite.Group()
for i in range(3):  # Adiciona 3 inimigos
    inimigo = Inimigo(200 + i * 150, ALTURA - 100)
    inimigos.add(inimigo)
    todas_sprites.add(inimigo)

plataformas = pygame.sprite.Group()
plataforma = Plataforma(100, ALTURA - 150, 300, 20)
plataformas.add(plataforma)
todas_sprites.add(plataforma)

coletaveis = pygame.sprite.Group()
coletavel = Coletavel(400, ALTURA - 170)
coletaveis.add(coletavel)
todas_sprites.add(coletavel)

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Entrada de teclado
    teclas = pygame.key.get_pressed()

    # Atualizações
    jogador.atualizar(teclas)
    inimigos.update()
    checar_eventos(jogador, inimigos, coletaveis)

    # Desenhar na tela
    tela.fill(PRETO)
    todas_sprites.draw(tela)

    # Mostrar barra de vida
    for i in range(jogador.vida):
        pygame.draw.rect(tela, VERMELHO, (10 + i * 40, 10, 30, 30))

    pygame.display.flip()
    relogio.tick(60)
