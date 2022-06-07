from Champions.champions import *
from Utility.champions_stats_template import generate_champions_stats_template
from Trainer.processing import get_game_stats

from skimage.filters import threshold_otsu
# from scipy.ndimage import convolve

import win32gui
import matplotlib.pyplot as plt

get_game_stats()

# def check_tab_position(img, pattern) -> list:

#     img_rows, img_cols = img.shape
#     pattern_rows, pattern_cols = pattern.shape

#     for row in range(img_rows-pattern_rows):

#         for col in range(img_cols-pattern_cols):

#             res = np.array_equal(img[row:row+pattern_rows, col:col+pattern_cols], pattern)

#             if res == True:
#                 return [row, col]

#     return None

# screen = np.load("tab_screen.npy")

# screen = np.where(screen >= 60, 0, 255)

# plt.matshow(screen[234:699, 380:1538], cmap='gray')

# plt.show()

# width: starts at col 380, ends at col 1538 => width = 1158
# height: starts at row 234, ends at row 699 => height = 465
# ==> sword box appears after 26 rows and 570 cols
# ==> from the sword box we have to remove 26 rows, 570 cols and arrive to +1158 cols and +465 rows
# sword = screen[260:280, 950:970]





# print(check_tab_position(screen, sword))

# plt.matshow(screen2, cmap='gray')

# plt.show()
# def callback(hwnd, extra):
#     rect = win32gui.GetWindowRect(hwnd)
#     # x = rect[0]
#     # y = rect[1]
#     # w = rect[2] - x
#     # h = rect[3] - y

#     if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == "League of Legends (TM) Client":


#         print("Window %s:" % win32gui.GetWindowText(hwnd), rect)
#         # print(win32gui.GetDC(hwnd))
#     # print("\tLocation: (%d, %d)" % (x, y))
#     # print("\t    Size: (%d, %d)" % (w, h))

# def test():
#     win32gui.EnumWindows(callback, None)
#     #print(response)


# Ahri = LoLChampions('Jax')
# # Ahri.item_upgrade('Abyssal Mask')

# Ahri.level_up(18)

# print(Ahri.items)
# print(Ahri.stats)

