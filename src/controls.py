import pygame
import sys
import os

def show_controls(screen, clock, width, height, custom_mouse):
    base_dir = os.path.dirname(__file__)

    wasd_paths = [
        os.path.join(base_dir, "../assets/WASD.png"),
        os.path.join(base_dir, "../assets/WASD_W.png"),
        os.path.join(base_dir, "../assets/WASD_S.png"),
    ]

    arrow_paths = [
        os.path.join(base_dir, "../assets/Arrow.png"),
        os.path.join(base_dir, "../assets/ArrowUp.png"),
        os.path.join(base_dir, "../assets/ArrowDown.png"),
    ]

    font_path = os.path.join(base_dir, "../assets/Extrude.ttf")
    click_sound_path = os.path.join(base_dir, "../assets/menu.mp3")

    wasd_images = [pygame.image.load(path) for path in wasd_paths]
    arrow_images = [pygame.image.load(path) for path in arrow_paths]

    wasd_images = [pygame.transform.scale(img, (150, 120)) for img in wasd_images]
    arrow_images = [pygame.transform.scale(img, (150, 120)) for img in arrow_images]

    title_font = pygame.font.Font(font_path, 48)
    instruction_font = pygame.font.Font(font_path, 34)

    # Load the click sound
    click_sound = pygame.mixer.Sound(click_sound_path)
    click_sound.set_volume(0.5)

    state = 0
    timer = 0
    interval = 30

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                click_sound.play()
                return  # Exit controls and return to the menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
                return  # Exit controls and return to the menu

        # Update animation state for images
        timer += 1
        if timer >= interval:
            timer = 0
            state = (state + 1) % len(arrow_images)

        # Fill the screen with a black background
        screen.fill((0, 0, 0))

        # Draw titles for players
        player1_text = title_font.render("Player 1", True, (255, 255, 255))
        player2_text = title_font.render("Player 2", True, (255, 255, 255))

        screen.blit(player1_text, (width // 4 - player1_text.get_width() // 2, 50))
        screen.blit(player2_text, (3 * width // 4 - player2_text.get_width() // 2, 50))

        # Draw the animated key images
        screen.blit(wasd_images[state], (width // 4 - wasd_images[state].get_width() // 2, 150))
        screen.blit(arrow_images[state], (3 * width // 4 - arrow_images[state].get_width() // 2, 150))

        # Draw the instructions text
        instructions_text = instruction_font.render("Press any key or click to return to menu", True, (200, 200, 200))
        screen.blit(instructions_text, (width // 2 - instructions_text.get_width() // 2, height - 100))

        # Draw the custom mouse cursor
        custom_mouse.draw(screen)

        pygame.display.flip()
        clock.tick(60)
