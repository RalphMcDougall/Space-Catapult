import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CAPTION = "Space Catapult"
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN = None

PLANET_RADIUS = 6371000 # distance in metres
ATMOSPHERE_HEIGHT = 1E5 # distance in metres
SCALE = 5E4

def getDisplayDist(length):
    return int(length / SCALE)

def runSimulation():
    # The main loop of the application
    global SCREEN
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
    pass

if __name__ == "__main__":
    runSimulation()