import pygame
import settings

pygame.init()

screen = pygame.display.set_mode((settings.leenght, settings.width))
pygame.display.set_caption(settings.name)

icon = pygame.image.load(settings.pic)
pygame.display.set_icon(icon)

player = pygame.Surface((settings.player_lenght, settings.player_width))
player2 = pygame.Surface((settings.player_lenght, settings.player_width))

player.fill(settings.player_color)
player2.fill(settings.player_color)

font = pygame.font.SysFont("Arial", 40)
game_over_font = pygame.font.SysFont("Arial", 80)

player1_y = settings.player_y

score_player1 = 0
score_player2 = 0

max_score = 5

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and player1_y > 0:
            player1_y -= 3
        if keys[pygame.K_s] and player1_y + settings.player_width < settings.width:
            player1_y += 3

        settings.cyrcle_center_x += settings.cyrcle_speed_x
        settings.cyrcle_center_y += settings.cyrcle_speed_y

        player2_y = settings.cyrcle_center_y - settings.player_width // 2

        if settings.cyrcle_center_x >= settings.leenght:
            score_player1 += 1
            settings.cyrcle_center_x = settings.center_x
            settings.cyrcle_center_y = settings.center_y
            settings.cyrcle_speed_x *= -1

        if settings.cyrcle_center_x <= 0:
            score_player2 += 1
            settings.cyrcle_center_x = settings.center_x
            settings.cyrcle_center_y = settings.center_y
            settings.cyrcle_speed_x *= -1

        if settings.cyrcle_center_y >= settings.width or settings.cyrcle_center_y <= 0:
            settings.cyrcle_speed_y *= -1

        if score_player1 >= max_score or score_player2 >= max_score:
            game_over = True

    screen.fill(settings.color)

    player2_x = settings.leenght - settings.player_lenght - settings.player_x

    if not game_over:

        player1_rect = pygame.Rect(settings.player_x, player1_y, settings.player_lenght, settings.player_width)
        player2_rect = pygame.Rect(player2_x, player2_y, settings.player_lenght, settings.player_width)
        circle_rect = pygame.Rect(
            settings.cyrcle_center_x - settings.cyrcle_radius,
            settings.cyrcle_center_y - settings.cyrcle_radius,
            settings.cyrcle_radius * 2,
            settings.cyrcle_radius * 2
        )

        if player1_rect.colliderect(circle_rect) or player2_rect.colliderect(circle_rect):
            settings.cyrcle_speed_x *= -1

        pygame.draw.circle(
            screen,
            settings.cyrcle_color,
            (settings.cyrcle_center_x, settings.cyrcle_center_y),
            settings.cyrcle_radius
        )

        screen.blit(player, (settings.player_x, player1_y))
        screen.blit(player2, (player2_x, player2_y))

    pygame.draw.line(
        screen,
        settings.line_color,
        (settings.center_x, 0),
        (settings.center_x, settings.width),
        2
    )

    text1 = font.render(str(score_player1), True, (255, 255, 255))
    text2 = font.render(str(score_player2), True, (255, 255, 255))
    screen.blit(text1, (50, 20))
    screen.blit(text2, (settings.leenght - 100, 20))

    if game_over:
        winner = "Player1" if score_player1 >= max_score else "Player2"
        game_over_text = game_over_font.render(f"Game Over! {winner} Wins!", True, (255, 0, 0))
        screen.blit(game_over_text, (settings.leenght // 2 - game_over_text.get_width() // 2,
                                     settings.width // 2 - game_over_text.get_height() // 2))

    pygame.display.update()
