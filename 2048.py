import pygame
import random
import sys

pygame.init()

WIDTH = 650
HEIGHT = 790

TWO_COLOR = (249, 249, 236)
FOUR_COLOR = (255, 255, 204)
EIGHT_COLOR = (255, 204, 153)
SIXTEEN_COLOR = (255, 178, 102)
THIRTY_TWO_COLOR = (245, 164, 164)
SIXTY_FOUR_COLOR = (242, 99, 28)
ONE_TWENTY_EIGHT_COLOR = (249, 219, 101)
TWO_FIFTY_SIX_COLOR = (249, 219, 101)
FIVE_TWELVE_COLOR = (249, 219, 101)
TEN_TWENTY_FOUR_COLOR = (249, 219, 101)
TWNETY_FOURTY_EIGHT_COLOR = (249, 219, 101)
BACKGROUND_COLOR = (253, 255, 225)
SUB_BACKGROUND_COLOR = (175, 175, 175)
GREY_TEXT_COLOR = (111, 111, 111)
WHITE_TEXT_COLOR = (239, 239, 239)
block_size = 100
border_size = 10

matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

score = 0

clock = pygame.time.Clock()

file = open("highscore.txt", "r")
hs = file.readline()
highscore = int(hs)
file.close()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False


def generate_num(game_start):
    empty = False
    for r in range(0, 4):
        for i in range(0, 4):
            if matrix[i][r] == 0:
                empty = True
    if empty:
        temp = random.randint(0, 10)
        if temp == 1:
            num = 4
        else:
            num = 2
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while matrix[y][x] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        matrix[y][x] = num


def draw_background():
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, (121, 121, 121), (101, 290, 450, 450))
    text = "2048"
    my_font = pygame.font.SysFont('monospace', 170)
    label = my_font.render(text, 1, (255, 153, 51))
    screen.blit(label, (110, 40))
    pygame.draw.rect(screen, SIXTEEN_COLOR, (425, 70, 120, 50))
    textN = "NEW GAME"
    my_font = pygame.font.SysFont('monospace', 26)
    label = my_font.render(textN, 1, (255, 255, 255))
    screen.blit(label, (435, 86))
    for r in range(0, 4):
        for i in range(0, 4):
            pygame.draw.rect(screen, SUB_BACKGROUND_COLOR, (111 + 110*i, 300 + 110*r, block_size, block_size))
    for l in range(0, 2):
        pygame.draw.rect(screen, (168, 168, 168), (100+230*l, 170, 220, 100))
    text2 = "SCORE"
    my_font2 = pygame.font.SysFont('monospace', 40)
    label2 = my_font2.render(text2, 1, (239, 239, 239))
    screen.blit(label2, (160, 185))
    text3 = "BEST"
    label3 = my_font2.render(text3, 1, (239, 239, 239))
    screen.blit(label3, (400, 185))


def draw_nums():
    for r in range(0, 4):
        for i in range(0, 4):
            coord = matrix[r][i]
            pygame.draw.rect(screen, get_color(coord), (111 + 110*i, 300 + 110*r, block_size, block_size))
            text = str(coord)
            my_font = pygame.font.SysFont('monospace', get_font(coord))
            label = my_font.render(text, 1, get_text_color(coord))
            screen.blit(label, (get_coordx(coord) + 110*i, get_coordy(coord) + 110*r))


def get_coordx(num):
    if num <= 8:
        return 141
    elif num <= 64:
        return 130
    elif num <= 512:
        return 126
    else:
        return 119


def get_x_coord(num):
    if num < 10:
        return 200
    elif num < 100:
        return 190
    elif num < 1000:
        return 170
    elif num < 10000:
        return 165
    else:
        return 155


def get_y_coord(num):
    if num < 10:
        return 218
    elif num < 100:
        return 220
    elif num < 1000:
        return 223
    elif num < 10000:
        return 223
    else:
        return 223


def get_coordy(num):
    if num <= 8:
        return 325
    elif num <= 64:
        return 330
    else:
        return 335


def get_font(num):
    if num < 10:
        return 90
    elif num < 100:
        return 80
    elif num < 1000:
        return 60
    elif num < 10000:
        return 50
    else:
        return 40


def get_text_color(num):
    if num == 0:
        return SUB_BACKGROUND_COLOR
    elif num == 2 or num == 4:
        return GREY_TEXT_COLOR
    else:
        return WHITE_TEXT_COLOR


def get_color(num):
    if num == 0:
        return SUB_BACKGROUND_COLOR
    elif num == 2:
        return TWO_COLOR
    elif num == 4:
        return FOUR_COLOR
    elif num == 8:
        return EIGHT_COLOR
    elif num == 16:
        return SIXTEEN_COLOR
    elif num == 32:
        return THIRTY_TWO_COLOR
    elif num == 64:
        return SIXTY_FOUR_COLOR
    elif num == 128:
        return ONE_TWENTY_EIGHT_COLOR
    elif num == 256:
        return TWO_FIFTY_SIX_COLOR
    elif num == 512:
        return FIVE_TWELVE_COLOR
    elif num == 1024:
        return TEN_TWENTY_FOUR_COLOR
    elif num == 2048:
        return TWNETY_FOURTY_EIGHT_COLOR


