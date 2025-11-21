import tkinter
from tkinter import Tk
from tkinter import Canvas
import time
import random
snake = [[0, 0]]
eat = []
reverse = []
reverse3 = []
blocks = []
eat3 = []
blocks3 = []
material = 'eat'
def tap2(event):
    global material
    global eat
    global blocks
    global c1
    global eat3
    global blocks3
    x = (event.x-(event.x%20))
    y = (event.y-(event.y%20))
    if material == 'eat':
        eat.append([[x, y], None])
        eat3.append(c1.create_rectangle(x, y, x+20, y+20, fill='green'))
    elif material == 'block':
        blocks.append([x, y, None])
        blocks3.append(c1.create_rectangle(x, y, x+20, y+20, fill='red'))
def tap(event):
    global material
    global eat
    global blocks
    global c1
    global eat3
    global blocks3
    x = (event.x-(event.x%20))
    y = (event.y-(event.y%20))
    if material == 'eat':
        if not [[x, y], None] in eat:
            eat.append([[x, y], None])
            eat3.append(c1.create_rectangle(x, y, x+20, y+20, fill='green'))
        else:
            c1.delete(eat3[eat.index([[x, y], None])])
            eat3.remove(eat3[eat.index([[x, y], None])])
            eat.remove([[x, y], None])
    elif material == 'block':
        if not [x, y, None] in blocks:
            blocks.append([x, y, None])
            blocks3.append(c1.create_rectangle(x, y, x+20, y+20, fill='red'))
        else:
            c1.delete(blocks3[blocks.index([x, y, None])])
            blocks3.remove(blocks3[blocks.index([x, y, None])])
            blocks.remove([x, y, None])
    elif material == 'reverse':
        if not [x, y, None] in reverse:
            reverse.append([x, y, None])
            reverse3.append(c1.create_rectangle(x, y, x+20, y+20, fill='black', outline='blue'))
        else:
            c1.delete(reverse3[reverse.index([x, y, None])])
            reverse3.remove(reverse3[reverse.index([x, y, None])])
            reverse.remove([x, y, None])
def eat2(event):
    global material
    material = 'eat'
def block2(event):
    global material
    material = 'block'
def reverse2(event):
    global material
    material = 'reverse'

tk_build = Tk()
tk_build.title('Level editor')
tk_build.bind('<Button-1>', tap)
#stk_build.bind('<Motion>', tap2)
tk_build.bind('<Key-1>', eat2)
tk_build.bind('<Key-2>', block2)
tk_build.bind('<Key-3>', reverse2)
c1 = Canvas(tk_build, width=800, height=600)
c1['background'] = 'black'
c1.grid(column=0, row=0)
tk_build.mainloop()
color = 'blue'
direction = 'right2'
colorized = False
pause = False
commenttext = None
doublespeed = False
commenttext2 = None
def tick():
    global snake3
    global direction
    global eat
    global eat2
    global count
    global color
    global colorized
    global pause
    global commenttext
    global doublespeed
    global commenttext2
    c1.delete(commenttext)
    c1.delete(commenttext2)
    if not pause:
        snake2 = snake
        if direction == 'right':
            snake.insert(0, [(snake[0][0])+20, snake[0][1]])
        elif direction == 'left':
            snake.insert(0, [(snake[0][0])-20, snake[0][1]])
        elif direction == 'down':
            snake.insert(0, [(snake[0][0]), snake[0][1]+20])
        elif direction == 'up':
            snake.insert(0, [(snake[0][0]), snake[0][1]-20])
        else:
            snake.insert(0, [snake[0][0], snake[0][1]])
        snake.pop(len(snake)-1)
        ##if snake[0] == block1 or snake[0] == block2:
        ##    exit()
        for i in blocks:
            if snake[0] == [i[0], i[1]]:
                exit()
        ind = 0
        for i in eat:
            if snake[0] == i[0]:
                r = random.randrange(0, 800, 20)
                r2 = random.randrange(0, 600, 20)
                for i in blocks:
                    block1 = [i[0], i[1]]
                    if not [r, r2] == block1:
                        eat[ind][0] = [r, r2]
                    else:
                        r += 20
                        r2 += 20
                        eat[ind][0] = [r, r2]
                if len(blocks) == 0:
                    eat[ind][0] = [r, r2]
                snake.append(snake[len(snake2)-1])
                c1.delete(eat[ind][1])
                eat[ind][1] = c1.create_rectangle(eat[ind][0][0], eat[ind][0][1], eat[ind][0][0] + 20, eat[ind][0][1] + 20, fill='green')
            ind += 1
        for i in reverse:
            i2 = [i[0], i[1]]
            if snake[0] == i2:
                r = random.randrange(0, 800, 20)
                r2 = random.randrange(0, 600, 20)
                for i in blocks:
                    block1 = [i[0], i[1]]
                    if not [r, r2] == block1:
                        reverse[ind] = [r, r2, None]
                    else:
                        r += 20
                        r2 += 20
                        reverse[ind][0] = [r, r2, None]
                if len(blocks) == 0:
                    reverse[ind][0] = [r, r2, None]
                snake.append(snake[len(snake2)-1])
                c1.delete(reverse[ind][1])
                reverse[ind][2] = c1.create_rectangle(reverse[ind][0], reverse[ind][1], reverse[ind][0] + 20, reverse[ind][1] + 20, fill='black', outline='blue')
            ind += 1
        for i in snake3:
            c1.delete(i)
        snake3 = []
        if colorized:
            color = 'yellow'
        for i in snake:
            if color == 'blue' and colorized:
                color = 'yellow'
            else:
                color = 'blue'
            snake3.append(c1.create_rectangle(i[0], i[1], i[0]+20, i[1]+20, fill=color))
        c1.delete(count)
        count = c1.create_text(35, 20, text=len(snake), fill='white', font=('Courier New', 20))
        tk1.update()
        c1.update()
        for i in snake[1:len(snake)]:
            if i == snake[0] and len(snake)>2:
                exit()
        if snake[0][0] < 0:
            snake[0][0] = 800
        elif snake[0][0] > 780:
            snake[0][0] = 0
        elif snake[0][1] < 0:
            snake[0][1] = 600
        elif snake[0][1] > 580:
            snake[0][1] = 0
    else:
        commenttext = c1.create_text(150, 580, text='Game paused. Tap <p> to start.', fill='white', font=('Courier New', 10))
    if doublespeed:
        commenttext2 = c1.create_text(450, 580, text='2x speed. Tap <e> to normal speed', fill='white', font=('Courier New', 10))
    tk1.update()
    c1.update()
