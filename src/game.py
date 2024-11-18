import pygame
import sys
import random
from paddle import Paddle
from ball import Ball
from menu import Menu
from game_over import GameOver

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
FONT_SIZE = 36

# Star Constants
STAR_COUNT = 150
STAR_SPEED = 2
MAX_ALPHA = 255  # Maximum brightness
MIN_ALPHA = 30  # Minimum brightness

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", FONT_SIZE)

# Initialize Menu and GameOver
menu = Menu(screen, WIDTH, HEIGHT)
game_over_screen = GameOver(screen, WIDTH, HEIGHT)

# Initialize Stars
stars = [
    {
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "speed": random.uniform(0.5, 2),
        "alpha": random.randint(MIN_ALPHA, MAX_ALPHA),
        "alpha_direction": random.choice([-1, 1]),  # Controls twinkle direction
    }
    for _ in range(STAR_COUNT)
]

def update_starfield():
    """Update the position and twinkle effect of stars."""
    for star in stars:
        # Move the star
        star["x"] -= star["speed"]
        if star["x"] < 0:  # If the star goes off-screen, reset its position
            star["x"] = WIDTH
            star["y"] = random.randint(0, HEIGHT)
            star["speed"] = random.uniform(0.5, 2)

        # Adjust alpha for the twinkle effect
        star["alpha"] += star["alpha_direction"] * 5  # Change brightness gradually
        if star["alpha"] >= MAX_ALPHA:  # Reverse direction if maximum brightness is reached
            star["alpha"] = MAX_ALPHA
            star["alpha_direction"] = -1
        elif star["alpha"] <= MIN_ALPHA:  # Reverse direction if minimum brightness is reached
            star["alpha"] = MIN_ALPHA
            star["alpha_direction"] = 1

def draw_starfield():
    """Draw the stars on the screen with their current alpha values and size based on speed."""
    for star in stars:
        star_size = int(star["speed"] * 1.5)  # Larger stars move faster
        star_surface = pygame.Surface((star_size, star_size), pygame.SRCALPHA)  # Create a surface matching star size
        star_surface.fill((255, 255, 255, star["alpha"]))  # RGBA: white with alpha
        screen.blit(star_surface, (star["x"], star["y"]))


def game_loop():
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
        if ball.rect.colliderect(paddle1.rect):
            ball.speed_x = -ball.speed_x  # Reverse ball direction
            player1_hits += 1            # Increment Player 1's hit count
        elif ball.rect.colliderect(paddle2.rect):
            ball.speed_x = -ball.speed_x  # Reverse ball direction
            player2_hits += 1            # Increment Player 2's hit count

        # Check for losing condition (ball out of bounds)
        if ball.rect.left <= 0:
            return "Player 2", player2_hits  # Player 2 wins, return their hits
        elif ball.rect.right >= WIDTH:
            return "Player 1", player1_hits  # Player 1 wins, return their hits

        # Draw everything
        screen.fill((0, 0, 0))  # Clear the screen
        draw_starfield()  # Draw the scrolling starfield
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)
        pygame.display.flip()  # Update the display

        # Control frame rate
        clock.tick(60)


def main():
    while True:
        choice = menu.get_choice()
        if choice == "START GAME":
            # Unpack only the two values returned by game_loop
            winner, winner_hits = game_loop()
            # Show the Game Over screen with the winner and their hit count
            game_over_choice = game_over_screen.get_choice(winner, winner_hits)
            if game_over_choice == "RESTART GAME":
                continue  # Restart the loop, showing the main menu again
            elif game_over_choice == "QUIT":
                pygame.quit()
                sys.exit()
        elif choice == "QUIT":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
