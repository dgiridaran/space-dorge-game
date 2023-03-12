import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE DORGE")

BG = pygame.transform.scale(pygame.image.load(".\\images\\background.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HIGHT = 60

STAR_WIDTH = 30
STAR_HIGHT = 50

PLAYER_VEL = 5
STAR_VEL = 3
FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, stars, life):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")

    life_text = FONT.render(f"life: {life}", 1, "white")
    WIN.blit(time_text, (10,10))
    WIN.blit(life_text, (1100, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    pygame.display.update()


def main():
    run =True
    hit = False
    life = 3
    player = pygame.Rect(200, HEIGHT - PLAYER_HIGHT, PLAYER_WIDTH, PLAYER_HIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH)
                star = pygame.Rect(star_x, -STAR_HIGHT, STAR_WIDTH, STAR_HIGHT)
                stars.append(star)
            
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                life -= 1
                break
        
        if life <= 0:
            lost_text = FONT.render("You Lost", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars, life)
    pygame.quit()

if __name__ == "__main__":
    main()
