import pygame
import random

# Constants for the starfield
WIDTH = 800
HEIGHT = 600
STAR_COUNT = 150
STAR_SPEED = 2
MAX_ALPHA = 255  # Maximum brightness
MIN_ALPHA = 30  # Minimum brightness

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

def draw_starfield(screen):
    """Draw the stars on the screen with their current alpha values and size based on speed."""
    for star in stars:
        star_size = int(star["speed"] * 1.5)  # Larger stars move faster
        star_surface = pygame.Surface((star_size, star_size), pygame.SRCALPHA)  # Create a surface matching star size
        star_surface.fill((255, 255, 255, star["alpha"]))  # RGBA: white with alpha
        screen.blit(star_surface, (star["x"], star["y"]))