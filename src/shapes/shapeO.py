import pygame

class ShapeO:

    def draw(self, surface, color, center, width):
        pygame.draw.circle(surface, color, center, int(width / 2), 3)