def up(event):
    global direction
    if not direction == 'down':
        direction = 'up'
def left(event):
    global direction
    if not direction == 'right':
        direction = 'left'
def down(event):
    global direction
    if not direction == 'up':
        direction = 'down'
def right(event):
    global direction
    if not direction == 'left':
        direction = 'right'
def pause2(event):
    global pause
    if pause:
        pause = False
    else:
        pause = True
def doublespeed2(event):
    global doublespeed
    if doublespeed:
        doublespeed = False
    else:
        doublespeed = True
tk1 = Tk()
tk1.title('Snake stargame')
c1 = Canvas(tk1, width=800, height=600)
c1.grid(column=0, row=0)
c1['background'] = 'black'
tk1.bind('<Key-w>', up)
tk1.bind('<Key-a>', left)
tk1.bind('<Key-s>', down)
tk1.bind('<Key-d>', right)
tk1.bind('<Key-p>', pause2)
tk1.bind('<Key-e>', doublespeed2)
commenttext = c1.create_text(50, 500, text='', fill='white', font=('Courier New', 10))
commenttext2 = c1.create_text(300, 500, text='', fill='white', font=('Courier New', 10))
count = c1.create_text(35, 20, text='1', fill='white', font=('Courier New', 20))
ind = 0
for i in blocks:
    blocks[ind][2] = c1.create_rectangle(i[0], i[1], i[0]+20, i[1]+20, fill='red')
    ind += 1
ind = 0
for i in eat:
    eat[ind][1] = c1.create_rectangle(eat[ind][0][0], eat[ind][0][1], eat[ind][0][0]+20, eat[ind][0][1]+20, fill='green')
    ind += 1
ind = 0
for i in reverse:
    reverse[ind][2] = c1.create_rectangle(reverse[ind][0], reverse[ind][1], reverse[ind][0]+20, reverse[ind][1]+20, fill='black', outline='blue')
    ind += 1
snake3 = [c1.create_rectangle(snake[0][0], snake[0][1], snake[0][0]+20, snake[0][1]+20, fill='blue')]
true = True
while true:
    tick()
    if not doublespeed:
        time.sleep(0.1)
    else:
        time.sleep(0.05)
    #print(reversed)
tk1.mainloop()
