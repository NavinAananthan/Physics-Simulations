import pygame
import sys
import pymunk


'''
Function initializations
'''

def create_apple(space):
    body = pymunk.Body(1,100, body_type=pymunk.Body.DYNAMIC) # we specify the parameters for the dynmaic body with mass, inertia and body_type
    body.position = (400,0) # seting the position of the body
    shape = pymunk.Circle(body,80) # Defining the shape of the object by passing the body and the radius
    space.add(body,shape) # adding this to our physics simulation space
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),80)



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
apples.append(create_apple(space))


while True: # game loop
    for event in pygame.event.get(): # checking for user input
        if event.type == pygame.QUIT: # input to close the game
            pygame.quit()
            sys.exit()
    
    screen.fill((217,217,217)) # background color
    draw_apples(apples) # drawing the apples
    space.step(1/50) # to update the simulation parameter is to set how fast we need to update it
    pygame.display.update() # rendering the frame
    clock.tick(120) # limiting the FPS to 120