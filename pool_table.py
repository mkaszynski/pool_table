import pygame
import pygame.locals as pg_locals
import random
import time as t

WELCOME_TXT = 'Hello! Welcome to pool table game! Press enter to start.'

def wrap_text(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x
        ty = y + y_offset
        y_offset += fh

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))


def rand_color():
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))

def add_line(screen, text, x, y):
    # used to print the status of the variables
    text = font.render(text, True, white) 
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)


black = (0, 0, 0)
white = (255, 255, 255)

TICKS = 60
vel_y = 0

GRAVITY = -3
ANTIGRAVITY = 3
red = 75
green = 25
blue = 0

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)


# set the screen size
full_screen = True
if full_screen:
    info = pygame.display.Info()
    SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h - 105
else:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600

screen = pygame.display.set_mode((0, 0))


HEIGHT = 40
GROUND_Y = SCREEN_HEIGHT + HEIGHT + 60

pos_x = 0.5 * SCREEN_WIDTH
pos_y = GROUND_Y

my_color = (160, 0, 0)
my_color2 = (0, 0, 200)
bounce = 0
gravity = 1
friction = 0.1
pos_x2 = 0.4 * SCREEN_WIDTH
pos_y2 = GROUND_Y
jump = 20
vel_y2 = 0
vel_x2 = 0
health = 100
health2 = 100
second_time = False
second_time2 = False
healing = 0.005
healing2 = 0.005
heling = False
heling2 = False
strength = False
strength2 = False
poison = False
poison2 = False
time = 0
ground_c = 125
sun_moon = 255
sun_moon2 = 0
points = 0
points2 = 0

def star(posx, posy):
    he = pygame.Rect(posx, posy, 5, 5)
    pygame.draw.rect(screen, (255, 255, 255), he)
        

# use this clock to limit the update of the game
clock = pygame.time.Clock()

unn = True
while unn:
    screen.fill((120, 0, 170))# make entire screen black
    add_line(screen, 'Kaszynski studios',
                     550, 250)
    pygame.event.poll()
    pygame.display.update()
    t.sleep(2)
    clock.tick(TICKS)
    unn = False

vel_x = 0
vel_y = 0
h = random.randint(0, 1000)
n = random.randint(0, 1000)


