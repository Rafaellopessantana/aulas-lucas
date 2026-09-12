import pygame,random,json

pygame.init()
#cria a janela
janela = pygame.display.set_mode((700,700))
pygame.display.set_caption("jogo do sonic sem wifi")
executando = True
fonte = pygame.font.SysFont(None,48)
inicio = False
pontos = 0
pontos_txt = fonte.render("pontos: "+str(pontos),True,(0,0,0))
velocidade = 0.5
try:
    with open("melhor.json","r") as f:
      melhor = json.loads(f.read())
except:
    melhor = 0
melhor_txt = fonte.render("recorde: "+str(melhor),True,(0,0,0))
aperte_espaço = fonte.render("aperte espaço para iniciar",True,(255,255,255))
titulo = fonte.render("SONIC SEM WIFI",True,(0,0,0))
titulo = pygame.transform.scale(titulo,(400,200))
credito = fonte.render("por: rafa lopes studios",True,(0,0,0))
fundo_inicial = pygame.image.load("sprites/green hill zone.png")
fundo_inicial = pygame.transform.scale(fundo_inicial,(700,700))
dino = pygame.image.load("sprites/dino.webp")
dino = pygame.transform.scale(dino,(100,100))
sprite_correndo = 0
sprite_pulando = 0
sprite_background = 0
backgrounds = [pygame.image.load("sprites/green hill zone 1.png"),pygame.image.load("sprites/green hill zone 2.png"),pygame.image.load("sprites/green hill zone 3.png"),pygame.image.load("sprites/green hill zone 4.png"),pygame.image.load("sprites/green hill zone 5.png")]
sonic_correndo = [pygame.image.load("sprites/sonic correndo.gif"),pygame.image.load("sprites/sonic correndo 1.gif"),pygame.image.load("sprites/sonic correndo 2.gif"),pygame.image.load("sprites/sonic correndo 3.gif"),pygame.image.load("sprites/sonic correndo 2.gif")]
sonic_pulando = [pygame.image.load("sprites/sonic pulando 1.gif"),pygame.image.load("sprites/sonic pulando 0.5.gif"),pygame.image.load("sprites/sonic pulando 2.gif"),pygame.image.load("sprites/sonic pulando 0.5.gif"),pygame.image.load("sprites/sonic pulando 3.gif"),pygame.image.load("sprites/sonic pulando 0.5.gif")]
background = pygame.image.load("sprites/green hill zone.png")
background = pygame.transform.scale(background,(700,700))
sonic = pygame.image.load("sprites/sonic parado.gif")
sonic = pygame.transform.scale(sonic,(100,100))
y_sonic = 500
sonic_rolando = False
tempo_rolando = 0
invencivel = False
tipo = "normal"
robotinik = pygame.image.load("sprites/robotinik.png")
crabmeat = pygame.image.load("sprites/crabmeat.webp")
crabmeat = pygame.transform.scale(crabmeat,(150,50))
x_crabmeat = random.randint(800,2000)
motobug = pygame.image.load("sprites/motobug.png")
motobug = pygame.transform.scale(motobug,(150,50))
x_motobug = random.randint(800,2000)
crabmeat2 = pygame.image.load("sprites/crabmeat.webp")
crabmeat2 = pygame.transform.scale(crabmeat2,(150,50))
x_crabmeat2 = random.randint(800,2000)
motobug2 = pygame.image.load("sprites/motobug.png")
motobug2 = pygame.transform.scale(motobug2,(150,50))
x_motobug2 = random.randint(800,2000)
monitor = pygame.image.load("sprites/monitor.webp")
monitor = pygame.transform.scale(monitor,(100,100))
x_monitor = random.randint(1600,4000)
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            inicio = True
    janela.fill((0,0,255))
    janela.blit(fundo_inicial)
    janela.blit(titulo,(150,100))
    janela.blit(sonic,(200,300))
    janela.blit(dino,(350,300))
    janela.blit(aperte_espaço,(150,250))
    janela.blit(credito,(0,665))
    pygame.display.flip()
    if inicio:
        break
