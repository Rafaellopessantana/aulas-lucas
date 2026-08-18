import pygame

pygame.init()
clock = pygame.time.Clock()
blocos = []
janela = pygame.display.set_mode((0,0))
pygame.display.set_caption("minecraft")
fonte = pygame.font.SysFont(None,48)
texto = [fonte.render("1-tronco\n2-tabuas\n3-pedra\n4-folha\n5-tijolo\n6-porta\n7-vidro\n8-terra\n9-flor\ne-trocar inventario",True,(255,0,0)),fonte.render("1-crafting table\nfornalha\ne-trocar inventario",True,(255,0,0))]
fundo = pygame.image.load("blocos/fundo.jpg")
fundo = pygame.transform.scale(fundo,pygame.display.get_window_size())
tronco = pygame.image.load("blocos/tronco.jpg")
tronco = pygame.transform.scale(tronco,(100,100))
tabua = pygame.image.load("blocos/tabua.webp")
tabua = pygame.transform.scale(tabua,(100,100))
pedra = pygame.image.load("blocos/pedra.jpg")
pedra = pygame.transform.scale(pedra,(100,100))
folha = pygame.image.load("blocos/folha.png")
folha = pygame.transform.scale(folha,(100,100))
tijolo = pygame.image.load("blocos/tijolo.webp")
tijolo = pygame.transform.scale(tijolo,(100,100))
porta = pygame.image.load("blocos/porta.jpg")
porta = pygame.transform.scale(porta,(100,200))
vidro = pygame.image.load("blocos/vidro.webp")
vidro = pygame.transform.scale(vidro,(100,100))
terra = pygame.image.load("blocos/terra.webp")
terra = pygame.transform.scale(terra,(100,100))
flor = pygame.image.load("blocos/flor.png")
flor = pygame.transform.scale(flor,(100,100))
crafting_table = pygame.image.load("blocos/crafting table.jpg")
fornalha = pygame.image.load("blocos/fornalha.webp")
fornalha = pygame.transform.scale(fornalha,(100,100))
crafting_table = pygame.transform.scale(crafting_table,(100,100))
id = tronco
itens = 0
hotbar = [{49:tronco,50:tabua,51:pedra,52:folha,53:tijolo,54:porta,55:vidro,56:terra,57:flor},{49:crafting_table,50:fornalha}]
em_execuçao = True
frame = 0
offset_x = 0
offset_y = 0
while em_execuçao:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            em_execuçao = False
        if event.type == pygame.KEYDOWN:
            try:
                id = hotbar[itens][event.key]
            except:
                pass
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            blocos.append([id,event.pos[0] // 100 * 100 + offset_x,event.pos[1] // 100 * 100 + offset_y])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for bloco in blocos[::-1]:
                if bloco[1] == event.pos[0] // 100 * 100 + offset_x and bloco[2] == event.pos[1] // 100 * 100 + offset_y:
                    blocos.remove(bloco)
                    break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            itens += 1
            if itens >= len(hotbar):
                itens = 0
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and frame % 10 == 00:
        offset_x -= 100
    if teclas[pygame.K_RIGHT] and frame % 10 == 00:
        offset_x += 100
    janela.fill((0,255,0))
    janela.blit(fundo)
    for bloco in blocos:
        janela.blit(bloco[0],(bloco[1] - offset_x,bloco[2] - offset_y))
    janela.blit(texto[itens],(0,0))
    pygame.display.flip()
    clock.tick(60)
    frame += 1
    frame %= 60