import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CAPTION = "Space Catapult"
FPS = 30

def runSimulation():
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()

    running = True
    while running:
        drawScene()
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
    # Do all of the drawing required for the 
    pass


if __name__ == "__main__":
    runSimulation()