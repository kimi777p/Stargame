import tkinter
from tkinter import Tk
from tkinter import Canvas
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Button

level1 = [[[0, 0]], [[0, 20], [20, 20], [40, 20], [60, 20], [80, 20], [100, 20], [120, 20], [140, 20], [160, 20], [180, 20], [220, 0], [220, 20], [220, 40], [220, 60], [200, 60], [180, 60], [160, 60], [140, 60], [120, 60], [100, 60], [80, 60], [80, 60], [60, 60], [40, 60], [20, 60], [0, 100], [20, 100], [40, 100], [60, 100], [80, 100], [100, 100], [120, 100], [140, 100], [160, 100], [180, 100], [200, 100], [220, 100], [240, 100], [260, 100], [260, 80], [260, 60], [260, 40], [260, 20]], [[400, 400]]]
level2 = [[[0, 0]], [[20, 0], [20, 20], [20, 40], [20, 60], [20, 80], [20, 100], [40, 140], [60, 140], [60, 120], [60, 100], [60, 80], [60, 60], [60, 40], [60, 20], [100, 20], [100, 40], [100, 60], [100, 80], [100, 100], [100, 120], [100, 140], [100, 160], [100, 180], [80, 180], [60, 180], [20, 220], [40, 220], [60, 220], [80, 220], [20, 140], [20, 160], [20, 180], [20, 200]], [[400, 400]]]
level3 = [[[0, 0]], [[20, 20], [40, 20], [20, 40], [20, 60], [60, 20], [80, 20], [100, 20], [60, 60], [80, 60], [100, 60], [120, 20], [120, 60], [60, 80], [20, 80], [160, 20], [160, 40], [160, 60], [160, 100], [120, 100], [140, 100], [100, 100], [100, 120], [200, 100], [180, 100], [220, 100], [220, 120], [200, 60], [220, 60], [240, 60], [260, 60], [260, 80], [200, 20], [220, 20], [240, 20], [280, 20], [300, 20], [300, 60], [300, 40], [200, 0], [120, 0], [340, 0], [340, 20], [340, 40], [340, 60], [340, 100], [340, 80], [320, 100], [300, 100], [260, 120], [260, 140], [280, 140], [320, 140], [300, 140], [360, 140], [340, 140], [380, 140], [400, 140], [420, 140], [420, 120], [420, 100], [360, 100], [380, 100], [420, 80], [420, 60], [400, 60], [380, 60], [360, 20], [380, 20], [400, 20], [420, 20], [440, 20], [460, 20], [440, 100], [460, 100], [480, 100], [500, 60], [500, 80], [460, 40], [460, 60], [500, 100], [500, 120], [500, 140], [460, 140], [460, 160], [460, 180], [480, 180], [500, 180], [540, 180], [520, 180], [540, 160], [540, 140], [540, 120], [540, 100], [540, 80], [540, 60], [540, 40], [540, 20], [520, 20], [480, 20], [500, 20], [420, 160], [420, 180], [420, 220], [460, 220], [480, 220], [500, 220], [540, 220], [560, 220], [580, 220], [500, 240], [500, 260], [520, 260], [540, 260], [560, 260], [580, 300], [540, 300], [560, 300], [500, 280], [500, 300], [500, 320], [500, 340], [540, 340], [520, 340], [560, 340], [560, 400], [560, 360], [560, 380], [560, 420], [560, 460], [560, 500], [560, 480], [540, 460], [520, 460], [520, 440], [520, 420], [520, 380], [520, 400], [500, 380], [480, 380], [460, 340], [480, 300], [460, 300], [440, 300], [420, 300], [420, 320], [420, 340], [420, 360], [400, 360], [380, 360], [360, 380], [440, 380], [440, 400], [440, 420], [420, 440], [400, 440], [380, 440], [360, 420], [480, 420], [460, 420], [500, 460], [480, 460], [440, 460], [440, 480], [440, 500], [460, 500], [500, 500], [520, 500], [480, 500], [560, 520], [560, 540], [540, 540], [500, 540], [480, 540], [520, 540], [460, 540], [420, 540], [420, 560], [420, 580], [460, 560], [500, 580], [540, 560], [580, 580], [560, 180], [580, 140], [560, 100], [580, 60], [560, 20], [140, 140], [180, 140], [160, 140], [180, 160], [140, 160], [180, 180], [140, 180], [100, 160], [100, 180], [100, 200], [100, 220], [120, 220], [140, 220], [180, 220], [200, 220], [220, 220], [220, 200], [220, 180], [220, 160], [340, 380], [320, 380], [340, 420], [320, 420], [300, 380], [300, 420], [260, 380], [260, 400], [260, 420], [260, 440], [260, 460], [280, 460], [300, 460], [320, 460], [340, 460], [340, 480], [360, 480], [380, 480], [400, 480], [400, 500], [380, 520], [380, 540], [380, 560], [360, 560], [340, 560], [340, 540], [340, 520], [300, 500], [300, 540], [300, 560], [260, 360], [260, 340], [280, 340], [320, 340], [340, 340], [300, 340], [360, 320], [380, 320], [380, 300], [380, 280], [380, 260], [400, 260], [420, 260], [440, 260], [460, 260], [480, 260], [400, 220], [380, 220], [380, 200], [380, 180], [360, 180], [340, 180], [300, 180], [280, 180], [260, 180], [260, 200], [260, 220], [300, 220], [320, 220], [340, 220], [320, 260], [320, 280], [340, 320], [340, 260], [360, 300], [300, 300], [260, 320], [260, 300], [260, 280], [300, 260], [260, 260], [60, 120], [60, 140], [40, 140], [20, 140], [0, 140], [20, 100], [80, 180], [60, 180], [20, 160], [20, 180], [20, 200], [20, 220], [40, 220], [60, 220], [60, 240], [60, 280], [60, 300], [40, 300], [20, 300], [20, 260], [0, 260], [20, 320], [20, 360], [0, 360], [60, 360], [60, 340], [80, 300], [100, 300], [100, 320], [120, 360], [100, 360], [60, 380], [60, 400], [40, 400], [20, 400], [0, 440], [40, 440], [80, 440], [60, 440], [80, 400], [100, 400], [60, 420], [120, 440], [140, 440], [140, 380], [140, 400], [140, 420], [140, 360], [60, 460], [140, 460], [120, 480], [100, 480], [60, 500], [20, 480], [0, 480], [60, 520], [40, 520], [20, 520], [20, 540], [0, 580], [20, 580], [60, 580], [60, 560], [60, 540], [40, 580], [80, 520], [100, 520], [100, 540], [80, 580], [100, 580], [120, 580], [140, 580], [140, 560], [140, 520], [140, 500], [140, 480], [160, 520], [180, 520], [180, 540], [180, 560], [220, 560], [220, 540], [220, 520], [220, 500], [220, 480], [200, 480], [180, 480], [180, 440], [180, 460], [160, 400], [180, 400], [200, 400], [200, 440], [220, 440], [240, 440], [220, 400], [240, 360], [220, 360], [180, 360], [200, 360], [140, 340], [140, 320], [160, 320], [200, 320], [180, 320], [220, 320], [220, 300], [220, 280], [220, 260], [180, 260], [180, 280], [160, 280], [140, 280], [140, 260], [120, 260], [100, 260], [260, 500], [260, 520], [280, 500], [260, 540], [260, 560], [260, 580]], [[400, 400]]]
level = level1
position = level[0][0]
blocks = level1[1]
win = level1[2]
player = None
color1 = 'blue'
color2 = 'red'
color3 = 'green'
def wincheck():
    if position == level[2][0]:
        messagebox.showinfo('Stargame', 'You win!')
        exit()
