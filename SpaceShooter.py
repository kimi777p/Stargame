import tkinter
from tkinter import *
from tkinter.ttk import Button
import time
import random

class personage():
    def __init__(self, canvas):
        self.x = 0
        self.y = 0
        self.direction = 'right'
        self.shape = []
        self.canvas = canvas
        self.shape.append(self.canvas.create_rectangle(self.x+4, self.y+5, self.x+20, self.y+15, fill='blue', outline='grey', width=1))
        self.shape.append(self.canvas.create_rectangle(self.x, self.y, self.x+10, self.y+4, fill='blue', outline='grey', width=1))
        self.shape.append(self.canvas.create_rectangle(self.x, self.y+16, self.x+10, self.y+20, fill='blue', outline='grey', width=1))
    def move(self, direction):
        for i in self.shape:
            self.canvas.delete(i)
        if direction == 'right':
            self.direction = 'right'
            self.x += 20
        elif direction == 'left':
            self.direction = 'left'
            self.x -= 20
        elif direction == 'up':
            self.direction = 'up'
            self.y -= 20
        elif direction == 'down':
            self.direction = 'down'
            self.y += 20
        if self.direction == 'right':
            self.shape.append(self.canvas.create_rectangle(self.x+4, self.y+5, self.x+20, self.y+15, fill='blue', outline='grey', width=1))
            self.shape.append(self.canvas.create_rectangle(self.x, self.y, self.x+10, self.y+4, fill='blue', outline='grey', width=1))
            self.shape.append(self.canvas.create_rectangle(self.x, self.y+16, self.x+10, self.y+20, fill='blue', outline='grey', width=1))
        if self.direction == 'left':
            self.shape.append(self.canvas.create_rectangle(self.x+20-4, self.y+5, self.x+20-20, self.y+15, fill='blue', outline='grey', width=1))
            self.shape.append(self.canvas.create_rectangle(self.x+20, self.y, self.x+20-10, self.y+4, fill='blue', outline='grey', width=1))
            self.shape.append(self.canvas.create_rectangle(self.x+20, self.y+16, self.x+20-10, self.y+20, fill='blue', outline='grey', width=1))
        if self.direction == 'down':
            self.shape.append(self.canvas.create_rectangle(self.x+5, self.y+4, self.x+15, self.y+20, fill='blue', outline='grey', width=1))
            self.shape.append(self.canvas.create_rectangle(self.x, self.y, self.x+4, self.y+10, fill='blue', outline='grey', width=1))
            self.shape.append(self.canvas.create_rectangle(self.x+16, self.y, self.x+20, self.y+10, fill='blue', outline='grey', width=1))
        if self.direction == 'up':
            self.shape.append(self.canvas.create_rectangle(self.x+5, self.y+20-4, self.x+15, self.y, fill='blue', outline='grey', width=1))
            self.shape.append(self.canvas.create_rectangle(self.x, self.y+20, self.x+4, self.y+20-10, fill='blue', outline='grey', width=1))
            self.shape.append(self.canvas.create_rectangle(self.x+16, self.y+20, self.x+20, self.y+20-10, fill='blue', outline='grey', width=1))
