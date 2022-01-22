# 引入库
import time, pygame, sys, random

pygame.init()  # 初始化
screen = pygame.display.set_mode((844, 600))
pygame.display.set_caption("google-egg")  # 设置标题名

# 载入图片
ground5 = pygame.image.load("ground5.png")
ground6 = pygame.image.load("ground6.png")
dinosour1 = pygame.image.load("dinosour-down-up.png")
dinosour2 = pygame.image.load("dinosour-up-down.png")
dinosour3 = pygame.image.load("dinosour-stand.png")
dinosour4 = pygame.image.load("down_dinosour_right.png")
dinosour5 = pygame.image.load("down_dinosour_left.png")
dinosour6 = pygame.image.load("dinosour-die.png")
cactus1 = pygame.image.load("1-cactus.png")
cactus2 = pygame.image.load("2-cactus.png")
cactus3 = pygame.image.load("3-cactus.png")
cactus4 = pygame.image.load("4-cactus.png")
welcome = pygame.image.load("welcome.png")
bird1 = pygame.image.load("bird-up.png")
bird2 = pygame.image.load("bird-down.png")
boonball1 = pygame.image.load("boonball.white.png")
cloud1 = pygame.image.load("cloud.white.png")


# 定义输出字体函数
def drawTextT(content, a, b, c, d, e, f, g):  # 输出字体设置
    pygame.font.init()
    font = pygame.font.Font("gilroy-black-6.otf", g)
    text_sf = font.render(content, True, pygame.Color(a, b, c), pygame.Color(d, e, f))
    return text_sf


def drawTextScore(content):  # 输出字体设置
    pygame.font.init()
    font = pygame.font.Font("gilroy-black-6.otf", 30)
    text_sf = font.render(content, True, pygame.Color(0, 0, 0), pygame.Color(255, 255, 255))
    return text_sf


# 定义全局变量(global)
location, size, jumpnum = 300, 30, 0
jumpstate, jump_bool, Dlocation = 46, 1, 0
forward_state, back_state, image_state = 0, 0, 0
bg1, bg2, bg3 = 0, 680, 1360
jump_begin, colorstate, colormiddle = 1, 255, 0
screen_speed, speedmiddle, cactus_appear = 5, 0, 0
may, far, rangemiddle = 1, 0, 0
Emay = 2.5

# 获取最高分数
with open("record.txt", "r") as file:
    farthest = file.read()


# 定义恐龙class
class Dinosour():
    def __init__(self):
        global location, size
        self.image = dinosour1
        self.hp = 50
        self.rect = pygame.Rect(70, location, size, size)
        self.speed = 3

    def show(self, screen):
        screen.blit(self.image, self.rect)

    def forward(self):  # 前进
        self.rect.x = self.rect.x + self.speed

    def back(self):  # 后退
        global screen_speed
        self.rect.x = self.rect.x - screen_speed - 1

    def squat(self, x, y):
        self.rect = pygame.Rect(x, y, 65, 31)


# 定义仙人掌class
class Cactus():
    def __init__(self):
        self.high = random.randint(300, 310)
        self.r_image = random.randint(1, 4)
        if self.r_image == 1:
            self.image = cactus1
            self.rect = pygame.Rect(844, self.high, 25, 50)
        elif self.r_image == 2:
            self.image = cactus2
            self.rect = pygame.Rect(844, self.high, 50, 50)
        elif self.r_image == 3:
            self.image = cactus3
            self.rect = pygame.Rect(844, self.high, 75, 50)
        elif self.r_image == 4:
            self.image = cactus4
            self.rect = pygame.Rect(844, self.high, 77, 50)

    def show(self, screen):
        screen.blit(self.image, self.rect)

    def hit(self, dinosour):
        if self.rect.colliderect(dinosour.rect):
            dinosour.hp = dinosour.hp - 10

    def move(self):
        global screen_speed
        self.rect.x = self.rect.x - screen_speed


# 定义鸟类Class
class Bird():
    def __init__(self):
        self.rect_y = random.randint(270, 300)
        self.rect = pygame.Rect(844, self.rect_y, 41, 30)
        self.image = bird1

    def move(self):
        global screen_speed
        self.rect.x = self.rect.x - screen_speed - 2

    def show(self, screen):
        screen.blit(self.image, self.rect)

    def hit(self, dinosour):
        if self.rect.colliderect(dinosour.rect):
            dinosour.hp = dinosour.hp - 10


