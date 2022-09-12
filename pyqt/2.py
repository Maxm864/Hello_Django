import pygame
from random import randrange

res = 800
size = 50

x1,y1 = randrange(0,res,size),randrange(0,res,size)
apple = randrange(0,res,size),randrange(0,res,size)
l = 1
snake = [(x1, y1)]
score = 0

pygame.init()


black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

dis = pygame.display.set_mode((res,res))
pygame.display.set_caption("Snake")
font_score = pygame.font.SysFont('Arial',26, bold=True)
img = pygame.image.load('travas.jpg').convert()

game_over = False



x1_change = 0
y1_change = 0

clock =pygame.time.Clock()

while not game_over:
    # dis.blit(img,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -size
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = size
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -size
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = size

    if x1>=800 or x1<0 or y1>=800 or y1<0:
        game_over = True

    x1+=x1_change
    y1+=y1_change
    dis.fill(black)


    [(pygame.draw.rect(dis, blue, (i, j, size-2, size-2))) for i, j in snake]
    # pygame.draw.rect(dis, blue, (x1,y1,size,size)) не понятно если поставить эту строчку вместо той что выше,
    #                                                  то змея не увеличивается
    pygame.draw.rect(dis, red, (*apple, size, size))
    ren_score = font_score.render(f'SCORE: {score}',1,pygame.Color('orange'))
    dis.blit(ren_score,(5,5))
    snake.append((x1,y1))
    snake = snake[-l:]
    pygame.display.update()

    if snake[-1] == apple:
        apple = randrange(0,res,size),randrange(0,res,size)
        l+=1
        score+=1
    pygame.display.flip()



    clock.tick(5)



pygame = quit()
quit()
