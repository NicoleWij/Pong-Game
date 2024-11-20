import pygame

class Paddle:
    def __init__(self, x, y, width, height, screen_height):
        self.rect = pygame.Rect(x, y, width, height)
        self.screen_height = screen_height

    def move(self, up_key, down_key, speed):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= speed
        if keys[down_key] and self.rect.bottom < self.screen_height:
            self.rect.y += speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def handle_collision(self, ball, up_key, down_key):
        """Handle collision between paddle and ball."""
        if self.rect.colliderect(ball.rect):
            keys = pygame.key.get_pressed()
            # Add spin if the paddle is moving
            if keys[up_key]:  # Paddle moving up
                ball.speed_y -= 1
            elif keys[down_key]:  # Paddle moving down
                ball.speed_y += 1

            # Calculate collision point
            relative_intersect_y = (self.rect.centery - ball.rect.centery) / (self.rect.height / 2)
            ball.speed_y = -relative_intersect_y * abs(ball.speed_x)  # Adjust vertical speed
            ball.speed_x = -ball.speed_x  # Reverse horizontal speed
            return True  # Collision occurred
        return False  # No collision
