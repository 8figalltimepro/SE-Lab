import pygame


class Obstacle:
    def __init__(self, x, ground_y, width=25, height=40):
        self.x = x
        self.prev_x = x
        self.width = width
        self.height = height
        self.y = ground_y - height
        self.scored = False

    def move(self, speed):
        self.prev_x = self.x
        self.x -= speed

    def hits(self, rect):
        swept = self.rect()
        swept.union_ip(pygame.Rect(self.prev_x, self.y, self.width, self.height))
        return swept.colliderect(rect)

    def off_screen(self):
        return self.x + self.width < 0

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
