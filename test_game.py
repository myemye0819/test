import pygame, sys
pygame.init()
print("py init OK")   # (브라우저 콘솔에 찍힘)

# 캔버스 크기: 640x360
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 360
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("테스트 게임")

clock = pygame.time.Clock()
running = True
t = 0

while running and t < 3000:  # 3000 프레임(테스트용)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30,30,30))
    pygame.draw.circle(screen, (255,200,0), (int(SCREEN_WIDTH*0.25+t%300/300*200), SCREEN_HEIGHT//2), 20)
    pygame.display.flip()
    clock.tick(30)
    t += 1

print("test finished")
pygame.quit()
