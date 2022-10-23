import pygame
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    bk = pygame.image.load('space1.png').convert()

    clock = pygame.time.Clock()
    while True:
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        # Do logical updates here
        #screen.fill('purple')
        # Render the graphics here
        pygame.display.flip()
        clock.tick(60)



# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
