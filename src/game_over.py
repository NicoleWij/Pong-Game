import pygame
import sys
import os
from starfield import update_starfield, draw_starfield

class GameOver:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        # Get the absolute path to the font file
        base_dir = os.path.dirname(__file__)  # Directory of the current script
        font_path = os.path.join(base_dir, "../assets/Extrude.ttf")

        self.font = pygame.font.Font(font_path, 64)
        self.options_font = pygame.font.Font(font_path, 34)
        self.hover_font = pygame.font.Font(font_path, 48)
        
        self.options = ["RESTART GAME", "QUIT"]
        self.clock = pygame.time.Clock()

    def draw(self, winner, winner_hits, hovered_index=None):
        update_starfield()  # Update star positions
        self.screen.fill((0, 0, 0))  # Clear the screen
        draw_starfield(self.screen)  # Draw the starfield

        # Game Over text
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))  # Red text
        x = (self.width - game_over_text.get_width()) // 2
        y = self.height // 6
        self.screen.blit(game_over_text, (x, y))

        # Winner text
        winner_text = self.options_font.render(f"The winner is {winner}!", True, (255, 255, 0))  # Yellow text
        x = (self.width - winner_text.get_width()) // 2
        y += 100  # Add spacing below "GAME OVER"
        self.screen.blit(winner_text, (x, y))

        # Winner hits text
        hits_text = self.options_font.render(f"You hit the ball a total of {winner_hits} times!", True, (255, 255, 0))
        x = (self.width - hits_text.get_width()) // 2
        y += 80  # Add spacing below "The winner is"
        self.screen.blit(hits_text, (x, y))

        # Draw options with hover effect
        for index, option in enumerate(self.options):
            if index == hovered_index:
                text = self.hover_font.render(option, True, (200, 200, 200))  # Gray text when hovered
            else:
                text = self.font.render(option, True, (255, 255, 255))  # White text

            x = (self.width - text.get_width()) // 2
            y += 100  # Add spacing for menu options
            self.screen.blit(text, (x, y))

        pygame.display.flip()

    def get_choice(self, winner, winner_hits):
        while True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            hovered_index = None

            # Check if the mouse is hovering over any menu option
            base_y = self.height // 6 + 100 + 80 + 100  # Starting y-position for menu options
            for index, option in enumerate(self.options):
                text = self.font.render(option, True, (255, 255, 255))
                x = (self.width - text.get_width()) // 2
                y = base_y + index * 100

                if x <= mouse_x <= x + text.get_width() and y <= mouse_y <= y + text.get_height():
                    hovered_index = index

            self.draw(winner, winner_hits, hovered_index)  # Pass hovered_index to the draw method

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if hovered_index is not None:
                        return self.options[hovered_index]  # Return the selected option

            # Control frame rate
            self.clock.tick(60)