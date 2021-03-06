
import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    button =event.widget
    num=button["text"]
    if num=="=":
        eq=entry.get()
        re=eval(eq)
        entry.delete(0,tk.END)
        entry.insert(tk.END,re)
    elif num == "C":
        entry.delete(0,tk.END)

    elif num == "%":
        sub=entry.get()
        entry.delete(0,tk.END)
        ans = int(sub)*100
        return entry.insert(tk.END,ans)

    elif num == "♡":
        return entry.insert(tk.END,"大好き♡")

    elif num == "( ﾉД`)":
        return entry.insert(tk.END,"嫌い。。。")

    else:
        entry.insert(tk.END,num)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("超高機能電卓")
    entry=tk.Entry(root, justify="right",width=10,font=("Times New Roman",40))
    entry.grid(column=0,columnspan=5)
    r,c=1,0
    for i, num in enumerate(["%","-","÷","del",7,8,9,"=",4,5,6,"+",1,2,3,"C",0,"♡","( ﾉД`)","*"]):
        button = tk.Button(root,text=f"{num}", width=4,height=2, font=("Times New Roman", 30))
        button.bind("<1>",button_click)
        button.grid(row=r,column=c)
        c+=1
        if (i+1)%4==0:
            r+=1
            c = 0
       
    root.mainloop()