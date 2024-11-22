import pygame
import os
import sys
from menu import Menu
from game_over import GameOver
from game import PongGame
from mouse import Mouse

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 36

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", FONT_SIZE)
pygame.mixer.init()

# Initialize custom mouse cursor & audio
base_dir = os.path.dirname(__file__)
cursor_path = os.path.join(base_dir, "../assets/star_cursor.xpm")
music_path = os.path.join(base_dir, "../assets/background.mp3")
ball_sound_path = os.path.join(base_dir, "../assets/ball.mp3")
game_over_path = os.path.join(base_dir, "../assets/game_over.mp3")

custom_mouse = Mouse(base_dir, "../assets/star_cursor.xpm")

# Load and set up background music
pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(0.5)

# Load and set up the ball hit sound effect
ball_sound = pygame.mixer.Sound(ball_sound_path)
ball_sound.set_volume(0.3)

# Load and set up the game over sound effect
game_over_sound = pygame.mixer.Sound(game_over_path)
game_over_sound.set_volume(1)

# Initialize Menu and GameOver with the custom mouse
menu = Menu(screen, WIDTH, HEIGHT, custom_mouse)
game_over_screen = GameOver(screen, WIDTH, HEIGHT, custom_mouse)

# Initialize the PongGame
pong_game = PongGame(screen, clock, custom_mouse, ball_sound, game_over_sound)

def main():
    """Main entry point for the PONG game."""
    # Play background music on a loop
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely

    while True:
        # Display the main menu and get the user's choice
        choice = menu.get_choice()

        if choice == "START GAME":
            # Start the game loop and get the game results
            winner, winner_hits = pong_game.game_loop()

            # Display the Game Over screen
            game_over_choice = game_over_screen.get_choice(winner, winner_hits)
            
            if game_over_choice == "RESTART GAME":
                continue  # Restart the loop, showing the main menu again
            elif game_over_choice == "QUIT":
                pygame.quit()
                sys.exit()
        
        elif choice == "QUIT":
            # Quit the game if the user selects Quit
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
