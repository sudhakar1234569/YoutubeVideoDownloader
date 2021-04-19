import tkinter as tk
from tkinter import *
import pytube
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('YV-Downloader')
root.geometry('500x400')
root.configure(bg='white')
root.iconbitmap('downarrow.ico')

val = tk.StringVar()


# --------- change color functions ----#
def chage():
    root.configure(bg='black')
    Label(root, text="Link : ", font=("Airal", 20), width=5, fg='white', bg='black').place(x=20, y=50)
    Entry(root, width=50, textvariable=val, fg='yellow', bg='black').place(x=100, y=60)
    Label(root, image=new_pic, bg='black').place(x=180, y=85)
    Label(root, text="YV-Downloader", font=("Airal", 25), fg='white', bg='black').place(x=110)


def chage2():
    root.configure(bg='white')
    Label(root, text="Link : ", font=("Airal", 20), width=5, bg='white').place(x=20, y=50)
    Entry(root, width=50, textvariable=val, bg='white').place(x=100, y=60)
    Label(root, image=new_pic, bg='white').place(x=180, y=85)
    Label(root, text="YV-Downloader", font=("Airal", 25), fg='black', bg='white').place(x=110)


def download():
    name = val.get()
    SAVE_PATH = "C:/Users/god/Desktop/GUI-P/output/"
    try:
        link = pytube.YouTube(name)
        stream = link.streams.first()
        stream.download(SAVE_PATH)
        # ---- alert box --- #
        messagebox.showinfo("Info", "Video Download Successfully!")
    except ConnectionError:
        messagebox.showerror("Error","Your internet is slow")


# ----------------------------------------------------------------------------------------#
# ---- Buttons ---#
Button(root, text='Dark', command=chage, width=5, bg='white').place(x=455)
Button(root, text='Day', command=chage2, width=5, bg='white').place(x=455, y=30)
# ---- Header----#
words = Label(root, text="YV-Downloader", font=("Airal", 25), bg='white')
words.place(x=110)
# ---------------------------------------------------------#
link = Label(root, text="Link : ", font=("Airal", 20), width=5, bg='white').place(x=20, y=50)
e1 = Entry(root, textvariable=val, width=50).place(x=100, y=60)
# -------------------------- Download -----------------#
# open image
my_pic = Image.open('downarrow.png')
# resize image
resize = my_pic.resize((50, 50), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resize)

my_label = Label(root, image=new_pic, bg='white')
my_label.place(x=180, y=85)

# ----------------Download Button ----------------------------------------------#

Button(root, text='Download', font=("Airal", 15), command=download, fg='white', bg='blue').place(x=242, y=92)
Button(root, text="Exit", font=("Airal", 15), fg='white', bg='red', width=5, command=root.quit).place(x=230, y=200)
mainloop()