def rightmovement(event):
    global level
    global position
    global player
    global color1
    global color2
    global color3
    global tk1
    global c1
    global blocks
    a = True
    for i in blocks:
        if [position[0]+20, position[1]] == i:
            a = False
    if position[0] == 580:
        a = False
    if a:
        c1.delete(player)
        position = [position[0]+20, position[1]]
        player = c1.create_rectangle(position[0], position[1], position[0] + 20, position[1] + 20, fill=color1)
        tk1.update()
        c1.update()
    wincheck()
def leftmovement(event):
    global level
    global position
    global player
    global color1
    global color2
    global color3
    global tk1
    global c1
    global blocks
    a = True
    for i in blocks:
        if [position[0]-20, position[1]] == i:
            a = False
    if position[0] == 0:
        a = False
    if a:
        c1.delete(player)
        position = [position[0]-20, position[1]]
        player = c1.create_rectangle(position[0], position[1], position[0] + 20, position[1] + 20, fill=color1)
        tk1.update()
        c1.update()
    wincheck()
def upmovement(event):
    global level
    global position
    global player
    global color1
    global color2
    global color3
    global tk1
    global c1
    global blocks
    a = True
    for i in blocks:
        if [position[0], position[1]-20] == i:
            a = False
    if position[1] == 0:
        a = False
    if a:
        c1.delete(player)
        position = [position[0], position[1]-20]
        player = c1.create_rectangle(position[0], position[1], position[0] + 20, position[1] + 20, fill=color1)
        tk1.update()
        c1.update()
    wincheck()
