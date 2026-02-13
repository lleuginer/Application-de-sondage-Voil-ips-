from pathlib import Path
import subprocess
from tkinter import messagebox 
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pygame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

pygame.mixer.init()
pygame.mixer.music.load(r"song\sucess.wav")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def connexion():
    id= entry_1.get()  
    mdp= entry_2.get() 
    if id == "Admin" and mdp == "Admin1234":
        pygame.mixer.music.play()
        messagebox.showinfo("Succès", "Connexion réussie !")
        lien = r"dashboard.py"
        subprocess.Popen(["python", lien])
        window.destroy()
    else:
        messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect.") 
        count= count+1




window = Tk()

window.geometry("577x730")
window.configure(bg = "#3D3D3D")
window.title("Connexion Espace Admin")
window.iconbitmap(r'assets\frame0\logo.ico')


canvas = Canvas(
    window,
    bg = "#3D3D3D",
    height = 730,
    width = 577,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    42.999999999999886,
    83.0,
    anchor="nw",
    text="ADMIN !",
    fill="#FAFFFD",
    font=("Inter", 64 * -1)
)

canvas.create_text(
    36.999999999999886,
    168.0,
    anchor="nw",
    text="Connexion à l’espace Admin",
    fill="#FAFFFD",
    font=("Inter", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    224.9999999999999,
    304.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=50.999999999999886,
    y=281.0,
    width=348.0,
    height=44.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    224.9999999999999,
    418.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
entry_2.place(
    x=50.999999999999886,
    y=395.0,
    width=348.0,
    height=44.0
)

canvas.create_text(
    42.999999999999886,
    251.0,
    anchor="nw",
    text="Indentifiant",
    fill="#FAFFFD",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    42.999999999999886,
    365.0,
    anchor="nw",
    text="Mot-De-Passe",
    fill="#FAFFFD",
    font=("Inter", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=connexion,
    relief="flat"
)
button_1.place(
    x=42.999999999999886,
    y=509.0,
    width=158.0,
    height=46.0
)
window.resizable(False, False)
window.mainloop()
