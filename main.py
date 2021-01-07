# Initializate
import pygame

pygame.init()

# Display
screen = pygame.display.set_mode((972, 460))

# background
background = pygame.image.load('background1.png')

pygame.display.set_caption("Game")
branco = (255, 255, 255)
# importar imagens player
walkRight = [pygame.image.load('Game/R/R1.png'), pygame.image.load('Game/R/R2.png'), pygame.image.load('Game/R/R3.png'),
             pygame.image.load('Game/R/R4.png'), pygame.image.load('Game/R/R5.png'), pygame.image.load('Game/R/R6.png'),
             pygame.image.load('Game/R/R7.png'), pygame.image.load('Game/R/R8.png'), pygame.image.load('Game/R/R9.png')]

walkLeft = [pygame.image.load('Game/L/L1.png'), pygame.image.load('Game/L/L2.png'), pygame.image.load('Game/L/L3.png'),
            pygame.image.load('Game/L/L4.png'), pygame.image.load('Game/L/L5.png'), pygame.image.load('Game/L/L6.png'),
            pygame.image.load('Game/L/L7.png'), pygame.image.load('Game/L/L8.png'), pygame.image.load('Game/L/L9.png')]

score = 0  # pontuaçã0

clock = pygame.time.Clock()


# Players
class character(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.jumpCount = 10
        self.Left = False
        self.Right = False
        self.isJump = False
        self.walkCount = 0
        self.facing = True
        self.hitbox = (self.x + 10, self.y, 20, 60)

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.facing:  # se player não está parado
            if self.Left:
                screen.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.Right:
                screen.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        else:
            if self.Left:
                screen.blit(walkLeft[0], (self.x, self.y))
            else:
                screen.blit(walkRight[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y, 20, 60)  # hitbox para checar colisão
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


class Goblin(object):
    GoblinLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'),
                  pygame.image.load('L3E.png'),
                  pygame.image.load('L4E.png'), pygame.image.load('L5E.png'),
                  pygame.image.load('L6E.png'),
                  pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                  pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    GoblinRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'),
                   pygame.image.load('R3E.png'),
                   pygame.image.load('R4E.png'), pygame.image.load('R5E.png'),
                   pygame.image.load('R6E.png'),
                   pygame.image.load('R7E.png.'), pygame.image.load('R8E.png.'), pygame.image.load('R9E.png.'),
                   pygame.image.load('R10E.png.'), pygame.image.load('R11E.png.')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.path = [self.x, self.end]  # inicio e fim do caminho
        self.vel = 3
        self.hitbox = (self.x + 7, self.y, 10, 60)

    def draw(self, screen):  # desenhar goblin
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            screen.blit(self.GoblinRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        else:
            screen.blit(self.GoblinLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)  # hitbox para checar colisão

        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        pygame.draw.rect(screen, (0, 255, 0), (self.hitbox[0], self.hitbox[1], 50, 10))  # healt box green
        pygame.draw.rect(screen, (255, 0, 0), (self.hitbox[0], self.hitbox[1], 50, 10))  # healt box red

        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


    def move(self):  # mover goblin
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:  # se onde esta não é maior que caminho
                self.x += self.vel

            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel

            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        print('hitted')


class projectile(object):
    def __init__(self, x, y, rai, cor, standing):
        self.x = x
        self.y = y
        self.rai = rai
        self.cor = cor
        self.standing = standing
        self.vel = 8 * standing

    def draw(self, scren):
        pygame.draw.circle(scren, self.cor, (self.x, self.y), self.rai)


def game_intro():  # tela inicial para jogo

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(branco)
        pygame.draw.rect(screen, (255, 0, 0), (200, 50, 100, 50))  # criar  butão
        mouse = pygame.mouse.get_pos()

        if 200 + 100 > mouse[0] > 200 and 50 + 50 > mouse[1] > 50:  # verificar se rato esta em cima do botão
            keepGoing = True

        clock.tick(15)
        pygame.display.update()


def redrawGameWindow():  # redesenhar tela
    screen.blit(pygame.transform.scale(background, (972, 460)), (0, 0))  # fundo
    text = font.render('Score:' + str(score), 1, (0, 0, 0))
    screen.blit(text, (390, 10 ))
    player.draw(screen)  # personagem principal
    enemy.draw(screen)  # inimigo

    for bullet in bullets:  # balas
        bullet.draw(screen)
    pygame.display.update()


# MainLoop
# Entities
font = pygame.font.SysFont('comicsans', 30, True, True)  # letra (tipo,tamanho,negirto)
player = character(90, 360, 64, 64, 5)
enemy = Goblin(100, 360, 64, 64, 450)
bullets = []
keepGoing = True
shootLoop = 0

while keepGoing:
    clock.tick(27)

    #para balas não serem desparadas todas ao mesmo tempo
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    for bullet in bullets:
        # verificar se bala colide com inimiigo
        if bullet.y < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y > enemy.hitbox[1]:  # hitbox[1] = x hitbox[3]
            if bullet.x > enemy.hitbox[0] and bullet.x < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
        if screen.get_width() > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if player.Left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(round(player.x + player.width // 2),
                                      round(player.y + player.height // 2), 6, (0, 0, 0), facing))
        shootLoop = 1

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.Left = True
        player.Right = False
        player.facing = False

    if keys[pygame.K_RIGHT] and player.x < screen.get_width() - player.width - player.vel:
        player.x += player.vel
        player.Right = True
        player.Left = False
        player.facing = False

    else:  # entra em loop nao deixa player deslocar a esquerda
        player.facing = True
        walkCount = 0

    if not player.isJump:
        if keys[pygame.K_UP]:
            player.isJump = True
            player.Right = False
            player.Left = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    redrawGameWindow()

pygame.quit()