def downmovement(event):
    global level
    global position
    global player
    global color1
    global color2
    global color3
    global tk1
    global c1
    global blocks
    a = True
    for i in blocks:
        if [position[0], position[1]+20] == i:
            a = False
    if position[1] > 560:
        a = False
    if a:
        c1.delete(player)
        position = [position[0], position[1]+20]
        player = c1.create_rectangle(position[0], position[1], position[0] + 20, position[1] + 20, fill=color1)
        tk1.update()
        c1.update()
    wincheck()
def level_1():
    global level
    global level1
    global position
    global tk_level
    global blocks
    global win
    level = level1
    position = level[0][0]
    blocks = level[1]
    win = level[2]
    tk_level.destroy()
def level_2():
    global level
    global level2
    global position
    global tk_level
    global blocks
    global win
    level = level2
    position = level[0][0]
    blocks = level[1]
    win = level[2]
    tk_level.destroy()
def level_3():
    global level
    global level3
    global position
    global tk_level
    global blocks
    global win
    level = level3
    position = level[0][0]
    blocks = level[1]
    win = level[2]
    tk_level.destroy()
def level_editor():
    material = 'block'
    global tk_level
    global level
    global position
    global blocks
    global win
    global color1
    global color2
    global color3
    win2 = None
    blocks2 = []
    player2 = None
    tk_level.destroy()
    position = [0, 0]
    level = [[[0, 0]], [], [[400, 400]]]
    blocks = []
    def block_comm(event):
        global material
        material = 'block'
    def player_comm(event):
        global material
        material = 'player'
    def win_comm(event):
        global material
        material = 'win'
    def tap2(event):
        #global material
        #global tk_level_editor
        #global c_level_editor
        #global wins2
        #global blocks2
        #global player2
        #global position
        #global level
        #global color1
        #global color2
        #global color3
        positionx = (event.x-((event.x)%20))
        positiony = (event.y-((event.y)%20))
        if material == 'block':
            if not [positionx, positiony] in blocks:
                blocks2.append(c_level_editor.create_rectangle(positionx, positiony, positionx+20, positiony+20, fill=color2))
                blocks.append([positionx, positiony])
        if material == 'win':
            c_level_editor.delete(win2)
            win2 = c_level_editor.create_rectangle(positionx, positiony, positionx+20, positiony+20, fill=color3)
            level[3] = [[positionx, positiony]]
        if material == 'player':
            c_level_editor.delete(player2)
            player2 = c_level_editor.create_rectangle(positionx, positiony, positionx+20, positiony+20, fill=color1)
            position = [positionx, positiony]
    def tap(event):
        #global material
        #global tk_level_editor
        #global c_level_editor
        #global wins2
        #global blocks2
        #global player2
        #global position
        #global level
        #global color1
        #global color2
        #global color3
        positionx = (event.x-((event.x)%20))
        positiony = (event.y-((event.y)%20))
        if material == 'block':
            if not [positionx, positiony] in blocks:
                blocks2.append(c_level_editor.create_rectangle(positionx, positiony, positionx+20, positiony+20, fill=color2))
                blocks.append([positionx, positiony])
            else:
                a = blocks.index([positionx, positiony])
                c_level_editor.delete(blocks2[a])
                blocks2.remove(blocks2[a])
                blocks.remove(blocks[a])
        if material == 'win':
            c_level_editor.delete(win2)
            win2 = c_level_editor.create_rectangle(positionx, positiony, positionx+20, positiony+20, fill=color3)
            level[3] = [[positionx, positiony]]
        if material == 'player':
            c_level_editor.delete(player2)
            player2 = c_level_editor.create_rectangle(positionx, positiony, positionx+20, positiony+20, fill=color1)
            position = [positionx, positiony]
    tk_level_editor = Tk()
    tk_level_editor.title('Level editor')
    tk_level_editor.geometry('600x600')
    tk_level_editor.resizable(False, False)
    tk_level_editor.bind('<ButtonPress-1>', tap)
    #tk_level_editor.bind('<B1-Motion>', tap2)
    '''tk_level_editor.bind('<KeyPress-1>', block_comm)
    tk_level_editor.bind('<KeyPress-2>', player_comm)
    tk_level_editor.bind('<KeyPress-3>', win_comm)'''
    c_level_editor = Canvas(tk_level_editor, width=600, height=600)
    c_level_editor['background'] = 'black'
    c_level_editor.grid(column=0, row=0)
    win2 = c_level_editor.create_rectangle(400, 400, 420, 420, fill=color3)
    player2 = c_level_editor.create_rectangle(position[0], position[1], position[0]+20, position[1]+20, fill=color1)
    tk_level_editor.mainloop()
    print(level)
    print(blocks)

