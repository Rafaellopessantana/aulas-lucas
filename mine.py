import pygame,json,time,random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("sons mine/musica.mp3")
pygame.mixer.music.play(-1)
janela = pygame.display.set_mode((0,0))
tamanho_janela = pygame.display.get_window_size()
pygame.display.set_caption("minecraft rafa edition")
colocar = pygame.mixer.Sound("sons mine/colocar.mp3")
quebrar = pygame.mixer.Sound("sons mine/quebrar.mp3")
fechar = pygame.mixer.Sound("sons mine/fechar.mp3")
som_secreto = pygame.mixer.Sound("sons mine/som secreto.mp3")
som_secreto_2 = pygame.mixer.Sound("sons mine/som secreto 2.mp3")
botao = pygame.mixer.Sound("sons mine/botao.mp3")
menu = pygame.mixer.Sound("sons mine/menu.mp3")
clock = pygame.time.Clock()
visitados_x = []
blocos = []
bloco = 0
fonte = pygame.font.SysFont(None,48)
texto = [fonte.render("1-tronco\n2-tabuas\n3-pedra\n4-folha\n5-tijolo\n6-porta\n7-vidro\n8-terra\n9-flor\ne-trocar inventario",True,(255,0,0)),fonte.render("1-crafting table\n2-fornalha\n3-bau\n4-bau duplo\n5-bedrock\n6-obsidian\n7-terra\n8-pedra\ne-trocar inventario",True,(255,0,0))]
dia = pygame.image.load("blocos/dia.jpg")
dia = pygame.transform.scale(dia,(tamanho_janela[0],tamanho_janela[1] * 5))
noite = pygame.image.load("blocos/noite.png")
noite = pygame.transform.scale(noite,tamanho_janela)
mine = pygame.image.load("blocos/mine.png")
mine = pygame.transform.scale(mine,(tamanho_janela[0],tamanho_janela[1] // 4.7))
fundo_menu_1 = pygame.image.load("blocos/plano de fundo 1.png")
fundo_menu_1 = pygame.transform.scale(fundo_menu_1,(tamanho_janela))
fundo_menu_2 = pygame.image.load("blocos/plano de fundo 2.webp")
fundo_menu_2 = pygame.transform.scale(fundo_menu_2,(tamanho_janela))
fundo_menu_3 = pygame.image.load("blocos/plano de fundo 3.webp")
fundo_menu_3 = pygame.transform.scale(fundo_menu_3,(tamanho_janela))
fundo_menu_4 = pygame.image.load("blocos/plano de fundo 4.png")
fundo_menu_4 = pygame.transform.scale(fundo_menu_4,(tamanho_janela))
chance = random.randint(1,10000)
if chance <= 4000:
    fundo_menu = fundo_menu_1
elif chance <= 8000:
    fundo_menu = fundo_menu_2
elif chance <= 9999:
    fundo_menu = fundo_menu_3
else:
    fundo_menu = fundo_menu_4
fundos = [dia,noite]
fundo = 0
começar = False
criar = pygame.image.load("blocos/criar.png")
criar = pygame.transform.scale(criar,(tamanho_janela[0],tamanho_janela[1] // 2))
abrir = pygame.image.load("blocos/abrir.png")
abrir = pygame.transform.scale(abrir,(tamanho_janela[0],tamanho_janela[1] // 2))
salvar = pygame.image.load("blocos/salvar.png")
salvar = pygame.transform.scale(salvar,(tamanho_janela[0],tamanho_janela[1] // 2))
tronco = pygame.image.load("blocos/tronco.jpg")
tronco = pygame.transform.scale(tronco,(100,100))
tabua = pygame.image.load("blocos/tabua.webp")
tabua = pygame.transform.scale(tabua,(100,100))
pedregulho = pygame.image.load("blocos/pedregulho.jpg")
pedregulho = pygame.transform.scale(pedregulho,(100,100))
folha = pygame.image.load("blocos/folha.png")
folha = pygame.transform.scale(folha,(100,100))
tijolo = pygame.image.load("blocos/tijolo.webp")
tijolo = pygame.transform.scale(tijolo,(100,100))
porta = pygame.image.load("blocos/porta.png")
porta = pygame.transform.scale(porta,(100,200))
vidro = pygame.image.load("blocos/vidro.webp")
vidro = pygame.transform.scale(vidro,(100,100))
terra = pygame.image.load("blocos/terra.webp")
terra = pygame.transform.scale(terra,(100,100))
flor = pygame.image.load("blocos/flor.png")
flor = pygame.transform.scale(flor,(100,100))
crafting_table = pygame.image.load("blocos/crafting table.jpg")
crafting_table = pygame.transform.scale(crafting_table,(100,100))
fornalha = pygame.image.load("blocos/fornalha.webp")
fornalha = pygame.transform.scale(fornalha,(100,100))
bau = pygame.image.load("blocos/bau.jpg")
bau = pygame.transform.scale(bau,(100,100))
bau_duplo = pygame.transform.scale(bau,(200,100))
bedrock = pygame.image.load("blocos/bedrock.jfif")
bedrock = pygame.transform.scale(bedrock,(100,100))
obsidian = pygame.image.load("blocos/obsidian.jpg")
obsidian = pygame.transform.scale(obsidian,(100,100))
grama = pygame.image.load("blocos/grama.jfif")
grama = pygame.transform.scale(grama,(100,100))
pedra = pygame.image.load("blocos/pedra.jpg")
pedra = pygame.transform.scale(pedra,(100,100))
diorito = pygame.image.load("blocos/diorito.webp")
diorito = pygame.transform.scale(diorito,(100,100))
andesito = pygame.image.load("blocos/andesito.webp")
andesito = pygame.transform.scale(andesito,(100,100))
granito = pygame.image.load("blocos/granito.webp")
granito = pygame.transform.scale(granito,(100,100))
ardosia = pygame.image.load("blocos/ardosia.jpg")
ardosia = pygame.transform.scale(ardosia,(100,100))
segredo = pygame.image.load("blocos/segredo.png")
segredo = pygame.transform.scale(segredo,(100,100))
mao = pygame.image.load("blocos/mao.webp")
mao = pygame.transform.scale(mao,(200,200))
mostrar = True
id = 49
itens = 0
em_execuçao = True
frame = 1
offset_x = 0
offset_y = 0
hotbar = [{49:tronco,50:tabua,51:pedregulho,52:folha,53:tijolo,54:porta,55:vidro,56:terra,57:flor,48:segredo},{49:crafting_table,50:fornalha,51:bau,52:bau_duplo,53:bedrock,54:obsidian,55:grama,56:pedra,48:mao},{49:andesito,50:diorito,51:granito,52:pedra,53:ardosia,54:bedrock}]
posiçao = 0
for x in range(0,tamanho_janela[0]):
    offset_x -= 100
    if offset_x not in visitados_x:
        visitados_x.append(offset_x)
        tamanho = random.randint(2,5)
        for y in range(tamanho+1):
            if y < tamanho:
                blocos.append([56,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 800) // 100 * 100,0,posiçao,frame])  
            else:
                blocos.append([55,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 800) // 100 * 100,1,posiçao,frame])
            if random.randint(1,3) == 3:
                blocos.append([57,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 900) // 100 * 100,0,posiçao,frame])  
        for y in range(tamanho_janela[1] // 100,tamanho_janela[1] // 100 * 2):
            tipo = random.randint(49,52)
            blocos.append([tipo,offset_x,y * 100 + 100,2,posiçao,frame])
        for y in range(tamanho_janela[1] // 100 * 2,tamanho_janela[1] // 100 * 3):
            blocos.append([53,offset_x,y * 100 + 100,2,posiçao,frame])   
        blocos.append([54,offset_x,y * 100 + 200,2,posiçao,frame])
menu.play()
while em_execuçao:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar.play()
            time.sleep(3)
            em_execuçao = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] <= tamanho_janela[1] // 2:
            botao.play()
            começar = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] >= tamanho_janela[1] // 2:
            with open("mundo.json","r") as f:
                botao.play()
                blocos = json.loads(f.read())
                começar = True
    janela.fill((0,0,0))
    janela.blit(fundo_menu,(0,0))
    janela.blit(criar,(0,0))
    janela.blit(mine,(0,0))
    janela.blit(abrir,(0,tamanho_janela[1] // 2))
    pygame.display.flip()
    if começar:
        break
while em_execuçao:
    começar = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar.play()
            time.sleep(3)
            em_execuçao = False
        if event.type == pygame.KEYDOWN:
            try:
                id = hotbar[itens][event.key]
                id = event.key
            except:
                pass
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if id == 48 and itens == 0:
                som_secreto.play()
            else:
                colocar.play()
            blocos.append([id,event.pos[0] // 100 * 100 + offset_x,event.pos[1] // 100 * 100 + offset_y,itens,posiçao,frame])
            posiçao += 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for bloco in blocos[::-1]:
                if bloco[1] == event.pos[0] // 100 * 100 + offset_x and bloco[2] == event.pos[1] // 100 * 100 + offset_y:
                    if bloco[0] == 48:
                        som_secreto_2.play()
                    else:
                        quebrar.play()
                    blocos.remove(bloco)
                    break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if mostrar:
                mostrar = False
            else:
                mostrar = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            itens += 1
            if itens >= len(hotbar):
                itens = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F4:  
            menu.play()
            while em_execuçao:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        fechar.play()
                        time.sleep(3)
                        em_execuçao = False
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] <= tamanho_janela[1] // 2:
                        blocos = []
                        botao.play()
                        começar = True
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] >= tamanho_janela[1] // 2:
                            with open("mundo.json","w") as f:
                                f.write(json.dumps(blocos))
                            botao.play()
                            começar = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_F4:
                        começar = True
                janela.blit(criar,(0,0))
                janela.blit(mine,(0,0))
                janela.blit(salvar,(0,tamanho_janela[1] // 2))
                pygame.display.flip()
                if começar:
                    break
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and frame % 10 == 00:
        offset_x -= 100
        if offset_x not in visitados_x:
            visitados_x.append(offset_x)
            tamanho = random.randint(2,5)
            for y in range(tamanho+1):
                if y < tamanho:
                  blocos.append([56,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 800) // 100 * 100,0,posiçao,frame])  
                else:
                    blocos.append([55,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 800) // 100 * 100,1,posiçao,frame])
            if random.randint(1,3) == 3:
                blocos.append([57,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 900) // 100 * 100,0,posiçao,frame])  
            for y in range(tamanho_janela[1] // 100,tamanho_janela[1] // 100 * 2):
                tipo = random.randint(49,52)
                blocos.append([tipo,offset_x,y * 100 + 100,2,posiçao,frame])
    if teclas[pygame.K_RIGHT] and frame % 10 == 00:
        for x in range(0,20):
            offset_x += 100
            if offset_x not in visitados_x:
                visitados_x.append(offset_x)
                tamanho = random.randint(2,5)
                for y in range(tamanho+1):
                    if y < tamanho:
                        blocos.append([56,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 800) // 100 * 100,0,posiçao,frame])  
                    else:
                        blocos.append([55,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 800) // 100 * 100,1,posiçao,frame])
                if random.randint(1,3) == 3:
                    blocos.append([57,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 900) // 100 * 100,0,posiçao,frame])  
                for y in range(tamanho_janela[1] // 100,tamanho_janela[1] // 100 * 2):
                    tipo = random.randint(49,52)
                    blocos.append([tipo,offset_x,y * 100 + 100,2,posiçao,frame])
            if y < tamanho:
                blocos.append([56,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 800) // 100 * 100,0,posiçao,frame])  
            else:
                blocos.append([55,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 800) // 100 * 100,1,posiçao,frame])
            if random.randint(1,3) == 3:
                blocos.append([57,offset_x // 100 * 100,(tamanho_janela[1] + (tamanho_janela[1] - (100 * y)) - 900) // 100 * 100,0,posiçao,frame])  
            for y in range(tamanho_janela[1] // 100,tamanho_janela[1] // 100 * 2):
                tipo = random.randint(49,52)
                blocos.append([tipo,offset_x,y * 100 + 100,2,posiçao,frame])
            for y in range(tamanho_janela[1] // 100 * 2,tamanho_janela[1] // 100 * 3):
                blocos.append([53,offset_x,y * 100 + 100,2,posiçao,frame])   
        blocos.append([54,offset_x,y * 100 + 200,2,posiçao,frame])
        offset_x -= 1900
    if teclas[pygame.K_UP] and frame % 10 == 00:
        offset_y -= 100
    if teclas[pygame.K_DOWN] and frame % 10 == 00:
        if offset_y < tamanho_janela[1] * 300 // 100:
            offset_y += 100
    janela.fill((0,0,255))
    janela.blit(fundos[fundo],(0,offset_y))
    for bloco in blocos:
        if bloco[1] >= offset_x and bloco[1] <= offset_x + tamanho_janela[0] and bloco[2] >= offset_y and bloco[2] <= offset_y + tamanho_janela[1]:
            janela.blit(hotbar[bloco[3]][bloco[0]],(bloco[1] - offset_x,bloco[2] - offset_y))
    if mostrar:
        janela.blit(texto[itens],(0,0))
        janela.blit(mao,(tamanho_janela[0]-200,tamanho_janela[1]-200))
    if frame % 7200 == 0:
        fundo += 1
        if fundo >= len(fundos):
            fundo = 0
    pygame.display.flip()
    clock.tick(60)
    frame += 1