import pygame,random
pygame.init()

nome_pc = input("qual o nome dele(_/): ")
nome_pc2 = input("e o dele(_/²): ")
janela = pygame.display.set_mode((500,500))
pygame.display.set_caption("movimento ASCII")

pc = "_/"
x_pc = 450
y_pc = 450
r_pc = 255
g_pc = 255
b_pc = 255
pc2 = "²\\_"
x_pc2 = 0
y_pc2 = 0
r_pc2 = 255
g_pc2 = 255
b_pc2 = 255
x_anel = 250
y_anel = 250
fonte = pygame.font.SysFont(None,48)
em_execuçao = True

while em_execuçao:
    t_pc = fonte.render(pc,True,(r_pc,g_pc,b_pc))
    t_pc2 = fonte.render(pc2,True,(r_pc2,g_pc2,b_pc2))
    t_anel = fonte.render("o",True,(255,255,0))
    mov_x_pc = 0
    mov_y_pc = 0
    mov_x_pc2 = 0
    mov_y_pc2 = 0
    for event in pygame.event.get():
        #sistema
        if event.type == pygame.QUIT:
            em_execuçao = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            em_execuçao = False
        #inputs
            #movimento
                #pc1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            mov_y_pc -= 10
            pc = nome_pc + "\n\\/"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            mov_y_pc += 10
            pc = nome_pc + "\n/\\"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            mov_x_pc -= 10
            pc = nome_pc + "\n_/"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            mov_x_pc += 10
            pc = nome_pc + "\n\\_"   
                #pc2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            mov_y_pc2 -= 10
            pc2 = nome_pc2 + "\n²\/"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            mov_y_pc2 += 10
            pc2 = nome_pc2 + "\n/\\²"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            mov_x_pc2 -= 10
            pc2 = nome_pc2 + "\n_/²"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            mov_x_pc2 += 10
            pc2 = nome_pc2 + "\n²\\_"
            #skin
                #pc1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_1:
            r_pc = 255
            g_pc = 0
            b_pc = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP2:
            r_pc = 0
            g_pc = 255
            b_pc = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_3:
            r_pc = 0
            g_pc = 0
            b_pc = 255
        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_5:
            r_pc = 255
            g_pc = 255
            b_pc = 255
                #pc2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            r_pc2 = 255
            g_pc2 = 0
            b_pc2 = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            r_pc2 = 0
            g_pc2 = 255
            b_pc2 = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            r_pc2 = 0
            g_pc2 = 0
            b_pc2 = 255
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            r_pc2 = 255
            g_pc2 = 255
            b_pc2 = 255
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos,event.button)
            em_execuçao = False
    x_pc += mov_x_pc
    y_pc += mov_y_pc
    x_pc2 += mov_x_pc2
    y_pc2 += mov_y_pc2
    hitbox_pc = pygame.Rect(x_pc,y_pc,50,50)
    hitbox_pc2 = pygame.Rect(x_pc2,y_pc2,50,50)
    hitbox_anel = pygame.Rect(x_anel,y_anel,30,30)
    if hitbox_pc.colliderect(hitbox_pc2):
        x_pc -= mov_x_pc
        y_pc -= mov_y_pc
        x_pc2 -= mov_x_pc2
        y_pc2 -= mov_y_pc2
    if hitbox_pc.colliderect(hitbox_anel):
        pc = nome_pc + "\n\\_(^_^)_/"
        x_anel = random.randint(0,500)
        y_anel = random.randint(0,500)
    if hitbox_pc2.colliderect(hitbox_anel):
        pc2 = nome_pc2 + "\n\\_(^_^)_/²"
        x_anel = random.randint(0,500)
        y_anel = random.randint(0,500)
    janela.fill((0,0,0))
    janela.blit(t_pc,(x_pc,y_pc))
    janela.blit(t_pc2,(x_pc2,y_pc2))
    janela.blit(t_anel,(x_anel,y_anel))
    pygame.display.flip()