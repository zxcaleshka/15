from tkinter import Canvas, Tk
from random import shuffle

# Размеры поля
BOARD_SIZE = 3
SQUARE_SIZE = 80
EMPTY_SQUARE = BOARD_SIZE ** 2

# Создаем окно
root = Tk()
root.title("Пятнашки")

c = Canvas(root, width=BOARD_SIZE * SQUARE_SIZE,
           height=BOARD_SIZE * SQUARE_SIZE, bg='#808080')
c.pack()

def draw_board():
    c.delete('all')
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            index = str(board[BOARD_SIZE * i + j]) # Значение в клетке
            if index != str(EMPTY_SQUARE): # Если клетка не пустая
                c.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE, # Здесь рисуем квадрат
                                   j * SQUARE_SIZE + SQUARE_SIZE,
                                   i * SQUARE_SIZE + SQUARE_SIZE,
                                   fill='#FFFFFF',
                                   outline='#000000')
                c.create_text(j * SQUARE_SIZE + SQUARE_SIZE / 2, # Пишем число
                              i * SQUARE_SIZE + SQUARE_SIZE / 2,
                              text=index,
                              font="Arial {} italic".format(int(SQUARE_SIZE / 4)),
                              fill='#000000')

def get_empty_neighbor(index): # Узнать индекс пустой клетки
    empty_index = board.index(EMPTY_SQUARE)
    abs_value = abs(empty_index - index) # Расстояние от пустой до выбранной
    if abs_value == BOARD_SIZE: # Если рядом пустая рядом возвращается индекс пустой
        return empty_index
    elif abs_value == 1: # Если в одном ряду
        max_index = max(index, empty_index)
        if max_index % BOARD_SIZE != 0:
            return empty_index
    return index # Рядом нет пустого поля


def click(event):
    x, y = event.x, event.y # Координаты точки куда нажал пользователь
    x = x // SQUARE_SIZE
    y = y // SQUARE_SIZE
    board_index = x + (y * BOARD_SIZE) # Так узнаем значение в этой клетке
    empty_index = get_empty_neighbor(board_index)
    board[board_index], board[empty_index] = board[empty_index], board[board_index] # Меняем местами пустую и куда нажали
    draw_board() # Все стираем и рисуем с новыми данными

c.bind('<Button-1>', click)
c.pack()

# Создаем поле
board = list(range(1, EMPTY_SQUARE + 1))
shuffle(board)
draw_board()
root.mainloop()
<<<<<<< HEAD
