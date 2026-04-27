import pygame
import sys

# 棋盤大小
BOARD_SIZE = 15

# 棋盤格大小
GRID_SIZE = 40

# 棋盤邊距
MARGIN = 20

# 棋盤顏色
BOARD_COLOR = (200, 200, 200)

# 棋子顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 遊戲狀態
EMPTY = 0
BLACK_STONE = 1
WHITE_STONE = 2

# 初始化 Pygame
pygame.init()

# 設定視窗大小
screen = pygame.display.set_mode((BOARD_SIZE * GRID_SIZE + MARGIN * 2, BOARD_SIZE * GRID_SIZE + MARGIN * 2))

# 設定視窗標題
pygame.display.set_caption("五子棋")

# 建立棋盤
board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# 目前玩家
current_player = BLACK_STONE

# 判斷輸贏
def check_win(row, col, player):
    # 檢查水平方向
    count = 1
    for i in range(1, 5):
        if col + i < BOARD_SIZE and board[row][col + i] == player:
            count += 1
        else:
            break
    for i in range(1, 5):
        if col - i >= 0 and board[row][col - i] == player:
            count += 1
        else:
            break
    if count >= 5:
        return True

    # 檢查垂直方向
    count = 1
    for i in range(1, 5):
        if row + i < BOARD_SIZE and board[row + i][col] == player:
            count += 1
        else:
            break
    for i in range(1, 5):
        if row - i >= 0 and board[row - i][col] == player:
            count += 1
        else:
            break
    if count >= 5:
        return True

    # 檢查右下斜線方向
    count = 1
    for i in range(1, 5):
        if row + i < BOARD_SIZE and col + i < BOARD_SIZE and board[row + i][col + i] == player:
            count += 1
        else:
            break
    for i in range(1, 5):
        if row - i >= 0 and col - i >= 0 and board[row - i][col - i] == player:
            count += 1
        else:
            break
    if count >= 5:
        return True

    # 檢查左下斜線方向
    count = 1
    for i in range(1, 5):
        if row + i < BOARD_SIZE and col - i >= 0 and board[row + i][col - i] == player:
            count += 1
        else:
            break
    for i in range(1, 5):
        if row - i >= 0 and col + i < BOARD_SIZE and board[row - i][col + i] == player:
            count += 1
        else:
            break
    if count >= 5:
        return True

    return False

# 遊戲迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # 取得滑鼠點擊位置
            x, y = event.pos

            # 計算棋盤格位置
            row = round((y - MARGIN) / GRID_SIZE)
            col = round((x - MARGIN) / GRID_SIZE)

            # 判斷是否在棋盤內
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == EMPTY:
                # 下棋
                board[row][col] = current_player

                # 判斷輸贏
                if check_win(row, col, current_player):
                    print("玩家", "黑" if current_player == BLACK_STONE else "白", "獲勝！")
                    pygame.quit()
                    sys.exit()

                # 切換玩家
                current_player = WHITE_STONE if current_player == BLACK_STONE else BLACK_STONE

    # 繪製棋盤
    screen.fill(BOARD_COLOR)
    for i in range(BOARD_SIZE):
        pygame.draw.line(screen, BLACK, (MARGIN, MARGIN + i * GRID_SIZE), (MARGIN + (BOARD_SIZE - 1) * GRID_SIZE, MARGIN + i * GRID_SIZE))
        pygame.draw.line(screen, BLACK, (MARGIN + i * GRID_SIZE, MARGIN), (MARGIN + i * GRID_SIZE, MARGIN + (BOARD_SIZE - 1) * GRID_SIZE))

    # 繪製棋子
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] != EMPTY:
                color = BLACK if board[row][col] == BLACK_STONE else WHITE
                pygame.draw.circle(screen, color, (MARGIN + col * GRID_SIZE, MARGIN + row * GRID_SIZE), GRID_SIZE // 2 - 2)

    # 更新畫面
    pygame.display.flip()