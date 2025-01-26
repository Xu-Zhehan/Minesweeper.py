import turtle
import random
from tkinter import messagebox

left = 10
abks = 9 * 9
land = [[0] * 9 for _ in range(9)]
flag = [[0] * 9 for _ in range(9)]
mnum = [[9] * 9 for _ in range(9)]
rx = [1, -1, 0, 0, 1, 1, -1, -1]
ry = [0, 0, 1, -1, 1, -1, 1, -1]

#clicked = False
unongame = False

turtle.setup(300, 360)
t = turtle.Pen()
s = turtle.Screen()
s.tracer(0, 0)

def getrealx(x):
    if -130 <= x and x <= -110:
        return 0
    elif -100 <= x and x <= -80:
        return 1
    elif -70 <= x and x <= -50:
        return 2
    elif -40 <= x and x <= -20:
        return 3
    elif -10 <= x and x <= 10:
        return 4
    elif 20 <= x and x <= 40:
        return 5
    elif 50 <= x and x <= 70:
        return 6
    elif 80 <= x and x <= 100:
        return 7
    elif 110 <= x and x <= 130:
        return 8

def getrealy(y):
    if 90 <= y and y <= 110:
        return 0
    elif 60 <= y and y <= 80:
        return 1
    elif 30 <= y and y <= 50:
        return 2
    elif 0 <= y and y <= 20:
        return 3
    elif -30 <= y and y <= -10:
        return 4
    elif -60 <= y and y <= -40:
        return 5
    elif -90 <= y and y <= -70:
        return 6
    elif -120 <= y and y <= -100:
        return 7
    elif -150 <= y and y <= -130:
        return 8

def Open(x, y):
    #global clicked
    #clicked = True
    global unongame
    if unongame:
        return 0
    global abks
    rlx = getrealx(x)
    rly = getrealy(y)
    if land[rlx][rly]:
        messagebox.showinfo("", "你踩雷了")
        unongame = True
        s.update()
        for i in range(9):
            for j in range(9):
                if land[i][j] == 1:
                    exec('_' + str(i) + str(j) + '.color("red")')
    else:
        flag[rlx][rly] = 2
        abks -= 1
        pname = '_' + str(rlx) + str(rly)
        roundmines = mnum[rlx][rly]
        exec(pname + '.color("black")')
        exec(pname + '.hideturtle()')
        if roundmines > 0:
            exec(pname + '.write("' + str(roundmines) + '", align="center")')
        else:
            for i in range(8):
                sx = rlx + rx[i]
                sy = rly + ry[i]
                if(sx >= 0 and sx < 9 and sy >= 0 and sy < 9):
                    if flag[sx][sy] != 2 and (not land[sx][sy]):
                        Open(x + rx[i] * 30, y + ry[i] * -30)
    s.update()

def Flag(x, y):
    global unongame
    if unongame:
        return 0
    global left
    #global clicked
    #clicked = True
    rlx = getrealx(x)
    rly = getrealy(y)
    pname = '_' + str(rlx) + str(rly)
    if flag[rlx][rly] == 0 and left > 0:
        flag[rlx][rly] = 1
        exec(pname + '.color("blue")')
        left -= 1
    elif flag[rlx][rly] == 1 and left < 10:
        flag[rlx][rly] = 0
        exec(pname + '.color("black")')
        left += 1
    s.update()

s.title("Minesweeper")
t.speed(0)
t.hideturtle()

for i in range(10):
    x = random.randint(0, 8)
    y = random.randint(0, 8)
    while land[x][y] == 1:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
    land[x][y] = 1

for x in range(-120, 150, 30):
    for y in range(100, -170, -30):
        penname = '_' + str(getrealx(x)) + str(getrealy(y))
        exec(penname + ' = turtle.Pen()')
        exec(penname + '.penup()')
        exec(penname + '.speed(0)')
        exec(penname + '.shape("square")')
        exec(penname + '.goto(' + str(x) + ', ' + str(y) + ')')
        roundmines = 0
        for i in range(8):
            sx = getrealx(x) + rx[i]
            sy = getrealy(y) + ry[i]
            if(sx >= 0 and sx < 9 and sy >= 0 and sy < 9):
                if land[sx][sy]:
                    roundmines += 1
        mnum[getrealx(x)][getrealy(y)] = roundmines
        exec(penname + '.onclick(Open, btn=1)')
        exec(penname + '.onclick(Flag, btn=3)')

while not abks == 10:
    t.clear()
    t.penup()
    t.goto(-120, 140);
    t.write("剩余雷数：" + str(left))# + ' : ' + str(abks))
    for x in range(-120, 150, 30):
        for y in range(100, -170, -30):
            if flag[getrealx(x)][getrealy(y)] == 2:
                t.goto(x, y)
                if mnum[getrealx(x)][getrealy(y)] > 0:
                    t.write(str(mnum[getrealx(x)][getrealy(y)]), align='center')
    s.update()
messagebox.showinfo("", "你赢了")
s.update()
unongame = True
turtle.done()
    
            






































