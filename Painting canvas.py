import tkinter
from tkinter import *
from tkinter import colorchooser
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Stargame')

dots = []

current_figure = 'dot'

print(' Star')
print('   game')
print('     2024')
print('----------------------')
print(' Painting canvas1.0.0')
print('\n'*2)

tk1 = Tk()
tk1.title('draw!')
tk1.iconbitmap('henicon.ico')

canvas1 = Canvas(tk1, width=1400, height=800, background='white')
canvas1.grid(column=0, row=0)

bgcolor = 'white'

tk_choose_file_1 = Tk()
tk_choose_file_1.title('Are you want to open image?')
tk_choose_file_1.iconbitmap('henicon.ico')
def open1():
    def OK():
        file = open(format(ent1.get()) + '.sti2', 'r').read()
        file = file.split('\n')
        tk_choose_file_2.destroy()
        canvas1['background'] = file[0]
        bgcolor = file[0]
        for i in file[1:len(file) - 1]:
            s = i.split(',')
            if s[0] == 'dot':
                px = int(s[1])
                py = int(s[2])
                color = s[3]
                size = int(s[4])
                canvas1.create_oval(px - size, py - size, px + size, py + size, fill=color, outline=color)
                dots.append(['dot', px, py, color, size])
            elif s[0] == 'square':
                px = int(s[1])
                py = int(s[2])
                color = s[3]
                size = int(s[4])
                canvas1.create_rectangle(px - size, py - size, px + size, py + size, fill=color, outline=color)
                dots.append(['square', px, py, color, size])
            elif s[0] == 'line':
                px = int(s[1])
                py = int(s[2])
                color = s[3]
                size = int(s[4])
                canvas1.create_line(px - s4, py - 4, px + 4, py + 4, fill=color, width=size)
                dots.append(['line', px, py, color, size])
    tk_choose_file_1.destroy()
    tk_choose_file_2 = Tk()
    tk_choose_file_2.title('Write the name of the file')
    tk_choose_file_2.iconbitmap('henicon.ico')
    ent1 = Entry(tk_choose_file_2, width=20)
    ent1.grid(column=0, row=0)
    btn1 = Button(tk_choose_file_2, text='OK', command=OK)
    btn1.grid(column=1, row=0)
def exit1():
    tk_choose_file_1.destroy()

btn1 = Button(tk_choose_file_1, text=' Yes ', command=open1)
btn1.grid(column=0, row=0)
btn2 = Button(tk_choose_file_1, text=' No ', command=exit1)
btn2.grid(column=1, row=0)
lbl1 = Label(tk_choose_file_1, text='                                                                                     ')
lbl1.grid(column=2, row=0)

size = 4
color = 'black'

def tap(event):
    global color
    global size
    global dots
    global current_figure
    if current_figure == 'dot':
        px = canvas1.winfo_pointerx()-8
        py = canvas1.winfo_pointery()-32
        px = event.x
        py = event.y
        canvas1.create_oval(px-size, py-size, px+size, py+size, fill=color, outline=color)
        print(event.x)
        print(event.y)
        print(color)
        print(size)
        dots.append(['dot', event.x, event.y, color, size])
    elif current_figure == 'square':
        px = canvas1.winfo_pointerx() - 8
        py = canvas1.winfo_pointery() - 32
        px = event.x
        py = event.y
        canvas1.create_rectangle(px - size, py - size, px + size, py + size, fill=color, outline=color)
        print(event.x)
        print(event.y)
        print(color)
        print(size)
        dots.append(['square', event.x, event.y, color, size])
    elif current_figure == 'line':
        px = canvas1.winfo_pointerx() - 8
        py = canvas1.winfo_pointery() - 32
        px = event.x
        py = event.y
        canvas1.create_line(px - 4, py - 4, px + 4, py + 4, fill=color, width=size)
        print(event.x)
        print(event.y)
        print(color)
        print(size)
        dots.append(['line', event.x, event.y, color, size])

def black(event):
    global color
    color = 'black'
    print('black')
def red(event):
    global color
    color = 'red'
    print('red')
def orange(event):
    global color
    color = 'orange'
    print('orange')
def yellow(event):
    global color
    color = 'yellow'
    print('yellow')
def green(event):
    global color
    color = 'green'
    print('green')
def blue(event):
    global color
    color = 'blue'
    print('blue')
def violet(event):
    global color
    color = 'violet'
    print('violet')
def white(event):
    global color
    color = 'white'
    print('white')
