import pygame
import random
import math

pygame.init()

# ✅ Fixed spelling mistake: HEIGHT instead of HIEGHT
WIDTH, HEIGHT = 600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

BLACK = (0, 0, 0)

class practical:
    def __init__(self, x, y, colour, vel_x, vel_y, lifetime):
        self.x = x
        self.y = y
        self.colour = colour
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.lifetime = lifetime
        self.age = 0

    def update(self):
        """Move particle and increase its age."""
        self.x += self.vel_x
        self.y += self.vel_y
        self.age += 1

        # Add some gradual slowing (like friction)
        self.vel_x *= 0.98
        self.vel_y *= 0.98

    def draw(self, surface):
        """Draw particle on screen."""
        if self.age < self.lifetime:
            pygame.draw.circle(surface, self.colour, (int(self.x), int(self.y)), 3)

# Main loop setup
particles = []
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ✅ Create random new particles each frame (from near top)
    for _ in range(5):
        x = WIDTH / 2
        y = HEIGHT / 8  # now this works correctly!
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        vel_x = random.uniform(-4, 4)
        vel_y = random.uniform(-4, 4)
        lifetime = random.randint(40, 100)
        particles.append(practical(x, y, colour, vel_x, vel_y, lifetime))

    # Update and draw all particles
    for p in particles[:]:
        p.update()
        p.draw(screen)
        if p.age > p.lifetime:
            particles.remove(p)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
