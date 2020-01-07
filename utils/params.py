from enum import Enum

# 窗框宽度
WINDOW_PADDING = 8
# 最小块单位大小
BLOCK = 60

# 游戏区域
GAME_WIDTH = 13 * BLOCK
GAME_HEIGHT = 13 * BLOCK

# 列表信息窗体
INFO_WIDTH = 4 * BLOCK
INFO_HEIGHT = GAME_HEIGHT

# 窗体的参数
WINDOW_WIDTH = 13 * BLOCK + 3 * WINDOW_PADDING + INFO_WIDTH
WINDOW_HEIGHT = 13 * BLOCK + 2 * WINDOW_PADDING


# 坦克方向
class Direction(Enum):
    NONE = -1
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


# 主体坦克的速度
player_rare = 15

# 子弹的速度
bullet_rare = 30

# 碰撞系数
inflict_param = 15