def choose_color(event):
    global color
    c = colorchooser.askcolor()[1]
    color = c
    print(c)
def up(event):
    global size
    size += 1
    print(size)
def down(event):
    global size
    if not size == 1:
        size -= 1
    print(size)
def eraser(event):
    global size
    global color
    size = 10
    color = 'white'
    print('eraser')
def pen(event):
    global size
    global color
    size = 4
    color = 'black'
    print('pen')
def marker(event):
    global size
    global color
    size = 10
    color = 'black'
    print('marker')
def settings(event):
    global bgcolor
    def white():
        global bgcolor
        canvas1['background'] = 'white'
        bgcolor = 'white'
        print('white')
    def black():
        global bgcolor
        canvas1['background'] = 'black'
        bgcolor = 'black'
        print('black')
    def blue():
        global bgcolor
        canvas1['background'] = 'blue'
        bgcolor = 'blue'
        print('blue')
    def yellow():
        global bgcolor
        canvas1['background'] = 'yellow'
        bgcolor = 'yellow'
        print('yellow')
    def red():
        global bgcolor
        canvas1['background'] = 'red'
        bgcolor = 'red'
        print('red')
    def green():
        global bgcolor
        canvas1['background'] = 'green'
        bgcolor = 'green'
        print('green')
    def another():
        global bgcolor
        bg_color = colorchooser.askcolor()[1]
        canvas1['background'] = bg_color
        bgcolor = bg_color
        print(bg_color)
    tk_settings = Tk()
    tk_settings.title('Settings')
    lbl1 = Label(tk_settings, text='Background color')
    lbl1.grid(column=0, row=0)
    var1 = IntVar()
    radio1 = Radiobutton(tk_settings, text='white', value=0, variable=var1, command=white)
    radio1.grid(column=0, row=1)
    radio2 = Radiobutton(tk_settings, text='black', value=1, variable=var1, command=black)
    radio2.grid(column=0, row=2)
    radio3 = Radiobutton(tk_settings, text='blue', value=2, variable=var1, command=blue)
    radio3.grid(column=0, row=3)
    radio4 = Radiobutton(tk_settings, text='yellow', value=3, variable=var1, command=yellow)
    radio4.grid(column=0, row=4)
    radio5 = Radiobutton(tk_settings, text='red', value=4, variable=var1, command=red)
    radio5.grid(column=0, row=5)
    radio6 = Radiobutton(tk_settings, text='green', value=5, variable=var1, command=green)
    radio6.grid(column=0, row=6)
    radio7 = Radiobutton(tk_settings, text='another color', value=6, variable=var1, command=another)
    radio7.grid(column=0, row=7)
def F1(event):
    help_script = '''Star
  Game
----------------------------------------------------------
painting canvas 1.0.1
----------------------------------------------------------
Help and information |Notes
---------------------|------------------------------------
Hold the mouse and   |16.12.24
move the coursor to  |Add pen, marker and eraser functions
paint on the screen. |20.12.24
Press F1 to get a    |Add menu on start and end
help                 |22.12.24
Press numbers (1-9)  |Add help menu and figures
to choose the color  |
for paint            |
1 - black            |
2 - red              |
3 - orange           |
4 - yellow           |
5 - green            |
6 - blue             |
7 - violet           |
8 - white            |
9 - custom color     |
Keys combinations:   |
Ctrl+S save file     |
Ctrl+O open file     |
'''
    tk_help = Tk()
    tk_help.title('Help and information')
    tk_help.iconbitmap('henicon.ico')
    lbl1 = Label(tk_help, text = help_script, justify = tkinter.LEFT, font=('Courier New', 10))
    lbl1.grid(column=0, row=0)

def save_file(event):
    def save():
        t = ent1.get()
        tk_save_file2.destroy()
        file = open(format(t) + '.sti2', 'w')
        ind = 0
        for i1 in dots:
            ind2 = 0
            for i in dots[ind]:
                dots[ind][ind2] = format(i)
                ind2 += 1
            ind += 1
        file.write(bgcolor)
        file.write('\n')
        for i in dots[0:len(dots) - 2]:
            file.write(','.join(i) + '\n')
        file.write(','.join(dots[len(dots) - 1]))
        print(dots)
        print('OK')
    tk_save_file2 = Tk()
    tk_save_file2.title('Write the name of the file')
    tk_save_file2.iconbitmap('henicon.ico')
    ent1 = Entry(tk_save_file2, width=20)
    ent1.grid(column=0, row=0)
    btn1 = Button(tk_save_file2, text='OK', command=save)
    btn1.grid(column=1, row=0)