first_time = True
running = True
while running:
    screen.fill((red, green, blue))# make entire screen black
    
    
    
    # display welcome text
    if first_time:
        
        wrap_text(WELCOME_TXT, font, 'white', 400, 200, screen,
                  SCREEN_WIDTH // 2)

        pygame.event.poll()
        keys = pygame.key.get_pressed()
        pygame.display.update()

        if keys[pg_locals.K_RETURN]:
            first_time = False
        
        continue        

    pygame.display.set_caption('fight game')

    GROUND_Y = SCREEN_HEIGHT - HEIGHT
    on_ground = pos_y == GROUND_Y

    # update events
    pygame.event.poll()

    keys = pygame.key.get_pressed()
    
    if True:
        if keys[pg_locals.K_d]:
            vel_x = 10
        if keys[pg_locals.K_a]:
            vel_x = -10
            
                        
        if health > 100:
            health = 100
        if health > 0:
            health = health + healing
        
                
        if health2 > 100:
            health2 = 100
        if health2 > 0:
            health2 = health2 + healing2
            
        if heling == True:
            healing = 0.01
        if heling2 == True:
            healing2 = 0.01
            
        if poison == True:
            health = health - 0.03
        if poison2 == True:
            health2 = health - 0.03
        
        if keys[pg_locals.K_k]:
            vel_x2 = 10
        if keys[pg_locals.K_h]:
            vel_x2 = -10
    
        # simulate drag
        vel_x -= friction *vel_x
        if abs(vel_x) < 0.5:
            vel_x = 0
        vel_x2 -= friction *vel_x2
        if abs(vel_x2) < 0.5:
            vel_x2 = 0
            
        # if pos_x > pos_x2 - 40:
        #     vel_x2 = vel_x
        #     vel_x = 0
        # if pos_x < pos_x2 + 40:
        #     vel_x2 = vel_x
        #     vel_x = 0
        # if pos_x2 > pos_x - 40:
        #     vel_x = vel_x2
        #     vel_x2 = 0
        # if pos_x2 < pos_x + 40:
        #     vel_x2 = vel_x
        #     vel_x2 = 0
            
        
        # if pos_y > pos_y2 - 40:
        #     vel_y2 = vel_y
        #     vel_y = 0
        # if pos_y < pos_y2 + 40:
        #     vel_y2 = vel_y
        #     vel_y = 0
        # if pos_y2 > pos_y - 40:
        #     vel_y = vel_y2
        #     vel_y2 = 0
        # if pos_y2 < pos_y + 40:
        #     vel_y2 = vel_y
        #     vel_y2 = 0
        
    if pos_y < 40 and pos_x == 40:
        points = points + 1
        pos_y = 0.5 * SCREEN_HEIGHT
        pos_x = 0.5 * SCREEN_WIDTH
    if pos_y2 < 40 and pos_x2 == 40:
        points2 = points2 + 1
        pos_y2 = 0.5 * SCREEN_HEIGHT
        pos_x2 = 0.4 * SCREEN_WIDTH
        
    pos_x += vel_x
    
    pos_x2 += vel_x2

    # bounds checking
    if pos_x < 40:
        pos_x = 40
        vel_x = vel_x * -1
    if pos_x > SCREEN_WIDTH - HEIGHT * 2:
        pos_x = SCREEN_WIDTH - HEIGHT * 2
        vel_x = vel_x * -1
        
    if pos_x2 < 40:
        pos_x2 = 40
        vel_x = vel_x * -1
    if pos_x2 > SCREEN_WIDTH - HEIGHT * 2:
        pos_x2 = SCREEN_WIDTH - HEIGHT * 2
    
    
    if keys[pg_locals.K_q]:
        running = False
    if keys[pg_locals.K_w]:
        vel_y -= 5
            
    if keys[pg_locals.K_u]:
        vel_y2 -= 5
            
    if health2 < 0:
        second_time2 = True
    if health < 0:
        second_time = True
    
    # falls to the roof
    if keys[pg_locals.K_s]:
        vel_y = 10
    if keys[pg_locals.K_j]:
        vel_y2 = 10
        
    if vel_y > 0:
        vel_y = vel_y - friction * vel_y
    if vel_y < 0:
        vel_y = vel_y - friction * vel_y
    if vel_y2 > 0:
        vel_y2 = vel_y2 - friction * vel_y2
    if vel_y2 < 0:
        vel_y2 = vel_y2 - friction * vel_y2
    
    # update position using velocity
    pos_y += vel_y
    
    pos_y2 += vel_y2
    
    
    if pos_y < 40 and pos_x != 0:
        pos_y = 40
        vel_y *= -1  # make bounce
    if pos_y > GROUND_Y:
        pos_y = GROUND_Y
        # must reset velocity as well
        vel_y *= -1  # make bounce
        
    if pos_y2 < 40:
        pos_y2 = 40
        vel_y2 *= -1  # make bounce
    if pos_y2 > GROUND_Y:
        pos_y2 = GROUND_Y
        # must reset velocity as well
        vel_y2 *= -1  # make bounce
    
    # simulate drag
    # if abs(vel_y) < 3.0:
    #     vel_y = 3.0
    
    # if abs(vel_y2) < 3.0:
    #     vel_y2 = 3.0
    
    ju = time * 0.5
    
        
    # print out the current variables
    # add_line(screen, f'vel 1: {vel_y :.0f}',
    #           0, 0)
    # add_line(screen, f'vel 2: {vel_y2 :.0f}',
    #           0, 45)
    # add_line(screen, f'time: {time :.0f}',
    #             0, 90)
        
    # if second_time == True:
    #     if second_time2 == False:
    #         add_line(screen, 'player 2 won! press enter to end the game or press p to play again',
    #                  200, 250)
    #         if keys[pg_locals.K_RETURN]:
    #             running = False
    #         if keys[pg_locals.K_p]:
    #             health = 100
    #             health2 = 100
    #             pos_x = 0.5 * SCREEN_WIDTH
    #             pos_x2 = 0.4 * SCREEN_WIDTH
    #             second_time = False
    
    # if second_time2 == True:
    #     if second_time == False:
    #         add_line(screen, 'player 1 won! press enter to end the game or press p to play again',
    #                  200, 250)
    #         if keys[pg_locals.K_RETURN]:
    #             running = False
    #         if keys[pg_locals.K_p]:
    #             health = 100
    #             health2 = 100
    #             pos_x = 0.5 * SCREEN_WIDTH
    #             pos_x2 = 0.4 * SCREEN_WIDTH
    #             second_time2 = False
                

    ground = pygame.Rect(40, 40, SCREEN_WIDTH - 80, SCREEN_HEIGHT - 40)
    pygame.draw.rect(screen, (0, ground_c, 0 ), ground)
        
    
    if health >= 0:
        rect = pygame.Rect(pos_x, pos_y, HEIGHT, HEIGHT)
        pygame.draw.rect(screen, my_color, rect)
    
    if health2 >= 0:
        rect2 = pygame.Rect(pos_x2, pos_y2, HEIGHT, HEIGHT)
        pygame.draw.rect(screen, my_color2, rect2)
    
    hole1 = pygame.Rect(40, 0, HEIGHT, HEIGHT)
    pygame.draw.rect(screen, (0, 0, 0), hole1)
    
    pygame.display.update()

    # wait until next tick
    clock.tick(TICKS)

pygame.quit()
