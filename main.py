# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphics import *


def get_light_digraphs_list():
    digraphs_list = []

    with open("light_digraphs.txt", "r") as light_digraphs:
        for line in light_digraphs:
            for i in line.split(','):
                digraphs_list.append(i)

    return digraphs_list


def get_dark_digraphs_list():
    digraphs_list = []

    with open("dark_digraphs.txt", "r") as dark_digraphs:
        for line in dark_digraphs:
            for i in line.split(','):
                digraphs_list.append(i)
    return digraphs_list


def get_pixels(pixel_digraph_list):
    letter_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                   'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                   'X': 24, 'Y': 25, 'Z': 26}
    letters = []
    numbers = []
    pixels = []
    for i in pixel_digraph_list:
        letters.append(i[0])
        numbers.append(i[1:])

    for j in range(0, len(letters)):
        pixels.append(Rectangle(Point((letter_dict.get(letters[j].upper()) - 1), eval(numbers[j]) - 1),
                                Point(letter_dict.get(letters[j].upper()), eval(numbers[j]))))

    return pixels


def draw_qr_code():
    win = GraphWin('Floor', 500, 500)
    pixels_to_draw = get_pixels(get_light_digraphs_list())
    win.setCoords(0.0, 0.0, 21.0, 21.0)
    win.setBackground("white")

    for i in pixels_to_draw:
        i.draw(win)
        i.setFill("black")

    win.getMouse()
    win.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    draw_qr_code()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
