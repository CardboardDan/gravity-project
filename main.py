# PyGame template.

# Import standard modules.
import sys

# Import non-standard modules.
import pygame
from pygame.locals import QUIT

width, height = 800, 600
RED = (200, 0, 0)
size = 25
x = 100
y = height-size
vx = 50
vy = -150
bounciness = 0.5
ay = 50
xclear = True
yclear = True

def update(dt):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""
    global x, y, vx, vy, width, height, xclear, yclear
    x += vx*dt/1000
    y += vy*dt/1000
    vy += ay * dt / 1000
    if x < 0 + size:
        x = 0 + size
    if y < 0 + size:
        y = 0 + size
    if x > width - size:
        x = width - size
    if y > height - size:
        y = height - size


    if x>size and x < width -size:
        xclear = True

    if y>size and y < height -size:
        yclear = True


    if xclear and (x + size >= width or x + -size <= 0):
        vx = -vx
        vx = vx * bounciness
        xclear = False
    if yclear and (y + size >= height or y + -size <= 0):
        vy = -vy
        vy = vy * bounciness
        yclear = False
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.
        # Handle other events as you wish.


def draw(screen):
    """
    Draw things to the window. Called once per frame.
    """
    global x
    global y
    global vx
    global vy
    global size
    screen.fill((255, 255, 255))  # Fill the screen with white.

    # Redraw screen here.
    pygame.draw.circle(screen, RED, (x, y), size)

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()


def runPyGame():
    # Initialise PyGame.
    pygame.init()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 60.0
    fpsClock = pygame.time.Clock()
    global width,height
    # Set up the window.

    screen = pygame.display.set_mode((width, height))

    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.

    # Main game loop.
    dt = 1 / fps  # dt is the time since last frame.
    while True:  # Loop forever!
        update(dt)  # You can update/draw here, I've just moved the code for neatness.
        draw(screen)

        dt = fpsClock.tick(fps)


if __name__=='__main__':
    runPyGame()