# 定义气球Class
class Boonball():
    def __init__(self):
        self.image = boonball1
        self.random_y = random.randint(50, 175)
        self.rect = pygame.Rect(844, self.random_y, 38, 71)

    def move(self):
        global screen_speed
        self.rect.x = self.rect.x - screen_speed + 3

    def show(self, screen):
        screen.blit(self.image, self.rect)


# 定义云Class
class Cloud():
    def __init__(self):
        self.random_y = random.randint(50, 175)
        self.image = cloud1
        self.rect = pygame.Rect(844, self.random_y, 108, 31)

    def move(self):
        global screen_speed
        self.rect.x = self.rect.x - screen_speed + 3

    def show(self, screen):
        screen.blit(self.image, self.rect)


# 制作欢迎界面
# '''
screen.fill((255, 255, 255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if colorstate == -1:
        time.sleep(3)
        break
    if colorstate == 255:
        time.sleep(1)
    screen.fill((colorstate, colorstate, colorstate))
    screen.blit(
        drawTextT("Made With", 255 - colorstate, 255 - colorstate, 255 - colorstate, colorstate, colorstate, colorstate,
                  50), (200, 200))
    screen.blit(
        drawTextT("Python", 255 - colorstate, 255 - colorstate, 255 - colorstate, colorstate, colorstate, colorstate,
                  100), (350, 250))
    colormiddle += 1
    if colormiddle % 2 == 0:
        colorstate -= 1
        colormiddle = 0
    pygame.display.update()
# '''
dinosour = Dinosour()
# 设置启动界面
jump_high = []
Dlocation = dinosour.rect.y
for i in range(48):
    jump_high.append(rangemiddle)
    if i % 2 == 0:
        rangemiddle += 0.3
screen.fill((255, 255, 255))
enter_bool, image_x, image_y = 0, 200, 100
image_middle = 0
dinosour.image = dinosour3
# '''
# 设置面板
while True:
    # 绘制图形
    screen.blit(drawTextT(str(far), 255, 255, 255, 255, 255, 255, 10), (680, 0))
    screen.blit(drawTextT(str(farthest), 255, 255, 255, 255, 255, 255, 10), (780, 0))
    screen.fill((247, 247, 247))
    screen.blit(welcome, (image_x, image_y))
    screen.blit(ground6, (70, 325))
    dinosour.show(screen)
    dinosour.rect.y = Dlocation

    # 检测按键
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if jump_begin == 0:
                    jumpnum = 92
                    jump_bool = 1
                    jump_begin = 1
                    enter_bool += 1

    # 图片动态效果
    if enter_bool >= 1 and jump_begin == 0:
        if image_middle == 0:
            jumpnum = 92
            jumpstate = 46
            jump_bool = 1
        image_middle += 1
        if jumpnum > 0 and jumpstate > 0 and jump_bool == 1:
            jumpstate -= 1
            image_y -= jump_high[jumpstate]
            jumpnum = jumpnum - 1
        elif jumpnum > 0 and jumpstate == 0 and jump_bool == 1:
            jumpstate -= 1
            jumpnum = jumpnum - 1
            jump_bool = 0
            jumpstate = -1
        elif jumpstate <= 45:
            jumpstate += 1
            image_y += jump_high[jumpstate]
            jumpnum = jumpnum - 1
        else:
            image_y += 6.9
        screen.blit(ground5, (bg1, location + 25))
        screen.blit(ground5, (bg2, location + 25))
        screen.blit(ground5, (bg3, location + 25))
        dinosour.show(screen)
        pygame.display.update()
        if image_y > 600:
            break
        continue

    # 跳跃上升及落下判断
    jump_begin = 0
    if jumpnum > 0 and jumpstate > 0 and jump_bool == 1:
        jumpstate -= 1
        jump_begin = 1
        Dlocation -= jump_high[jumpstate]
        jumpnum = jumpnum - 1
    elif jumpnum > 0 and jumpstate == 0 and jump_bool == 1:
        jumpstate -= 1
        jump_begin = 1
        jumpnum = jumpnum - 1
        jump_bool = 0
        jumpstate = -1
    elif jumpstate <= 45:
        jumpstate += 1
        jump_begin = 1
        Dlocation += jump_high[jumpstate]
        jumpnum = jumpnum - 1

    # 刷新屏幕
    pygame.display.update()
# '''
# 设置无限循环运行环境
jumpnum = 0
jumpstate, jump_bool, Dlocation = 46, 1, dinosour.rect.y
forward_state, back_state, image_state = 0, 0, 0
bg1, bg2, bg3 = 0, 680, 1360
jump_begin, colorstate, colormiddle = 0, 255, 0
speedmiddle, cactus_appear, Bspeedmiddle = 0, 0, 0
far, rangemiddle, squat_state = 0, 0, 0
squat_state_x, squat_state_y, boonball_state = 0, 0, 0
cactus, cactusnum = [], []
bird, birdnum = [], []
boonball, boonballnum = [], []
cloud, cloudnum = [], []
screen.blit(ground5, (bg1, location + 25))
screen.blit(ground5, (bg1, location + 25))
screen.blit(ground5, (bg1, location + 25))
jump_high = []

# 每次刷新跳跃高度列表
for i in range(48):
    jump_high.append(rangemiddle)
    if i % 2 == 0:
        rangemiddle += 0.3

# 设置面板
while True:
    screen.blit(drawTextScore(str(farthest)), (100, 0))
    dinosour.rect.y = Dlocation
    screen.fill((255, 255, 255))
    speedmiddle += 1

    # 退出和按键判断
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if jump_begin == 0:
                    jumpnum = 92
                    jump_bool = 1
                    jump_begin = 1
            if event.key == pygame.K_RIGHT:
                forward_state = 1
            if event.key == pygame.K_LEFT:
                back_state = 1
            if event.key == pygame.K_DOWN:
                squat_state = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                forward_state = 0
            if event.key == pygame.K_LEFT:
                back_state = 0
            if event.key == pygame.K_DOWN:
                squat_state = 0

    # dinosour下蹲检测
    if squat_state == 1:
        squat_state_x = dinosour.rect.x
        squat_state_y = dinosour.rect.y
        dinosour.squat(squat_state_x, squat_state_y)
        dinosour.rect.y += 30

    # 跳跃上升及落下判断
    jump_begin = 0
    if jumpnum > 0 and jumpstate > 0 and jump_bool == 1:
        jumpstate -= 1
        jump_begin = 1
        Dlocation -= jump_high[jumpstate]
        jumpnum = jumpnum - 1
    elif jumpnum > 0 and jumpstate == 0 and jump_bool == 1:
        jumpstate -= 1
        jump_begin = 1
        jumpnum = jumpnum - 1
        jump_bool = 0
        jumpstate = -1
    elif jumpstate <= 45:
        jumpstate += 1
        jump_begin = 1
        Dlocation += jump_high[jumpstate]
        jumpnum = jumpnum - 1

    # Dinosour前后移动控制
    if forward_state == 1:
        dinosour.forward()
    if back_state == 1:
        dinosour.back()

    # 控制Dinosour不出边界
    if dinosour.rect.x > 784:
        dinosour.rect.x = 784
    if dinosour.rect.x < 0:
        dinosour.rect.x = 0
    if dinosour.rect.y < 0:
        dinosour.rect.y = 0
    if dinosour.rect.y > 600:
        dinosour.rect.y = 600

    # 绘制屏幕背景
    screen.blit(ground5, (bg1, location + 25))
    screen.blit(ground5, (bg2, location + 25))
    screen.blit(ground5, (bg3, location + 25))
    bg1, bg2, bg3 = bg1 - screen_speed, bg2 - screen_speed, bg3 - screen_speed
    if bg2 == 0:
        bg1 = 1360
    elif bg3 == 0:
        bg2 = 1360
    elif bg1 == 0:
        bg3 = 1360

    # 显示跑的距离
    screen.blit(drawTextScore(str(far)), (680, 0))
    screen.blit(drawTextScore(str(farthest)), (780, 0))
    # screen.blit(drawTextScore("hp:"+str(dinosour.hp)), (0, 0))
    # 显示血量（打开后会使刷新速度变慢）
    if speedmiddle % 50 == 0:
        far += 1

    # Dinosour,Bird跑步动画
    image_state += 1
    Bspeedmiddle += 1
    if Bspeedmiddle == 26:
        Bspeedmiddle = 0
    if image_state == 50:
        image_state = 0
    if len(bird) >= 1:
        for i in range(len(bird)):
            if 0 <= Bspeedmiddle <= 12:
                bird[i].image = bird1
            elif 13 <= Bspeedmiddle <= 25:
                bird[i].image = bird2
    if squat_state == 0:
        if 0 <= image_state <= 24:
            dinosour.image = dinosour1
        elif 25 <= image_state <= 49:
            dinosour.image = dinosour2
    if squat_state == 1:
        if 0 <= image_state <= 24:
            dinosour.image = dinosour4
        elif 25 <= image_state <= 49:
            dinosour.image = dinosour5

    # 跳跃动画
    if dinosour.rect.y < 300 and squat_state == 0:
        dinosour.image = dinosour3

    # 重力判断
    if jump_begin == 0 and dinosour.rect.y < location:
        Dlocation = Dlocation + 3.5
    elif jump_begin == 0 and dinosour.rect.y > location:
        Dlocation = 300

    # Cactus显示及刷新
    if speedmiddle % (may * 100) == 0 and speedmiddle != 0:
        r_cactus = random.randint(0, 1)
        if r_cactus == 1:
            cactus.append(Cactus())
    if len(cactus) >= 1:
        for i in range(len(cactus)):
            cactus[i].show(screen)
            cactus[i].move()
            cactus[i].hit(dinosour)
    for i in range(len(cactus)):
        if cactus[i].rect.x <= -75:
            cactusnum.append(i)
    for i in range(len(cactusnum)):
        del cactus[cactusnum[i]]
    cactusnum = []

    # 加载Bird
    if speedmiddle % (may * 100) == 0 and speedmiddle != 0 and far >= 50:
        r_bird = random.randint(0, 1)
        if r_bird == 1:
            bird.append(Bird())
    if len(bird) >= 1:
        for i in range(len(bird)):
            bird[i].show(screen)
            bird[i].move()
            bird[i].hit(dinosour)
    for i in range(len(bird)):
        if bird[i].rect.x <= -75:
            birdnum.append(i)
    for i in range(len(birdnum)):
        del bird[birdnum[i]]
    birdnum = []

    # 加载Boonball
    boonball_state = 0
    if speedmiddle % (Emay * 100) == 0 and speedmiddle != 0:
        r_boonball = random.randint(0, 1)
        if r_boonball == 1:
            boonball.append(Boonball())
            boonball_state = 1
    if len(boonball) >= 1:
        for i in range(len(boonball)):
            boonball[i].show(screen)
            boonball[i].move()
    for i in range(len(boonball)):
        if boonball[i].rect.x <= -75:
            boonballnum.append(i)
    for i in range(len(boonballnum)):
        del boonball[boonballnum[i]]
    boonballnum = []

    # 加载Cloud
    if speedmiddle % (Emay * 50) == 0 and speedmiddle != 0 and boonball_state == 0:
        r_cloud = random.randint(0, 1)
        if r_cloud == 1:
            cloud.append(Cloud())
    if len(cloud) >= 1:
        for i in range(len(cloud)):
            cloud[i].show(screen)
            cloud[i].move()
    for i in range(len(cloud)):
        if cloud[i].rect.x <= -75:
            cloudnum.append(i)
    for i in range(len(cloudnum)):
        del cloud[cloudnum[i]]
    cloudnum = []

    # 检测Dinosour碰撞Cactus后掉血
    if dinosour.hp <= 0:
        if squat_state == 1:
            dinosour.rect.y -= 30
        dinosour.image = dinosour6
        pygame.display.update()
        dinosour.show(screen)
        pygame.display.update()
        break

    # 显示恐龙及刷新
    dinosour.show(screen)
    pygame.display.update()

# 写入跑的距离
if far > int(farthest):
    with open("record.txt", "w") as file:
        file.write(str(far))

# GAME OVER动画
middle = 0
while True:
    middle += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 闪动GAME OVER动画
    if 0 <= middle % 300 <= 149:
        screen.blit(drawTextT("Game", 0, 0, 0, 255, 255, 255, 40), (200, 100))
        screen.blit(drawTextT("Over", 0, 0, 0, 255, 255, 255, 40), (500, 100))
    elif 150 <= middle % 300 <= 299:
        screen.blit(drawTextT("Game", 255, 255, 255, 255, 255, 255, 40), (200, 100))
        screen.blit(drawTextT("Over", 255, 255, 255, 255, 255, 255, 40), (500, 100))
    pygame.display.update()
