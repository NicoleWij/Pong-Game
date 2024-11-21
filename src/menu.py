import pygame
import sys
import os
from starfield import update_starfield, draw_starfield
from controls import show_controls

class Menu:
    def __init__(self, screen, width, height, custom_mouse):
        self.screen = screen
        self.width = width
        self.height = height
        self.custom_mouse = custom_mouse

        # Get the absolute path to the font file
        base_dir = os.path.dirname(__file__)
        font_path = os.path.join(base_dir, "../assets/Extrude.ttf")
        click_sound_path = os.path.join(base_dir, "../assets/menu.mp3")

        self.font = pygame.font.Font(font_path, 64)
        self.hover_font = pygame.font.Font(font_path, 48)

        self.options = ["START GAME", "CONTROLS", "QUIT"]
        self.clock = pygame.time.Clock()

        # Load the click sound
        self.click_sound = pygame.mixer.Sound(click_sound_path)
        self.click_sound.set_volume(0.5)  # Set volume for the click sound

    def draw(self, hovered_index=None):
        update_starfield()
        self.screen.fill((0, 0, 0))
        draw_starfield(self.screen)

        for index, option in enumerate(self.options):
            if index == hovered_index:
                text = self.hover_font.render(option, True, (200, 200, 200))
            else:
                text = self.font.render(option, True, (255, 255, 255))

            x = (self.width - text.get_width()) // 2
            y = self.height // 3 + index * 100
            self.screen.blit(text, (x, y))

        self.custom_mouse.draw(self.screen)
        pygame.display.flip()

    def get_choice(self):
        while True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            hovered_index = None

            for index, option in enumerate(self.options):
                text = self.font.render(option, True, (255, 255, 255))
                x = (self.width - text.get_width()) // 2
                y = self.height // 3 + index * 100

                if x <= mouse_x <= x + text.get_width() and y <= mouse_y <= y + text.get_height():
                    hovered_index = index

            self.draw(hovered_index)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if hovered_index is not None:
                        self.click_sound.play()
                        if self.options[hovered_index] == "START GAME":
                            return "START GAME"
                        elif self.options[hovered_index] == "CONTROLS":
                            show_controls(self.screen, self.clock, self.width, self.height, self.custom_mouse)
                        elif self.options[hovered_index] == "QUIT":
                            pygame.quit()
                            sys.exit()

            self.clock.tick(60)