tk_level = Tk()
tk_level.title('Labirint stargame - choose level')
tk_level.geometry('600x600')
tk_level.resizable(False, False)
btn_level_editor = Button(tk_level, text='Level editor', command=level_editor)
btn_level_editor.grid(column=1, row=0)
btn1 = Button(tk_level, text='Level 1', command=level_1)
btn1.grid(column=0, row=0)
btn2 = Button(tk_level, text='Level 2', command=level_2)
btn2.grid(column=0, row=1)
btn3 = Button(tk_level, text='Level 3', command=level_3)
btn3.grid(column=0, row=2)
tk_level.mainloop()
tk1 = Tk()
tk1.title('Labirint stargame')
tk1.geometry('600x600')
tk1.resizable(False, False)
tk1.bind('<Key-Right>', rightmovement)
tk1.bind('<Key-d>', rightmovement)
tk1.bind('<Key-Left>', leftmovement)
tk1.bind('<Key-a>', leftmovement)
tk1.bind('<Key-Up>', upmovement)
tk1.bind('<Key-w>', upmovement)
tk1.bind('<Key-Down>', downmovement)
tk1.bind('<Key-s>', downmovement)
c1 = Canvas(tk1, width=600, height=600)
c1['background'] = 'black'
c1.grid(column=0, row=0)
player = c1.create_rectangle(position[0], position[1], position[0]+20, position[1]+20, fill=color1)
for i in blocks:
    c1.create_rectangle(i[0], i[1], i[0]+20, i[1]+20, fill=color2)
for i in win:
    c1.create_rectangle(i[0], i[1], i[0]+20, i[1]+20, fill=color3)
tk1.mainloop()