def draw_scores():
    text = str(score)
    my_font = pygame.font.SysFont('monospace', 55)
    label = my_font.render(text, 1, WHITE_TEXT_COLOR)
    screen.blit(label, (get_x_coord(score), get_y_coord(score)))

    text2 = str(highscore)
    label2 = my_font.render(text2, 1, WHITE_TEXT_COLOR)
    screen.blit(label2, (get_x_coord(highscore) + 230, get_y_coord(highscore)))


def draw_game_over():
    text = "GAME OVER"
    my_font = pygame.font.SysFont('monospace', 100)
    label = my_font.render(text, 1, GREY_TEXT_COLOR)
    screen.blit(label, (115, 450))


def move(direction):
    clone = make_clone(matrix)
    global score
    if direction == "LEFT":
        slide("LEFT")
        for r in range(0, 4):
            for i in range(0, 3):
                if matrix[r][i] == matrix[r][i+1]:
                    matrix[r][i+1] = 0
                    num = matrix[r][i]
                    temp = num * 2
                    matrix[r][i] = temp
                    score += temp
        slide("LEFT")
    elif direction == "RIGHT":
        slide("RIGHT")
        for r in range(0, 4):
            for i in range(0, 3):
                if matrix[r][3-i] == matrix[r][3-i-1]:
                    matrix[r][3-i-1] = 0
                    num = matrix[r][3-i]
                    temp = num*2
                    matrix[r][3-i] = temp
                    score += temp
        slide("RIGHT")
    elif direction == "UP":
        slide("UP")
        for r in range(0, 3):
            for i in range(0, 4):
                if matrix[r][i] == matrix[r+1][i]:
                    matrix[r+1][i] = 0
                    num = matrix[r][i]
                    temp = num*2
                    matrix[r][i] = temp
                    score += temp
        slide("UP")
    elif direction == "DOWN":
        slide("DOWN")
        for r in range(0, 3):
            for i in range(0, 4):
                if matrix[3-r][i] == matrix[3-r-1][i]:
                    matrix[3-r-1][i] = 0
                    num = matrix[3-r][i]
                    temp = num*2
                    matrix[3-r][i] = temp
                    score += temp
        slide("DOWN")
    draw_nums()
    if not check_equal(clone, matrix):
        # also draws generated num
        generate_num(False)
    if check_game_over():
        global game_over
        game_over = True


def check_equal(board1, board2):
    for r in range(0, 4):
        for i in range(0, 4):
            if board1[r][i] != board2[r][i]:
                return False
    return True


def make_clone(board):
    clone = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    for r in range(0, 4):
        for i in range(0, 4):
            clone[r][i] = board[r][i]
    return clone


def check_game_over():
    global matrix
    clone = matrix
    clone2 = matrix
    for r in range(0, 4):
        for i in range(0, 4):
            if matrix[r][i] == 0:
                return False
    slide("LEFT")
    for r in range(0, 4):
        for i in range(0, 3):
            if matrix[r][i] == matrix[r][i+1]:
                matrix = clone
                return False
    matrix = clone
    slide("UP")
    for r in range(0, 3):
        for i in range(0, 4):
            if matrix[r][i] == matrix[r + 1][i]:
                matrix = clone2
                return False
    return True


def slide(direction):
    global matrix
    if direction == "LEFT":
        for x in range(0, 3):
            for r in range(0, 4):
                for i in range(0, 3):
                    if matrix[r][i] == 0:
                        temp = matrix[r][i+1]
                        matrix[r][i] = temp
                        matrix[r][i+1] = 0
    elif direction == "RIGHT":
        for x in range(0, 3):
            for r in range(0, 4):
                for i in range(0, 3):
                    if matrix[r][3-i] == 0:
                        temp = matrix[r][3-i-1]
                        matrix[r][3-i] = temp
                        matrix[r][3-i-1] = 0
    elif direction == "UP":
        for x in range(0, 3):
            for r in range(0, 3):
                for i in range(0, 4):
                    if matrix[r][i] == 0:
                        temp = matrix[r+1][i]
                        matrix[r][i] = temp
                        matrix[r+1][i] = 0
    elif direction == "DOWN":
        for x in range(0, 3):
            for r in range(0, 3):
                for i in range(0, 4):
                    if matrix[3-r][i] == 0:
                        temp = matrix[3-r-1][i]
                        matrix[3-r][i] = temp
                        matrix[3-r-1][i] = 0


def new_game():
    global matrix
    matrix = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    global score
    score = 0
    global game_over
    game_over = False
    for z in range(2):
        generate_num(True)


for n in range(2):
    generate_num(True)

game_quit = False

while not game_quit:

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file2 = open('highscore.txt', "w")
                file2.write(str(highscore))
                file2.close()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 425 <= mouse_pos[0] <= 545 and 70 <= mouse_pos[1] <= 120:
                    new_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move("LEFT")
                elif event.key == pygame.K_RIGHT:
                    move("RIGHT")
                elif event.key == pygame.K_UP:
                    move("UP")
                elif event.key == pygame.K_DOWN:
                    move("DOWN")

        if score >= highscore:
            highscore = score

        draw_background()
        draw_nums()
        draw_scores()
        # draw_game_over()
        pygame.display.update()

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file2 = open('highscore.txt', "w")
                file2.write(str(highscore))
                file2.close()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 425 <= mouse_pos[0] <= 545 and 70 <= mouse_pos[1] <= 120:
                    new_game()
        draw_game_over()
        pygame.display.update()
