import random, time
from colorama import init, Fore, Back, Style

BASE_COLORAMA_CONFIG = Back.BLACK + Fore.GREEN

COUNTER_LIMIT = 15
LINE_GEN_CHANCE = 0
LINE_GEN_CHANCE_INCREASE = 0.01
LINE_GEN_CHANCE_MAX = 0.2
LINE_MAX_SIZE = 20

MATRIX_MAX_WIDTH = 80

SLEEP_TIME = 0.075
SLEEP_TIME_DECREASE = 0.01

class Line():
    def __init__(self, l = []):
        self.l = l
        self.generate_color_def()
    
    def is_empty(self):
        return (not self.l)

    def shuffle(self):
        random.shuffle(self.l)

    def generate_list(self):
        size = random.randint(0, LINE_MAX_SIZE)
        zero_count = random.randint(0, size)
        one_count = size - zero_count
        self.l = ([0] * zero_count) + ([1] * one_count)
        self.shuffle()
        self.generate_color_def()

    def generate_color_def(self):
        rand = random.random()
        if rand <= 0.7:
            self.color_def = BASE_COLORAMA_CONFIG + Style.DIM
        elif 0.7 < rand <= 0.85:
            self.color_def = BASE_COLORAMA_CONFIG + Style.NORMAL
        else:
            self.color_def = BASE_COLORAMA_CONFIG + Style.BRIGHT

    def pop(self):
        return self.l.pop()

def matrix():
    matrix = init_matrix()
    counter = 0
    line_gen = LINE_GEN_CHANCE
    timer = SLEEP_TIME

    while(True):
        update_matrix(matrix, line_gen) # generate new content
        print_line(matrix) # print single matrix line
        print("") # wait and print new line
        time.sleep(timer)

        if counter >= COUNTER_LIMIT and line_gen < LINE_GEN_CHANCE_MAX:
            # timer -= SLEEP_TIME_DECREASE
            line_gen += LINE_GEN_CHANCE_INCREASE
            counter = 0
        counter += 1

def init_matrix():
    matrix = []
    for i in range(MATRIX_MAX_WIDTH):
        matrix.append(Line())
    return matrix

def update_matrix(matrix, line_gen):
    for i, obj in enumerate(matrix):
        if obj.is_empty() and random.random() <= line_gen:
            matrix[i].generate_list()

def print_line(matrix):
    for obj in matrix:
        if obj.is_empty():
            print(obj.color_def + "%2s" % " ", end="")
        else:
            print(("{0} {1: <1}").format(obj.color_def, obj.pop()), end="")
        print(Style.RESET_ALL, end="")

if __name__ == "__main__":
    init() # colorama lib init func
    matrix()
    print("oi")