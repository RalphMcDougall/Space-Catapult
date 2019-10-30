import pygame
import math

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CAPTION = "Space Catapult"
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAY_FONT = None
SCREEN = None

PLANET_RADIUS = 6371000 # distance in metres
ATMOSPHERE_HEIGHT = 1E5 # distance in metres
SCALE = 5E4

LAUNCH_ANGLE = 45 # angle in degrees
LAUNCH_VELOCITY = 1E4 # velocity in m/s

def getDisplayDist(length):
    return int(length / SCALE)

def runSimulation():
    # The main loop of the application
    global SCREEN, DISPLAY_FONT
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    DISPLAY_FONT = pygame.font.Font(pygame.font.get_default_font(), 16)
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()

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

def displayUI():
    # Display the text information over the simulation
    displayText("Planet radius: " + str(PLANET_RADIUS) + "m", 10, 10)
    displayText("Atmosphere thickness: " + str(ATMOSPHERE_HEIGHT) + "m", 10, 30)

def displayText(txt, x, y):
    surface = DISPLAY_FONT.render(txt, True, WHITE, BLACK)
    rect = surface.get_rect()
    rect.topleft = (x, y)
    SCREEN.blit(surface, rect)

def simulateObject():
    position = [0, PLANET_RADIUS]
    velocity = [LAUNCH_VELOCITY * ]

if __name__ == "__main__":
    runSimulation()