class UFO():
    def __init__(self, canvas, ufos, playerx, playery, window):
        def set_random_positions(ufos):
            x = random.randint(1, xsize//20)*20
            y = random.randint(1, ysize//20)*20
            if ([x, y] in ufos) or ((x == playerx) and (y == playery)):
                return set_random_positions(ufos)
            else:
                return [x, y]
        self.ufos = ufos
        self.position = set_random_positions(self.ufos)
        self.shape = []
        self.shape.append(canvas.create_oval(self.position[0]+5, self.position[1], self.position[0]+15, self.position[1]+15, fill='cyan', width=0))
        self.shape.append(canvas.create_oval(self.position[0]+2, self.position[1]+10, self.position[0]+18, self.position[1]+20, fill='grey', width=0))
        self.canvas = canvas
        self.window = window
    def delete(self):
        for i in self.shape:
            self.canvas.delete(i)
        circle1 = self.canvas.create_oval(self.position[0]+5, self.position[1]+5, self.position[0]+15, self.position[1]+15, fill='black', outline='orange', width=1)
        self.window.update()
        time.sleep(0.1)
        self.canvas.delete(circle1)
        circle2 = self.canvas.create_oval(self.position[0]+4, self.position[1]+4, self.position[0]+16, self.position[1]+16, fill='black', outline='orange', width=1)
        self.window.update()
        time.sleep(0.1)
        self.canvas.delete(circle2)
        circle3 = self.canvas.create_oval(self.position[0]+3, self.position[1]+3, self.position[0]+17, self.position[1]+17, fill='black', outline='orange', width=1)
        self.window.update()
        time.sleep(0.1)
        self.canvas.delete(circle3)
        circle4 = self.canvas.create_oval(self.position[0]+2, self.position[1]+2, self.position[0]+18, self.position[1]+18, fill='black', outline='orange', width=1)
        self.window.update()
        time.sleep(0.1)
        self.canvas.delete(circle4)
        circle5 = self.canvas.create_oval(self.position[0]+1, self.position[1]+1, self.position[0]+19, self.position[1]+19, fill='black', outline='orange', width=1)
        self.window.update()
        time.sleep(0.1)
        self.canvas.delete(circle5)
        circle6 = self.canvas.create_oval(self.position[0], self.position[1], self.position[0]+20, self.position[1]+20, fill='black', outline='orange', width=1)
        self.window.update()
        time.sleep(0.1)
        self.canvas.delete(circle6)
        self.window.update()
class bomb():
    def __init__(self, canvas, direction, x, y, ufos):
        self.canvas = canvas
        self.direction = direction
        self.x = x
        self.y = y
        self.shape = []
        if self.direction == 'right' or self.direction == 'left':
            self.shape.append(self.canvas.create_rectangle(self.x, self.y+8, self.x+20, self.y+12, fill='red', width=0))
        else:
            self.shape.append(self.canvas.create_rectangle(self.x+8, self.y, self.x+12, self.y+20, fill='red', width=0))
        self.ufos = ufos
    def tick(self, ufos, ufos_positions):
        for i in self.shape:
            self.canvas.delete(i)
        if self.direction == 'right':
            self.x += 20
        elif self.direction == 'left':
            self.x -= 20
        elif self.direction == 'up':
            self.y -= 20
        elif self.direction == 'down':
            self.y += 20
        self.shape = []
        if self.direction == 'right' or self.direction == 'left':
            self.shape.append(self.canvas.create_rectangle(self.x, self.y+8, self.x+20, self.y+12, fill='red', width=0))
        if self.direction == 'up' or self.direction == 'down':
            self.shape.append(self.canvas.create_rectangle(self.x+8, self.y, self.x+12, self.y+20, fill='red', width=0))
        for i in ufos:
            if i.position[0] == self.x and i.position[1] == self.y:
                i.delete()
                return [i, i.position]
        return False

def close(event):
    for i in [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]:
        tk1.wm_attributes('-alpha', i)
        time.sleep(0.05)
    tk1.destroy()
def click(event):
    global xsize
    global ysize
    x = event.x
    y = event.y
    if x > xsize/2-150 and x < xsize/2+150 and y > 120 and y < 160:
        for i in [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]:
            tk1.attributes('-alpha', i)
            time.sleep(0.05)
        tk1.destroy()
    elif x > xsize/2-150 and x < xsize/2+150 and y > 80 and y < 120:
        def close_settings_window(event):
            tk_settings.destroy()
        tk_settings = Tk()
        tk_settings.overrideredirect(True)
        tk_settings.wm_attributes('-topmost', True)
        tk_settings.attributes('-alpha', 0)
        tk_settings['background'] = 'black'
        tk_settings.geometry(str(xsize)+'x'+str(ysize)+'+0+0')
        tk_settings.bind('<Key-e>', close_settings_window)
        tk_settings.update()
        time.sleep(0.05)
        for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
            tk_settings.attributes('-alpha', i)
            time.sleep(0.05)
        lbl1 = Label(tk_settings, text='SETTINGS', font=('8514oem', 15), foreground='white', background='black')
        lbl1.grid(column=0, row=0, sticky='w')
    elif x > xsize/2-150 and x < xsize/2+150 and y > 40 and y < 80:
        def close_game_window(event):
            tk_game.destroy()
        def up(event):
            player.move('up')
        def down(event):
            player.move('down')
        def right(event):
            player.move('right')
        def left(event):
            player.move('left')
        def clicked(event):
            def shot(event):
                new_bomb = bomb(game_canvas, player.direction, player.x, player.y, ufos)
                bombs.append(new_bomb)
            game_canvas.delete(text)
            tk_game.unbind('<Button-1>')
            health = 10
            tk2 = Tk()
            tk2.overrideredirect(True)
            tk2.wm_attributes('-topmost', True)
            tk2.attributes('-alpha', 0)
            tk2['background'] = 'black'
            tk2.geometry(str(xsize)+'x50+0+'+str(ysize))
            tk2.update()
            time.sleep(0.05)
            for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
                tk2.attributes('-alpha', i)
                time.sleep(0.05)
            hp = Label(tk2, text='♥', foreground='red', background='black', font=('Fira Code', 25))
            hp.grid(column=0, row=0, sticky='w')
            tk2.update()
            time.sleep(0.1)
            for i in range(2, 11):
                hp['text'] = '♥'*i
                tk2.update()
                time.sleep(0.1)
                tk2.update()
            text2 = game_canvas.create_text(xsize/2, ysize/2, text='3', fill='red', font=('8514oem', 75))
            tk_game.update()
            time.sleep(1.5)
            game_canvas.delete(text2)
            text3 = game_canvas.create_text(xsize/2, ysize/2, text='2', fill='red', font=('8514oem', 75))
            tk_game.update()
            time.sleep(1.5)
            game_canvas.delete(text3)
            text4 = game_canvas.create_text(xsize/2, ysize/2, text='1', fill='red', font=('8514oem', 75))
            tk_game.update()
            time.sleep(1.5)
            game_canvas.delete(text4)
            text5 = game_canvas.create_text(xsize/2, ysize/2, text='GO!', fill='red', font=('8514oem', 75))
            tk_game.update()
            time.sleep(1.5)
            game_canvas.delete(text5)
            tk_game.update()
            tickid = 0
            ufos = []
            ufos_positions = []
            bombs = []
            tk_game.bind('<Key-q>', shot)
            while True:
                if tickid % 30 == 0:
                    ufos.append(UFO(game_canvas, ufos_positions, player.x, player.y, tk_game))
                    ufos_positions.append(ufos[-1].position)
                tickid += 1
                for i in bombs:
                    res = i.tick(ufos, ufos_positions)
                    if res:
                        ufos.remove(res[0])
                        ufos_positions.remove(res[1])
                tk_game.update()
                time.sleep(0.02)
                index = 0
                ufos_positions2 = [i for i in ufos_positions]
                ufos2 = [i for i in ufos]
                for i in ufos_positions:
                    if i[0] == player.x and i[1] == player.y:
                        ufos[index].delete()
                        ufos_positions2.pop(index)
                        ufos2.pop(index)
                        hp['text'] = (len(hp['text'])-1)*'♥'
                        health -= 1
                        if health == 0:
                            def close():
                                tk_gameover.destroy()
                            tk_game.destroy()
                            tk2.destroy()
                            tk_gameover = Tk()
                            tk_gameover.title('Game over!')
                            tk_gameover.wm_attributes('-topmost', True)
                            tk_gameover.lift()
                            lbl1 = Label(tk_gameover, text='Game over!')
                            lbl1.grid(column=0, row=0)
                            btn1 = Button(tk_gameover, text='Close', command=close)
                            btn1.grid(column=0, row=1, sticky='w')
                    index += 1
                ufos_positions = [i for i in ufos_positions2]
                ufos = [i for i in ufos2]
                if len(ufos) >= 50:
                    def close():
                        tk_gameover.destroy()
                    tk_game.destroy()
                    tk2.destroy()
                    tk_gameover = Tk()
                    tk_gameover.title('Game over!')
                    tk_gameover.wm_attributes('-topmost', True)
                    tk_gameover.lift()
                    lbl1 = Label(tk_gameover, text='Game over!')
                    lbl1.grid(column=0, row=0)
                    btn1 = Button(tk_gameover, text='Close', command=close)
                    btn1.grid(column=0, row=1, sticky='w')
        tk_game = Tk()
        tk_game.overrideredirect(True)
        tk_game.wm_attributes('-topmost', True)
        tk_game.attributes('-alpha', 0)
        tk_game['background'] = 'black'
        tk_game.geometry(str(xsize)+'x'+str(ysize)+'+0+0')
        tk_game.bind('<Key-e>', close_game_window)
        tk_game.lift()
        game_canvas = Canvas(tk_game, width=xsize, height=ysize)
        game_canvas['background'] = 'black'
        game_canvas.grid(column=0, row=0)
        tk_game.update()
        time.sleep(0.05)
        for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
            tk_game.attributes('-alpha', i)
            time.sleep(0.05)
        player = personage(game_canvas)
        tk_game.bind('<Key-w>', up)
        tk_game.bind('<Key-s>', down)
        tk_game.bind('<Key-d>', right)
        tk_game.bind('<Key-a>', left)
        text = game_canvas.create_text(xsize/2, ysize/2, text='click to start', fill='yellow', font=('8514oem', 25))
        tk_game.bind('<Button-1>', clicked)

xsize = 1000
ysize = 700

tk1 = Tk()
tk1.overrideredirect(True)
tk1.wm_attributes('-topmost', True)
tk1.attributes('-alpha', 0)
tk1['background'] = 'black'
tk1.geometry(str(xsize)+'x'+str(ysize)+'+0+0')
tk1.bind('<Key-e>', close)
c1 = Canvas(tk1, width=xsize, height=ysize)
c1['background'] = 'black'
c1.grid(column=0, row=0)
text1 = c1.create_text(xsize/2, ysize/2, text='STARGAME', fill='yellow', font=('8514oem', 85))
tk1.update()
time.sleep(0.05)
for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
    tk1.attributes('-alpha', i)
    time.sleep(0.05)
time.sleep(2)
c1.delete(text1)
text2 = c1.create_text(xsize/2, ysize/2, text='SPACE SHOOTER', fill='yellow', font=('8514oem', 85))
tk1.update()
time.sleep(2)
c1.delete(text2)
text3 = c1.create_text(xsize/2, 20, text='Main menu', fill='yellow', font=('8514oem', 25))
text4 = c1.create_text(xsize/2, 60, text='Play', fill='blue', font=('8514oem', 25))
text5 = c1.create_text(xsize/2, 100, text='Options', fill='blue', font=('8514oem', 25))
text6 = c1.create_text(xsize/2, 140, text='Exit', fill='red', font=('8514oem', 25))
tk1.bind('<Button-1>', click)
tk1.mainloop()
