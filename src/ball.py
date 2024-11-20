import pygame
import os

class Ball:
    def __init__(self, x, y, size, speed_x, speed_y, screen_width, screen_height):
        # Get the absolute path to the star file
        base_dir = os.path.dirname(__file__)  # Directory of the current script
        star_path = os.path.join(base_dir, "../assets/star.png")
        
        self.rect = pygame.Rect(x, y, size, size)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load(star_path)  # Load the star image
        self.image = pygame.transform.scale(self.image, (size * 2.5, size * 2.5))  # Resize to match ball size
        self.angle = 0  # Rotation angle

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y = -self.speed_y

        # Increment angle for rotation
        self.angle += 5  # Adjust rotation speed as needed

    def draw(self, screen):
        # Rotate the image
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, rotated_rect.topleft)