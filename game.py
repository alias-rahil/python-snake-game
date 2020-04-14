from pynput import *
import os
import time
import threading
import random


def generateFood():
    if " " in snake:
        while True:
            food = random.choice(range(19 * 19))
            if food != head and food not in tail:
                break
    else:
        food = None
    return food


def display():
    if os.name == 'nt':
        os.system("clc")
    else:
        os.system("clear")
    print("""
    +++++++++++++++++++++
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}+
    +++++++++++++++++++++
    """.format(*snake))
    print(f"Score: {len(tail)}.")
    if badMove:
        print("Bad Move!")
    else:
        print("         ")
    return None


def start():
    global tail
    global snake
    global head
    global food
    global flag
    while True:
        if direction:
            if head in range(19) and direction == "up":
                display()
                print("Game over!")
                os._exit(0)
            elif head in range(342, 361) and direction == "down":
                display()
                print("Game over!")
                os._exit(0)
            elif head in range(0, 361, 19) and direction == "left":
                display()
                print("Game over!")
                os._exit(0)
            elif head in range(18, 379, 19) and direction == "right":
                display()
                print("Game over!")
                os._exit(0)
            elif direction == "up" and (head - 19) in tail:
                display()
                print("Game over!")
                os._exit(0)
            elif direction == "down" and (head + 19) in tail:
                display()
                print("Game over!")
                os._exit(0)
            elif direction == "right" and (head + 1) in tail:
                display()
                print("Game over!")
                os._exit(0)
            elif direction == "left" and (head - 1) in tail:
                display()
                print("Game over!")
                os._exit(0)
            else:
                for i in range(len(tail)):
                    if i == (len(tail) - 1):
                        tail[0] = head
                    else:
                        tail[len(tail) - 1 - i] = tail[len(tail) - 2 - i]
                if direction == "up":
                    head -= 19
                elif direction == "down":
                    head += 19
                elif direction == "right":
                    head += 1
                else:
                    head -= 1
                snake = [" " for i in range(19 * 19)]
                snake[head] = "X"
                for i in tail:
                    snake[i] = "-"
                if head == food:
                    tail.append(None)
                    food = generateFood()
                if food:
                    snake[food] = "O"
                display()
                flag = True
                time.sleep(0.1)
        else:
            display()
            time.sleep(0.1)
    return None


def main(key):
    global direction
    global badMove
    global flag
    if badMove:
        badMove = False
    key = str(key)
    if key == "Key.up" and direction != "down" and flag:
        direction = "up"
        flag = False
    elif key == "Key.down" and direction != "up" and flag:
        direction = "down"
        flag = False
    elif key == "Key.right" and direction != "left" and flag:
        direction = "right"
        flag = False
    elif key == "Key.left" and direction != "right" and flag:
        direction = "left"
        flag = False
    else:
        badMove = True
    return None


def listener():
    declarations()
    t = threading.Thread(target=start)
    t.start()
    updater = keyboard.Listener(on_press=main)
    updater.start()
    updater.join()
    return None


def declarations():
    global direction
    global badMove
    global flag
    global tail
    global snake
    global head
    global food
    direction = None
    head = 180
    tail = []
    snake = [" " for i in range(19 * 19)]
    snake[head] = "X"
    badMove = False
    flag = True
    for i in tail:
        snake[i] = "-"
    food = generateFood()
    snake[food] = "O"
    return None


listener()
