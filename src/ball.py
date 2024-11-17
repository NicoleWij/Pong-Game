import pygame

class Ball:
    def __init__(self, x, y, size, speed_x, speed_y, screen_width, screen_height):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y = -self.speed_y

    def check_collision(self, paddle1, paddle2):
        # Bounce off paddles
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.speed_x = -self.speed_x

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)
