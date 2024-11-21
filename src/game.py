import pygame
import sys
import os
from paddle import Paddle
from ball import Ball
from menu import Menu
from game_over import GameOver
from starfield import update_starfield, draw_starfield
from mouse import Mouse

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
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

def game_loop():
    """Main game loop for PONG."""
    # Initialize paddles, ball, and hit counters
    paddle1 = Paddle(10, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT, HEIGHT)
    paddle2 = Paddle(WIDTH - 20, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT, HEIGHT)
    ball = Ball(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, 5, 5, WIDTH, HEIGHT)
    player1_hits = 0
    player2_hits = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update
        update_starfield()

        # Move paddles and ball
        paddle1.move(pygame.K_w, pygame.K_s, 5)
        paddle2.move(pygame.K_UP, pygame.K_DOWN, 5)
        ball.move()

        # Check for collisions and update hit counters
        if paddle1.handle_collision(ball, pygame.K_w, pygame.K_s):
            ball_sound.play()
            player1_hits += 1
        elif paddle2.handle_collision(ball, pygame.K_UP, pygame.K_DOWN):
            ball_sound.play()
            player2_hits += 1

        # Check for losing condition (ball out of bounds)
        if ball.rect.left <= 0:
            game_over_sound.play()
            return "Player 2", player2_hits  # Player 2 wins, return their hits
        elif ball.rect.right >= WIDTH:
            game_over_sound.play()
            return "Player 1", player1_hits  # Player 1 wins, return their hits

        # Draw everything
        screen.fill((0, 0, 0))  # Clear the screen
        draw_starfield(screen)  # Draw the scrolling starfield
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)

        # Draw custom mouse cursor
        custom_mouse.draw(screen)

        pygame.display.flip()  # Update the display

        # Control frame rate
        clock.tick(60)

def main():
    """Main entry point for the PONG game."""
    # Play background music on a loop
    pygame.mixer.music.set_volume(0.5)  # Set volume (0.0 to 1.0)
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely
    
    while True:
        # Display the main menu and get the user's choice
        choice = menu.get_choice()
        
        if choice == "START GAME":
            # Start the game loop and get the game results
            winner, winner_hits = game_loop()

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
