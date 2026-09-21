import pygame,json,time,random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("sons mine/musica.mp3")
pygame.mixer.music.play(-1)
colocar = pygame.mixer.Sound("sons mine/colocar.mp3")
quebrar = pygame.mixer.Sound("sons mine/quebrar.mp3")
fechar = pygame.mixer.Sound("sons mine/fechar.mp3")
som_secreto = pygame.mixer.Sound("sons mine/som secreto.mp3")
som_secreto_2 = pygame.mixer.Sound("sons mine/som secreto 2.mp3")
botao = pygame.mixer.Sound("sons mine/botao.mp3")
menu = pygame.mixer.Sound("sons mine/menu.mp3")
clock = pygame.time.Clock()
seed1 = [[56, 0, 700, 0, 15, 2018], [56, 100, 700, 0, 16, 2068], [56, 200, 700, 0, 17, 2090], [56, 300, 700, 0, 18, 2116], [56, 400, 700, 0, 19, 2151], [56, 600, 700, 0, 21, 2218], [56, 700, 700, 0, 22, 2257], [56, 800, 700, 0, 23, 2291], [56, 900, 700, 0, 24, 2321], [56, 1000, 700, 0, 25, 2357], [56, 1100, 700, 0, 26, 2388], [56, 1200, 700, 0, 27, 2425], [56, 1300, 700, 0, 28, 2453], [56, 1400, 700, 0, 29, 2533], [56, 1500, 700, 0, 30, 2575], [56, 1600, 700, 0, 31, 2622], [56, 1700, 700, 0, 32, 2661], [56, 1800, 700, 0, 33, 2699], [56, 1900, 700, 0, 34, 2741], [56, 0, 600, 0, 35, 2964], [56, 100, 600, 0, 36, 3046], [56, 200, 600, 0, 37, 3070], [56, 600, 600, 0, 41, 3156], [56, 700, 600, 0, 42, 3188], [56, 800, 600, 0, 43, 3231], [56, 900, 600, 0, 44, 3259], [56, 1000, 600, 0, 45, 3285], [56, 1100, 600, 0, 46, 3309], [56, 1200, 600, 0, 47, 3330], [56, 1300, 600, 0, 48, 3352], [55, 0, 500, 1, 49, 3794], [55, 0, 500, 1, 50, 3799], [55, 100, 500, 1, 51, 3831], [55, 200, 500, 1, 52, 3871], [55, 600, 500, 1, 56, 4034], [55, 700, 500, 1, 57, 4060], [55, 800, 500, 1, 58, 4085], [55, 900, 500, 1, 59, 4110], [55, 1000, 500, 1, 60, 4129], [55, 1100, 500, 1, 61, 4157], [56, 1400, 600, 0, 64, 5291], [56, 1500, 600, 0, 65, 5393], [56, 1600, 600, 0, 66, 5423], [56, 1700, 600, 0, 67, 5480], [56, 1800, 600, 0, 68, 5505], [56, 1900, 600, 0, 69, 5529], [56, 1200, 500, 0, 70, 5710], [56, 1300, 400, 0, 71, 5781], [56, 1400, 400, 0, 73, 5881], [56, 1400, 500, 0, 74, 5913], [56, 1300, 500, 0, 75, 5941], [56, 1500, 500, 0, 76, 5988], [56, 1500, 400, 0, 77, 6011], [56, 1600, 400, 0, 78, 6111], [56, 1700, 300, 0, 80, 6228], [56, 1700, 300, 0, 81, 6232], [56, 1800, 200, 0, 82, 6302], [56, 1800, 300, 0, 83, 6337], [56, 1800, 400, 0, 84, 6364], [56, 1800, 500, 0, 85, 6392], [56, 1700, 400, 0, 86, 6424], [56, 1700, 500, 0, 87, 6442], [56, 1600, 500, 0, 88, 6472], [55, 1900, 500, 1, 89, 6945], [55, 1800, 100, 1, 90, 7014], [55, 1700, 200, 1, 91, 7059], [55, 1600, 300, 1, 92, 7101], [55, 1500, 300, 1, 93, 7133], [55, 1300, 300, 1, 96, 7296], [55, 1200, 400, 1, 97, 7340], [55, 1400, 300, 1, 99, 7856], [55, 300, 600, 1, 100, 8328], [55, 400, 600, 1, 101, 8360], [56, 500, 700, 0, 105, 9062], [55, 500, 600, 1, 106, 9272], [57, 100, 400, 0, 109, 11409], [57, 900, 400, 0, 110, 11557], [57, 800, 400, 0, 111, 11585], [57, 400, 500, 0, 112, 11652]]
seed2 = [[56, 0, 600, 0, 1, 879], [56, 100, 600, 0, 2, 935], [56, 200, 600, 0, 4, 993], [56, 300, 600, 0, 6, 1029], [56, 400, 600, 0, 8, 1067], [56, 500, 600, 0, 12, 1171], [56, 700, 600, 0, 13, 1196], [56, 900, 600, 0, 14, 1226], [56, 1300, 600, 0, 15, 1267], [56, 1200, 600, 0, 16, 1289], [56, 1100, 600, 0, 17, 1312], [56, 1000, 600, 0, 18, 1337], [56, 800, 600, 0, 19, 1366], [56, 700, 600, 0, 20, 1397], [56, 600, 600, 0, 21, 1417], [56, 0, 700, 0, 22, 2119], [56, 100, 700, 0, 23, 2152], [56, 200, 700, 0, 24, 2187], [56, 400, 700, 0, 25, 2213], [56, 300, 700, 0, 26, 2254], [56, 500, 700, 0, 27, 2291], [56, 600, 700, 0, 28, 2326], [56, 700, 700, 0, 29, 2365], [56, 800, 700, 0, 30, 2395], [56, 900, 700, 0, 31, 2430], [56, 1000, 700, 0, 32, 2464], [56, 1100, 700, 0, 33, 2507], [56, 1200, 700, 0, 34, 2550], [56, 1300, 700, 0, 35, 2580], [56, 1400, 700, 0, 36, 2671], [56, 1400, 600, 0, 37, 2704], [56, 1500, 700, 0, 38, 2752], [56, 1500, 600, 0, 39, 2775], [56, 1600, 700, 0, 40, 2817], [56, 1600, 600, 0, 41, 2841], [55, 0, 500, 1, 43, 3843], [55, 100, 500, 1, 44, 3899], [55, 200, 500, 1, 45, 4020], [55, 300, 500, 1, 46, 4059], [55, 400, 500, 1, 47, 4102], [55, 500, 500, 1, 48, 4138], [55, 600, 500, 1, 49, 4177], [55, 700, 500, 1, 50, 4213], [55, 800, 500, 1, 51, 4291], [55, 1000, 500, 1, 52, 4348], [55, 900, 500, 1, 53, 4389], [55, 1100, 500, 1, 54, 4422], [55, 1200, 500, 1, 55, 4448], [55, 1300, 500, 1, 56, 4486], [55, 1400, 500, 1, 57, 4518], [55, 1500, 500, 1, 58, 4549], [55, 1600, 500, 1, 59, 4582]]
seeds = [seed1,seed2]
blocos = seeds[random.randint(0,len(seeds)-1)]
visitados_x = []
for x in range(0,20):
    visitados_x.append(x*100)
