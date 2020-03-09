import pygame
def main():
    #初始化导入的pygame中的模块
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    screen.fill((242,242,242))
    pygame.draw.circle(screen,(255,0,0,),(100,100),30,0)
    pygame.display.flip()
    running=True
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()