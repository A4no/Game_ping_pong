import pygame
import settings

pygame.init()

# Էկրան
screen = pygame.display.set_mode((settings.leenght, settings.width))
pygame.display.set_caption(settings.name)

icon = pygame.image.load(settings.pic)
pygame.display.set_icon(icon)

# Player-ներ
player = pygame.Surface((settings.player_lenght, settings.player_width))
player2 = pygame.Surface((settings.player_lenght, settings.player_width))

player.fill(settings.player_color)
player2.fill(settings.player_color)

# Font score-ի համար
font = pygame.font.SysFont("Arial", 40)

# Player-ների անկախ Y դիրքեր
player1_y = settings.player_y
player2_y = settings.player_y

# Score
score_player1 = 0
score_player2 = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    keys = pygame.key.get_pressed()

    # Player1 (W/S)
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= 3
    if keys[pygame.K_s] and player1_y + settings.player_width < settings.width:
        player1_y += 3

    # Player2 (UP/DOWN)
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 3
    if keys[pygame.K_DOWN] and player2_y + settings.player_width < settings.width:
        player2_y += 3

    # Շրջանի շարժում
    settings.cyrcle_center_x += settings.cyrcle_speed_x
    settings.cyrcle_center_y += settings.cyrcle_speed_y

    # Եթե դիպչի եզրին՝ հետ շրջվի
    if settings.cyrcle_center_x >= settings.leenght:
        score_player1 += 1  # Player1 է ստանում միավոր
        settings.cyrcle_speed_x *= -1

        settings.cyrcle_center_x = settings.center_x
        settings.cyrcle_center_y = settings.center_y
    if settings.cyrcle_center_x <= 0:
        score_player2 += 1  # Player2 է ստանում միավոր
        settings.cyrcle_speed_x *= -1
        settings.cyrcle_center_x = settings.center_x
        settings.cyrcle_center_y = settings.center_y
    if settings.cyrcle_center_y >= settings.width or settings.cyrcle_center_y <= 0:
        settings.cyrcle_speed_y *= -1

    screen.fill(settings.color)

    # Player2 X դիրքը
    player2_x = settings.leenght - settings.player_lenght - settings.player_x

    # Բախման Rect-ներ
    player1_rect = pygame.Rect(settings.player_x, player1_y, settings.player_lenght, settings.player_width)
    player2_rect = pygame.Rect(player2_x, player2_y, settings.player_lenght, settings.player_width)
    circle_rect = pygame.Rect(
        settings.cyrcle_center_x - settings.cyrcle_radius,
        settings.cyrcle_center_y - settings.cyrcle_radius,
        settings.cyrcle_radius * 2,
        settings.cyrcle_radius * 2
    )

    # Բախումներ
    if player1_rect.colliderect(circle_rect) or player2_rect.colliderect(circle_rect):
        settings.cyrcle_speed_x *= -1

    # Նկարում ենք circle
    pygame.draw.circle(
        screen,
        settings.cyrcle_color,
        (settings.cyrcle_center_x, settings.cyrcle_center_y),
        settings.cyrcle_radius
    )

    # Կենտրոնական գիծ
    pygame.draw.line(
        screen,
        settings.line_color,
        (settings.center_x, 0),
        (settings.center_x, settings.width),
        2
    )

    # Նկարում ենք player-ները
    screen.blit(player, (settings.player_x, player1_y))
    screen.blit(player2, (player2_x, player2_y))

    # Նկարում ենք score
    text1 = font.render(str(score_player1), True, (255, 255, 255))
    text2 = font.render(str(score_player2), True, (255, 255, 255))

    screen.blit(text1, (50, 20))  # ձախ վերև
    screen.blit(text2, (settings.leenght - 250, 20))  # աջ վերև

    pygame.display.update()
