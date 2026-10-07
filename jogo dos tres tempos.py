import pygame

pygame.init()

tempos = [[["🏳️",0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,"🏴"]],[["🏳️",0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,"🏴"]],[["🏳️",0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,"🏴"]]]
info = [[1,0,0],[1,3,3]]
turno = 2
janela = pygame.display.set_mode((0,0))
pygame.display.set_caption("nome da janela")
fonte = pygame.font.SysFont(None,48)
texto = fonte.render("g\nr\na\ns\ns\nh\no\np\np\ne\nr",True,(0,0,0))
em_execuçao = True
while em_execuçao:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            em_execuçao = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            try:
                info[turno % 2][2] -= 1
                turno += 1
            except:
                pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            try:
                info[turno % 2][2] += 1
                turno += 1
            except:
                pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            try:
                info[turno % 2][1] += 1
                turno += 1
            except:
                pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            try:
                info[turno % 2][1] -= 1
                turno += 1
            except:
                pass
    tempos = [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
    tempos[info[0][0]][info[0][2]][info[0][1]] = "🏳️"
    tempos[info[1][0]][info[1][2]][info[1][1]] = "🏴"
    janela.fill((0,255,0))
    pygame.display.flip()
print(tempos)
print(info)