def open_file(event):
    def OK():
        tk_choose_file_2.destroy()
        file = open(format(ent1.get()) + '.sti2', 'r').read()
        file = file.split('\n')
        canvas1['background'] = file[0]
        bgcolor = file[0]
        for i in file[1:len(file) - 1]:
            s = i.split(',')
            px = int(s[0])
            py = int(s[1])
            color = s[2]
            size = int(s[3])
            canvas1.create_oval(px - size, py - size, px + size, py + size, fill=color, outline=color)
            dots.append([px, py, color, size])
    tk_choose_file_2 = Tk()
    tk_choose_file_2.title('Write the name of the file')
    tk_choose_file_2.iconbitmap('henicon.ico')
    ent1 = Entry(tk_choose_file_2, width=20)
    ent1.grid(column=0, row=0)
    btn1 = Button(tk_choose_file_2, text='OK', command=OK)
    btn1.grid(column=1, row=0)
def figure(event):
    def dot():
        global current_figure
        current_figure = 'dot'
    def square():
        global current_figure
        current_figure = 'square'
    def line():
        global current_figure
        current_figure = 'line'
    tk_figure = Tk()
    tk_figure.title('Choose figure')
    tk_figure.iconbitmap('henicon.ico')
    var1 = IntVar()
    radio1 = Radiobutton(tk_figure, text='dot', value=0, variable=var1, command=dot)
    radio1.grid(column=0, row=0)
    radio2 = Radiobutton(tk_figure, text='square', value=1, variable=var1, command=square)
    radio2.grid(column=0, row=1)
    radio3 = Radiobutton(tk_figure, text='line', value=2, variable=var1, command=line)
    radio3.grid(column=0, row=2)
def clear(event):
    global dots
    canvas1.delete('all')
    dots = []

tk1.bind('<Key-F1>', F1)
tk1.bind('<Key-1>', black)
tk1.bind('<Key-2>', red)
tk1.bind('<Key-3>', orange)
tk1.bind('<Key-4>', yellow)
tk1.bind('<Key-5>', green)
tk1.bind('<Key-6>', blue)
tk1.bind('<Key-7>', violet)
tk1.bind('<Key-8>', white)
tk1.bind('<Key-9>', choose_color)
tk1.bind('<Key-s>', settings)
tk1.bind('<Key-e>', eraser)
tk1.bind('<Key-p>', pen)
tk1.bind('<Key-m>', marker)
tk1.bind('<Key-f>', figure)
tk1.bind('<Key-c>', clear)
tk1.bind('<Key-Up>', up)
tk1.bind('<Key-Down>', down)
tk1.bind('<Control-Key-s>', save_file)
tk1.bind('<Control-Key-o>', open_file)
canvas1.bind('<B1-Motion>', tap)
canvas1.bind('<Button-1>', tap)

mainloop()


def yes():
    tk_save_file1.destroy()
    def save():
        t = ent1.get()
        tk_save_file2.destroy()
        file = open(format(t) + '.sti2', 'w')
        ind = 0
        for i1 in dots:
            ind2 = 0
            for i in dots[ind]:
                dots[ind][ind2] = format(i)
                ind2 += 1
            ind += 1
        file.write(bgcolor)
        file.write('\n')
        for i in dots[0:len(dots) - 2]:
            file.write(','.join(i) + '\n')
        file.write(','.join(dots[len(dots) - 1]))
        print(dots)
        print('OK')
    tk_save_file2 = Tk()
    tk_save_file2.title('Write the name of the file')
    tk_save_file2.iconbitmap('henicon.ico')
    ent1 = Entry(tk_save_file2, width=20)
    ent1.grid(column=0, row=0)
    btn1 = Button(tk_save_file2, text='OK', command=save)
    btn1.grid(column=1, row=0)
    tk_save_file2.mainloop()
def no():
    exit()
tk_save_file1 = Tk()
tk_save_file1.title('Are you want to save file?')
tk_save_file1.iconbitmap('henicon.ico')
btn1 = Button(tk_save_file1, text=' Yes ', command=yes)
btn1.grid(column=0, row=0)
btn2 = Button(tk_save_file1, text=' No ', command=no)
btn2.grid(column=1, row=0)
lbl1 = Label(tk_save_file1, text='                                                                                         ')
lbl1.grid(column=2, row=0)
tk_save_file1.mainloop()