bloco = 0
janela = pygame.display.set_mode((0,0))
tamanho_janela = pygame.display.get_window_size()
pygame.display.set_caption("minecraft rafa edition")
fonte = pygame.font.SysFont(None,48)
texto = [fonte.render("1-tronco\n2-tabuas\n3-pedra\n4-folha\n5-tijolo\n6-porta\n7-vidro\n8-terra\n9-flor\ne-trocar inventario",True,(255,0,0)),fonte.render("1-crafting table\n2-fornalha\n3-bau\n4-bau duplo\n5-bedrock\n6-obsidian\n7-terra\n8-pedra\ne-trocar inventario",True,(255,0,0))]
dia = pygame.image.load("blocos/fundo 2.png")
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
hotbar = [{49:tronco,50:tabua,51:pedregulho,52:folha,53:tijolo,54:porta,55:vidro,56:terra,57:flor,48:segredo},{49:crafting_table,50:fornalha,51:bau,52:bau_duplo,53:bedrock,54:obsidian,55:grama,56:pedra,48:mao}]
posiçao = 0
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
        offset_x -= 1900
    if teclas[pygame.K_UP] and frame % 10 == 00:
        offset_y -= 100
    if teclas[pygame.K_DOWN] and frame % 10 == 00:
        offset_y += 100
    janela.fill((0,0,255))
    janela.blit(fundos[fundo],(0,offset_y))
    for bloco in blocos:
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