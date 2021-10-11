import pygame
import sys
from random import randrange as rnd

WIN_WIDTH = 640
WIN_HEIGHT = 480
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
LIGHT_BLUE = (64, 128, 255)

FPS = 60
paddle_w = 100
paddle_h = 5
paddle_speed = 15

paddle = pygame.Rect(WIN_WIDTH // 2 - paddle_w // 2, WIN_HEIGHT - paddle_h - 10, paddle_w, paddle_h)

pygame.init()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

# скорость шарика
ball_speed = 2
# радиус будущего круга
ball_r = 10
# вписанный в шарик квадрат
ball_rect = int(ball_r * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, WIN_WIDTH - ball_rect), WIN_HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # заливаем фон
    sc.fill(WHITE)
    pygame.draw.rect(sc, pygame.Color(ORANGE), paddle)
    pygame.draw.circle(sc, pygame.Color(LIGHT_BLUE), ball.center, ball_r)
    # движение шарика
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy
    # collision left right
    if ball.centerx < ball_r or ball.centerx > WIN_WIDTH - ball_r:
        dx = -dx
    # collision top
    if ball.centery < ball_r:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # обработка нажатия стрелок влево / вправо
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIN_WIDTH:
        paddle.right += paddle_speed

    # рисуем круг

    # pygame.draw.circle(sc, ORANGE, (x, y), r)
    # обновляем окно
    pygame.display.update()

    clock.tick(FPS)