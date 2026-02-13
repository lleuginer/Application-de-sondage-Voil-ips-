from pathlib import Path
import subprocess
from tkinter import messagebox 
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pygame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


pygame.mixer.init()
pygame.mixer.music.load(r"song\son.mp3")

def b1():
    pygame.mixer.music.stop()
    subprocess.Popen(["python", Sondage])
    window.destroy()

def b2():
    pygame.mixer.music.stop()
    window.destroy()

def b3():
    pygame.mixer.music.stop()
    subprocess.Popen(["python", Connexion])
    window.destroy()
    

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

Connexion = r"Connexion.py"
Sondage = r"Sondage.py"

window = Tk()

window.geometry("1000x625")
window.configure(bg = "#FFFFFF")
window.title("Page d'Acceuil")
window.iconbitmap(r'assets\frame0\logo.ico')

pygame.mixer.music.play()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 625,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1000.0,
    154.0,
    fill="#494949",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    100.0,
    66.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=b1,
    relief="flat"
)
button_1.place(
    x=720.0,
    y=555.0,
    width=243.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=b2,
    relief="flat"
)
button_2.place(
    x=39.0,
    y=555.0,
    width=243.0,
    height=40.0
)

canvas.create_text(
    30.0,
    115.0,
    anchor="nw",
    text="SPACE-DATA",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    255.0,
    59.0,
    anchor="nw",
    text="SONDAGE VOYAGE VOILIP’S",
    fill="#FFFFFF",
    font=("Inter", 40 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    499.0,
    313.0,
    image=image_image_2
)

canvas.create_text(
    255.0,
    449.0,
    anchor="nw",
    text="Votez pour votre destination de voyage préférée !",
    fill="#000000",
    font=("Inter", 24 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=b3,
    relief="flat"
)
button_3.place(
    x=861.0,
    y=59.0,
    width=110.0,
    height=42.0
)
window.resizable(False, False)
window.mainloop()
