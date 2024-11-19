import pygame
import os

class Mouse:
    def __init__(self, base_dir, cursor_image_name):
        """Initialize the custom mouse cursor."""
        cursor_path = os.path.join(base_dir, cursor_image_name)  # Combine base directory and image name
        try:
            self.cursor_image = pygame.image.load(cursor_path)  # Load the cursor image
            self.cursor_image = pygame.transform.scale(self.cursor_image, (30, 30))  # Resize if needed
            pygame.mouse.set_visible(False)  # Hide the default system cursor
        except pygame.error as e:
            print(f"Error loading cursor image: {e}")
            self.cursor_image = None  # Fallback to no custom cursor

    def draw(self, screen):
        """Draw the custom cursor at the current mouse position."""
        if self.cursor_image:  # Only draw if the image was loaded successfully
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cursor_rect = self.cursor_image.get_rect(center=(mouse_x, mouse_y))
            screen.blit(self.cursor_image, cursor_rect)