while executando:
    sprite_correndo += 1
    if sprite_correndo > 4:
        sprite_correndo = 0
    sprite_pulando += 1
    if sprite_pulando > 4:
        sprite_pulando = 0
    sprite_background += 1
    if sprite_background > 4:
        sprite_background = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not sonic_rolando:
                if y_sonic >= 500:
                    sonic = pygame.image.load("sprites/sonic pulando.gif")
                    sonic = pygame.transform.scale(sonic,(100,100))
                    y_sonic -= 100
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y_sonic = 500
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            sonic_rolando = True
            sonic = pygame.image.load("sprites/sonic rolando.gif")
            sonic = pygame.transform.scale(sonic,(100,100))
    hitbox_sonic = pygame.Rect(0,y_sonic,50,50)
    x_crabmeat -= velocidade
    hitbox_crabmeat = pygame.Rect(x_crabmeat,500,100,10)
    x_crabmeat2 -= velocidade
    hitbox_crabmeat2 = pygame.Rect(x_crabmeat2,500,100,10)
    x_motobug -= velocidade
    hitbox_motobug = pygame.Rect(x_motobug,500,100,10)
    x_motobug2 -= velocidade
    hitbox_motobug2 = pygame.Rect(x_motobug2,500,100,10)
    x_monitor -= velocidade / 2
    hitbox_monitor = pygame.Rect(x_motobug,500,100,100)
    background = backgrounds[sprite_background]
    background = pygame.transform.scale(background,(700,700))
    pontos_txt = fonte.render("pontos: "+str(int(pontos)),True,(0,0,0))
    janela.fill((0,0,255))
    janela.blit(background,(0,0))
    janela.blit(pontos_txt,(0,0))
    janela.blit(melhor_txt,(0,20))
    janela.blit(robotinik,(500,400))
    janela.blit(sonic,(0,y_sonic))
    janela.blit(crabmeat,(x_crabmeat,550))
    janela.blit(crabmeat2,(x_crabmeat2,550))
    janela.blit(motobug,(x_motobug,550))
    janela.blit(motobug2,(x_motobug2,550))
    janela.blit(monitor,(x_monitor,500))
    if hitbox_crabmeat.colliderect(hitbox_sonic):
        if sonic_rolando:
            x_crabmeat = -150
            tempo_rolando = 100
        elif invencivel:
            x_crabmeat = -150
            invencivel = False
        else:
            executando = False
    if hitbox_crabmeat2.colliderect(hitbox_sonic):
        if sonic_rolando:
            x_crabmeat2 = -150
            tempo_rolando = 100
        elif invencivel:
            x_crabmeat2 = -150
            invencivel = False
        else:
            executando = False
    if hitbox_motobug.colliderect(hitbox_sonic):
        if sonic_rolando:
            x_motobug = -150
            tempo_rolando = 100
        elif invencivel:
            x_motobug = -150
            invencivel = False
        else:
            executando = False
    if hitbox_motobug2.colliderect(hitbox_sonic):
        if sonic_rolando:
            x_motobug2 = -150
            tempo_rolando = 100
        elif invencivel:
            x_motobug2 = -150
            invencivel = False   
        else:
            executando = False
    if hitbox_monitor.colliderect(hitbox_sonic):
        if sonic_rolando:
            if tipo == "invencivel":
                invencivel = True
            else:
                pontos += 10
            tempo_rolando = 100
        x_monitor = -200
    if x_crabmeat <= -150:
        x_crabmeat = random.randint(800,2000)
    if x_crabmeat2 <= -150:
        x_crabmeat2 = random.randint(800,2000)
    if x_motobug <= -150:
        x_motobug = random.randint(800,2000)
    if x_motobug2 <= -150:
        x_motobug2 = random.randint(800,2000)
    if x_monitor <= -150:
        x_monitor = random.randint(1600,4000) 
        tipo = random.randint(0,2)
        if tipo == 0:
            monitor = pygame.image.load("sprites/monitor.webp")
            monitor = pygame.transform.scale(monitor,(100,100))
        else:
            monitor = pygame.image.load("sprites/monitor2.png")
            monitor = pygame.transform.scale(monitor,(100,100))
            tipo = "invencivel"
    pygame.display.flip()
    pontos += 0.01
    velocidade += 0.0001
    if pontos > melhor:
        with open("melhor.json","w") as f:
            f.write(json.dumps(int(pontos),indent=4))
    if y_sonic < 500:
        y_sonic += 0.1
        sonic = sonic_pulando[sprite_pulando]
        sonic = pygame.transform.scale(sonic,(100,100))
    elif sonic_rolando:
        tempo_rolando += 1
        if tempo_rolando >= 100:
            sonic_rolando = False
            tempo_rolando = 0
    else:
        sonic = sonic_correndo[sprite_correndo]
        sonic = pygame.transform.scale(sonic,(100,100))