import pygame
import sys

class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("Arial", 64)
        self.options = ["START GAME", "QUIT"]

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black
        for index, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255))
            x = (self.width - text.get_width()) // 2
            y = self.height // 3 + index * 100
            self.screen.blit(text, (x, y))
        pygame.display.flip()

    def get_choice(self):
        while True:
            self.draw()  # Make sure the menu is redrawn continuously
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for index, option in enumerate(self.options):
                        text = self.font.render(option, True, (255, 255, 255))
                        x = (self.width - text.get_width()) // 2
                        y = self.height // 3 + index * 100
                        if x <= mouse_x <= x + text.get_width() and y <= mouse_y <= y + text.get_height():
                            print(f"Clicked on {option}")  # Debug: Show which option was clicked
                            return option
