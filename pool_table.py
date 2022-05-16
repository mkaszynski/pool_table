import pygame
import time
import random
import math

def add_line(screen, text, x, y, color=(0, 0, 0)):
    # used to print the status of the variables
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)

pygame.init()

font = pygame.font.Font("freesansbold.ttf", 24)

# Set up the drawing window
screen = pygame.display.set_mode([1200, 600])

balls = [[700, 250, 0, 0, (255, 255, 255), None, False]]

for i in range(9):
    for j in range(9):
        if i > j:
            if j % 2 == 0:
                balls.append([j*25 + 100, i*25 + 150 - j*25*0.5, 0, 0, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), i + j - 2, False])
            else:
                balls.append([j*25 + 100, i*25 + 150 - j*25*0.5, 0, 0, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), i + j - 2, True])

angle = 0

points1 = 0
points2 = 0

turn = False


holes = [[0, 250], [570, 0], [1170, 570], [1170, 0], [570, 570], [0, 570], [1170, 250]]

# Run until the user asks to quit
running = True
while running:
    # Fill the background with white
    screen.fill((128, 74, 0))
    pygame.event.poll()
    keys = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()
    mouse_held = pygame.mouse.get_pressed()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if keys[pygame.K_w]:
        angle += 0.03
    if keys[pygame.K_s]:
        angle -= 0.03
    
    for i in balls:
        for j in balls:
            if i == j:
                continue
            if j[0] > i[0] - 20 and j[0] < i[0] + 20:
                if j[1] > i[1] - 20 and j[1] < i[1] + 20:
                    if random.random() > 0.75:
                         n = i[2]
                         m = i[3]
                         a = j[2]
                         b = j[3]
                         i[2] = a + random.random()*i[2] - 0.5*i[2]
                         j[2] = n + random.random()*i[2] - 0.5*i[2]
                         i[3] = b + random.random()*i[2] - 0.5*i[2]
                         j[3] = m + random.random()*i[2] - 0.5*i[2]
    
    if keys[pygame.K_e]:
        for i in balls:
            if i[4] == (255, 255, 255):
                if abs(i[2]) < 0.3 and abs(i[3]) < 0.3:
                    i[2] = math.sin(angle)*25
                    i[3] = math.cos(angle)*25
                    turn = not turn
    
    for i in balls:
        for j in holes:
            if j[0] > i[0] - 30 and j[0] < i[0] + 20:
                if j[1] > i[1] - 30 and j[1] < i[1] + 20:
                    if not i[4] == (255, 255, 255):
                        if i[5] >= 0:
                            if not i[6]:
                                points1 += i[5]
                            else:
                                points2 += i[5]
                        else:
                            points1 += i[5]
                            points2 += i[5]
                        balls.remove(i)
                    else:
                        i[0] = 700
                        i[1] = 250
                        i[2] = 0
                        i[3] = 0
                        if turn:
                            points1 -= 1
                        else:
                            points2 -= 1
    
    for i in balls:
        i[2] *= 0.975
        i[3] *= 0.975
        i[0] += i[2]
        i[1] += i[3]
        if i[0] < 20:
            i[0] = 20
            i[2] *= -1
        if i[1] < 20:
            i[1] = 20
            i[3] *= -1
        if i[0] > 1160:
            i[0] = 1160
            i[2] *= -1
        if i[1] > 560:
            i[1] = 560
            i[3] *= -1
    
    map1 = pygame.Rect(20, 20, 1160, 560)
    pygame.draw.rect(screen, (0, 128, 0), map1)
    
    for i in holes:
        map1 = pygame.Rect(i[0], i[1], 30, 30)
        pygame.draw.rect(screen, (0, 0, 0), map1)
    
    for i in balls:
        if not i[5] == None:
            if i[5] >= 0:
                map1 = pygame.Rect(i[0], i[1], 20, 20)
                pygame.draw.rect(screen, i[4], map1)
            else:
                map1 = pygame.Rect(i[0], i[1], 20, 20)
                pygame.draw.rect(screen, (0, 0, 0), map1)
        else:
            map1 = pygame.Rect(i[0], i[1], 20, 20)
            pygame.draw.rect(screen, i[4], map1)
        if not i[5] == None:
            if i[5] >= 0:
                if not i[6]:
                    add_line(screen, str(i[5]), i[0], i[1], color=(0, 0, 0))
                else:
                    add_line(screen, str(i[5]), i[0], i[1], color=(200, 0, 0))
            else:
                add_line(screen, str(i[5]), i[0], i[1], color=(255, 255, 255))
    
    add_line(screen, f'points for person 1: {points1}', 0, 0)
    add_line(screen, f'points for person 2: {points2}', 0, 45)
    if not turn:
        add_line(screen, 'person 1 turn', 0, 90)
    else:
        add_line(screen, 'person 2 turn', 0, 90)
    
    for i in balls:
        if abs(i[2]) < 0.3 and abs(i[3]) < 0.3:
            if i[4] == (255, 255, 255):
                pygame.draw.line(screen, (128, 74, 0), (i[0], i[1]), (i[0] + math.sin(angle)*-400, i[1] + math.cos(angle)*-400), width=10)
                pygame.draw.line(screen, (0, 74, 128), (i[0], i[1]), (i[0] + math.sin(angle)*400, i[1] + math.cos(angle)*400), width=3)
    
    
    time.sleep(1/60)

    # Flip the display
    pygame.display.flip()

if points1 > points2:
    print('player 1 won')
elif points1 < points2:
    print('player 2 won')
else:
    print('players tied')
    

# Done! Time to quit.
pygame.quit()