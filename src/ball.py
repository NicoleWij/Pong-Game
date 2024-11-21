import pygame
import os
import random

class Ball:
    def __init__(self, x, y, size, speed_x, speed_y, screen_width, screen_height):
        base_dir = os.path.dirname(__file__)
        star_path = os.path.join(base_dir, "../assets/star.png")
        
        self.rect = pygame.Rect(x, y, size, size)
        
        # Randomize direction for both x and y speeds
        self.speed_x = speed_x if random.choice([True, False]) else -speed_x
        self.speed_y = speed_y if random.choice([True, False]) else -speed_y
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load(star_path)  # Load the star image
        self.image = pygame.transform.scale(self.image, (size * 2.5, size * 2.5))  # Resize to match ball size
        self.angle = 0  # Rotation angle

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom walls
        if self.rect.top <= 0:
            self.rect.top = 0  # Prevent overlapping the top boundary
            self.speed_y = -self.speed_y
        elif self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height  # Prevent overlapping the bottom boundary
            self.speed_y = -self.speed_y
    
        self.angle += 5 

    def draw(self, screen):
        # Rotate the image
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, rotated_rect.topleft)
