import pygame
import sys
from paddle import Paddle
from ball import Ball
from starfield import update_starfield, draw_starfield
from mouse import Mouse

class PongGame:
    def __init__(self, screen, clock, custom_mouse, ball_sound, game_over_sound):
        self.screen = screen
        self.clock = clock
        self.custom_mouse = custom_mouse
        self.ball_sound = ball_sound
        self.game_over_sound = game_over_sound

        # Constants
        self.WIDTH, self.HEIGHT = 800, 600
        self.PADDLE_WIDTH, self.PADDLE_HEIGHT = 10, 100
        self.BALL_SIZE = 15

    def game_loop(self):
        """Main game loop for PONG."""
        paddle1 = Paddle(10, (self.HEIGHT - self.PADDLE_HEIGHT) // 2, self.PADDLE_WIDTH, self.PADDLE_HEIGHT, self.HEIGHT)
        paddle2 = Paddle(self.WIDTH - 20, (self.HEIGHT - self.PADDLE_HEIGHT) // 2, self.PADDLE_WIDTH, self.PADDLE_HEIGHT, self.HEIGHT)
        ball = Ball(self.WIDTH // 2 - self.BALL_SIZE // 2, self.HEIGHT // 2 - self.BALL_SIZE // 2, self.BALL_SIZE, 5, 5, self.WIDTH, self.HEIGHT)

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
                self.ball_sound.play()
                player1_hits += 1
            elif paddle2.handle_collision(ball, pygame.K_UP, pygame.K_DOWN):
                self.ball_sound.play()
                player2_hits += 1

            # Check for losing condition (ball out of bounds)
            if ball.rect.left <= 0:
                self.game_over_sound.play()
                return "Player 2", player2_hits  # Player 2 wins, return their hits
            elif ball.rect.right >= self.WIDTH:
                self.game_over_sound.play()
                return "Player 1", player1_hits  # Player 1 wins, return their hits

            # Draw everything
            self.screen.fill((0, 0, 0))  # Clear the screen
            draw_starfield(self.screen)  # Draw the scrolling starfield
            paddle1.draw(self.screen)
            paddle2.draw(self.screen)
            ball.draw(self.screen)

            # Draw custom mouse cursor
            self.custom_mouse.draw(self.screen)

            pygame.display.flip()  # Update the display

            # Control frame rate
            self.clock.tick(60)
