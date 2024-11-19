import pygame
import sys
import os
from starfield import update_starfield, draw_starfield

class Menu:
    def __init__(self, screen, width, height, custom_mouse):
        self.screen = screen
        self.width = width
        self.height = height
        self.custom_mouse = custom_mouse  # Add the custom mouse instance

        # Get the absolute path to the font file
        base_dir = os.path.dirname(__file__)
        font_path = os.path.join(base_dir, "../assets/Extrude.ttf")
        
        self.font = pygame.font.Font(font_path, 64)
        self.hover_font = pygame.font.Font(font_path, 48)  # Smaller font for hover effect
        
        self.options = ["START GAME", "QUIT"]
        self.clock = pygame.time.Clock()

    def draw(self, hovered_index=None):
        update_starfield()  # Update star positions
        self.screen.fill((0, 0, 0))  # Clear the screen
        draw_starfield(self.screen)  # Draw the starfield

        # Draw menu options
        for index, option in enumerate(self.options):
            # Use hover font or regular font based on whether it's hovered
            if index == hovered_index:
                text = self.hover_font.render(option, True, (200, 200, 200))  # Gray text when hovered
            else:
                text = self.font.render(option, True, (255, 255, 255))  # White text

            x = (self.width - text.get_width()) // 2
            y = self.height // 3 + index * 100
            self.screen.blit(text, (x, y))

        self.custom_mouse.draw(self.screen)  # Draw the custom mouse cursor
        pygame.display.flip()

    def get_choice(self):
        while True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            hovered_index = None

            # Check if the mouse is hovering over any menu option
            for index, option in enumerate(self.options):
                text = self.font.render(option, True, (255, 255, 255))
                x = (self.width - text.get_width()) // 2
                y = self.height // 3 + index * 100

                if x <= mouse_x <= x + text.get_width() and y <= mouse_y <= y + text.get_height():
                    hovered_index = index

            self.draw(hovered_index)  # Pass the hovered index to the draw method

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if hovered_index is not None:
                        return self.options[hovered_index]  # Return the selected option

            self.clock.tick(60)  # Limit the frame rate
