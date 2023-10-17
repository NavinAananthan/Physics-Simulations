import pygame
import sys
import pymunk


'''
Function initializations
'''

def create_apple(space, pos):
    body = pymunk.Body(1,100, body_type=pymunk.Body.DYNAMIC) # we specify the parameters for the dynmaic body with mass, inertia and body_type
    body.position = pos # seting the position of the body
    shape = pymunk.Circle(body,50) # Defining the shape of the object by passing the body and the radius
    space.add(body,shape) # adding this to our physics simulation space
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x) # getting the position of apple in x
        pos_y = int(apple.body.position.y) # getting the position of apple in y
        pygame.draw.circle(screen,(255,0,0),(pos_x,pos_y),50) # Drawing the apple


def static_ball(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,50)
    space.add(body,shape)
    return shape


def draw_static_balls(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x) 
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),50)


'''
Pygame Initialization
'''
pygame.init() # Initializing the game
screen = pygame.display.set_mode((800,800)) # Creating display surface
clock = pygame.time.Clock() # Creating a game clock

'''
Pymunk Initialization
'''
space = pymunk.Space() # creating the space
space.gravity = (0,500) # creating the gravity for both x-axis and y-axis


apples = []


balls = []
balls.append(static_ball(space,(500,500)))
balls.append(static_ball(space,(270,600)))
balls.append(static_ball(space,(450,700)))


while True: # game loop
    for event in pygame.event.get(): # checking for user input
        if event.type == pygame.QUIT: # input to close the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space,event.pos))

    
    screen.fill((217,217,217)) # background color
    draw_apples(apples) # drawing the apples
    draw_static_balls(balls) # drawing the balls
    space.step(1/50) # to update the simulation parameter is to set how fast we need to update it
    pygame.display.update() # rendering the frame
    clock.tick(120) # limiting the FPS to 120