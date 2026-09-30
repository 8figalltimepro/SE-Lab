import pygame


class Player:
    def __init__(self, x, ground_y, width=30, height=40):
        self.x = x
        self.ground_y = ground_y
        self.width = width
        self.height = height
        self.gravity = 0.8
        self.jump_strength = -15
        self.reset()

    def reset(self):
        self.y = self.ground_y - self.height
        self.vy = 0
        self.on_ground = True

    def jump(self):
        if not self.on_ground:
            return False
        self.vy = self.jump_strength
        self.on_ground = False
        return True

    def update(self):
        self.vy += self.gravity
        self.y += self.vy

        ground_level = self.ground_y - self.height
        if self.y >= ground_level:
            self.y = ground_level
            self.vy = 0
            self.on_ground = True

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
