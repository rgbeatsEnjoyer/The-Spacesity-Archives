import pygame
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen_width, screen_height = 1280, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 20)
    pygame.key.set_repeat(20)

    fps = 60
    player_image = pygame.image.load("images//player.png").convert()

    class General:
        def game_exit(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()

        def screen_control(self):
            pygame.display.flip()
            pygame.display.update()
            clock.tick(fps)

    class Player:
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.image = image

        def movement(self, speed, delta_time):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.x -= speed * delta_time
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.x += speed * delta_time
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                self.y -= speed * delta_time
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.y += speed * delta_time

        def display(self):
            screen.blit(self.image, (self.x, self.y))

    player1 = Player(screen_width / 2 - 100, screen_height / 2 - 100, player_image)
    general = General()

    while True:
        delta_time = clock.tick(fps) / 1000.0  # Convert to seconds
        screen.fill((255, 255, 255))

        general.game_exit()

        player1.movement(1000, delta_time)

        player1.display()
        general.screen_control()

try:
    if __name__ == "__main__":
        main()
except Exception as exception:
    print(f"{exception}")
finally:
    pygame.display.quit()
    pygame.quit()
    sys.exit()

