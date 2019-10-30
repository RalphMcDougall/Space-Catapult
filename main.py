import pygame
import math

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CAPTION = "Space Catapult"
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

DISPLAY_FONT = None
SCREEN = None

PLANET_RADIUS = 6371000 # distance in metres
ATMOSPHERE_HEIGHT = 1E5 # distance in metres
PLANET_MASS = 6E24 # mass in kilograms
OBJECT_MASS = 1E3 # mass in kilograms

G = 6.67408 * 1E-11 # Universal Gravitation constant in m^3.kg^-1.s^-2

SCALE = 1E5

LAUNCH_ANGLE = 1 # angle in degrees
LAUNCH_VELOCITY = 1E4 # velocity in m/s
OBJECT_PATH = []

MAX_ITER = 2E4
DT = 1 # number of seconds to jump between each simulation
DOT_RADIUS = 1
MAX_H = 0


def runSimulation():
    # The main loop of the application
    global SCREEN, DISPLAY_FONT, OBJECT_PATH
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    DISPLAY_FONT = pygame.font.Font(pygame.font.get_default_font(), 16)
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()

    OBJECT_PATH = simulateObject()

    running = True
    while running:
        SCREEN.fill(BLACK)
        drawScene()
        displayUI()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        clock.tick(FPS)
        pygame.display.update() 
    
    pygame.quit()


def drawScene():
    # Do all of the drawing required for the simulation
    
    # Draw the atmosphere
    pygame.draw.circle( SCREEN, BLUE, (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)), getDisplayDist(PLANET_RADIUS + ATMOSPHERE_HEIGHT) )

    # Draw the planet overlayed on the atmosphere
    pygame.draw.circle( SCREEN, GREEN, (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)), getDisplayDist(PLANET_RADIUS) )

    for i in OBJECT_PATH:
        pygame.draw.circle(SCREEN, YELLOW, i, DOT_RADIUS)

def displayUI():
    # Display the text information over the simulation
    displayText("Planet radius: " + str(PLANET_RADIUS) + "m", 10, 10)
    displayText("Atmosphere thickness: " + str(ATMOSPHERE_HEIGHT) + "m", 10, 30)
    displayText("Launch angle: " + str(LAUNCH_ANGLE) + "deg", 10, 50)
    displayText("Launch velocity: " + str(LAUNCH_VELOCITY) + "m/s", 10, 70)
    displayText("Max height: " + str(MAX_H) + "m", 10, 90)

def displayText(txt, x, y):
    surface = DISPLAY_FONT.render(txt, True, WHITE, BLACK)
    rect = surface.get_rect()
    rect.topleft = (x, y)
    SCREEN.blit(surface, rect)

def getDisplayDist(length):
    return int(length / SCALE)

def simulateObject():
    global MAX_H
    print("Running simulation")
    position = [0, PLANET_RADIUS]
    velocity = [LAUNCH_VELOCITY * math.cos(LAUNCH_ANGLE * (math.pi / 180)), LAUNCH_VELOCITY * math.sin(LAUNCH_ANGLE * (math.pi / 180)) ]
    
    t = 0

    path = []
    MAX_H = 0

    while True:
        print("t = " + str(t) + ", position = (" + str(position[0]) + ", " + str(position[1]) + ")")
        if t > MAX_ITER:
            break
        h = getDistToOrigin(position[0], position[1])

        MAX_H = max(MAX_H, h)

        if h < PLANET_RADIUS:
            break
        
        acceleration = getUnitVectorToOrigin(position[0], position[1])

        accMag = G * PLANET_MASS / ( ( getDistToOrigin(position[0], position[1]) ) ** 2 ) # Newton's Law of Gravitation

        acceleration[0] *= accMag
        acceleration[1] *= accMag

        velocity[0] += acceleration[0] * DT
        velocity[1] += acceleration[1] * DT
        position[0] += velocity[0] * DT
        position[1] += velocity[1] * DT

        screenPos = ( int(getDisplayDist(position[0]) + SCREEN_WIDTH / 2), int(-1 * getDisplayDist(position[1]) + SCREEN_HEIGHT / 2) )
        path.append(screenPos)

        t += 1
    
    return path

def getDistToOrigin(x, y):
    return (x * x + y * y) ** 0.5

def getUnitVectorToOrigin(x, y):
    return [-1 * x / getDistToOrigin(x, y), -1 * y / getDistToOrigin(x, y)]

if __name__ == "__main__":
    runSimulation()