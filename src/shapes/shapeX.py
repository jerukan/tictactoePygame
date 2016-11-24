import pygame

class ShapeX:

    def draw(self, surface, color, center, width, height):
        pygame.draw.line(surface, color, (center[0] - int(width / 2), center[1] + int(height / 2)), (center[0] + int(width / 2), center[1] - int(height / 2)), 3)
        pygame.draw.line(surface, color, (center[0] + int(width / 2), center[1] + int(height / 2)), (center[0] - int(width / 2), center[1] - int(height / 2)), 3)