import pygame

class Paddle:
    def __init__(self, x, y, width, height, screen_height):
        self.rect = pygame.Rect(x, y, width, height)
        self.screen_height = screen_height

    def move(self, up_key, down_key, speed):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= speed
        if keys[down_key] and self.rect.bottom < self.screen_height:
            self.rect.y += speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
