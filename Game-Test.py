import pygame


def is_near_color(screen, direction, vector):
    color = None

    match direction:
        case "UP":
            color = screen.get_at((int(vector.x), int(vector.y - 1)))
        case "LEFT":
            color = screen.get_at((int(vector.x - 1), int(vector.y)))
        case "DOWN":
            color = screen.get_at((int(vector.x), int(vector.y + 1)))
        case "RIGHT":
            color = screen.get_at((int(vector.x + 1), int(vector.y)))

    print(color)
    return str(color) == "(0, 0, 0, 255)"


def start():
    pygame.init()

    running = True

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    dt = 0

    pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    direction = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        pygame.draw.circle(screen, "green", pos, 20)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            pos.y -= 300 * dt
            direction = "UP"

        if keys[pygame.K_a]:
            pos.x -= 300 * dt
            direction = "LEFT"

        if keys[pygame.K_s]:
            pos.y += 300 * dt
            direction = "DOWN"

        if keys[pygame.K_d]:
            pos.x += 300 * dt
            direction = "RIGHT"

        copy = pos.copy()
        if is_near_color(screen, direction, copy):
            print("test")

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    start()
