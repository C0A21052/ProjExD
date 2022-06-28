import tkinter as tk
import tkinter.messagebox as tkm
import random
import maze_maker as ml

def make_maze(yoko, tate):
    XP = [0, 1, 0, -1]
    YP = [-1, 0, 1, 0]

    maze_lst = []
    for y in range(tate):
        maze_lst.append([0]*yoko)
    for x in range(yoko):
        maze_lst[0][x] = 1
        maze_lst[tate-1][x] = 1
    for y in range(1, tate-1):
        maze_lst[y][0] = 1
        maze_lst[yoko][yoko-1] = 1






def key_down(event):
    global key
    key = event.keysym
    print(f"{key}が押されました")
def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    delta = {
       ""  :[0, 0],
       "Up":[0, -1],
       "Down":[0, +1],
       "Left":[-1, 0],
       "Right":[+1, 0],
       }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass
    # if key == "Up" : my -= 1
    # if key == "Down" : my += 1
    # if key == "Left" : mx -= 1
    # if key == "Right" : mx += 1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100,main_proc)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()
    maze_bg = ml.make_maze(15, 9)
    ml.show_maze(canvas, maze_bg)


    tori = tk.PhotoImage(file="ex03/fig/6.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    root.mainloop()

