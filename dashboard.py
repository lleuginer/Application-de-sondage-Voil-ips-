import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Accueil():
    lien = r"gui.py"
    subprocess.Popen(["python", lien])
    window.destroy()

def dashboard2():
    lien = r"dashboard2.py"
    subprocess.Popen(["python", lien])
    window.destroy()

def dashboard3():
    lien = r"dashboard3.py"
    subprocess.Popen(["python", lien])
    window.destroy()

def statistique(canvas):
   
    compteurs_destination = {"Croatie": 0, "Espagne": 0}
    compteurs_mois = {"Juillet": 0, "Août": 0}

  
    with open("Sondage.csv", "r", encoding='latin1') as F:
        for line in F.readlines():
            L = line.strip().split(";")
            if len(L) < 6:
                continue

           
            if L[4] == "1":
                compteurs_destination["Croatie"] += 1
            elif L[4] == "2":
                compteurs_destination["Espagne"] += 1

          
            if L[5] == "1":
                compteurs_mois["Juillet"] += 1
            elif L[5] == "2":
                compteurs_mois["Août"] += 1

   
    def filtrer_categories(labels, valeurs):
        filtered_labels = []
        filtered_valeurs = []
        for label, valeur in zip(labels, valeurs):
            if valeur > 0:  
                filtered_labels.append(label)
                filtered_valeurs.append(valeur)
        return filtered_labels, filtered_valeurs

        


    fig2, ax2 = plt.subplots(figsize=(5, 3))
    labels2, valeurs2 = filtrer_categories(compteurs_destination.keys(), compteurs_destination.values())
    if valeurs2:
        ax2.bar(labels2, valeurs2, color=['#4169E1', '#ADD8E6'])
        ax2.set_title("Destination Choisie")
        ax2.set_ylabel("Nombre de participants")
    canvas2 = FigureCanvasTkAgg(fig2, master=window)
    canvas2.draw()
    canvas2.get_tk_widget().place(x=925, y=250, width=400, height=450) 

   
    fig3, ax3 = plt.subplots(figsize=(5, 3))
    labels3, valeurs3 = filtrer_categories(compteurs_mois.keys(), compteurs_mois.values())
    if valeurs3:
        ax3.bar(labels3, valeurs3, color=['#4169E1', '#ADD8E6'])
        ax3.set_title("Mois Choisi")
        ax3.set_ylabel("Nombre de participants")
    canvas3 = FigureCanvasTkAgg(fig3, master=window)
    canvas3.draw()
    canvas3.get_tk_widget().place(x=435, y=250, width=400, height=450) 

window = Tk()
window.title("Espace Admin (Dashboard)")
window.iconbitmap(r'assets\frame0\logo.ico')

window.geometry("1400x750")
window.configure(bg="#101010")

canvas = Canvas(
    window,
    bg="#101010",
    height=750,
    width=1400,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    360.0,
    0.0,
    1400.0,
    750.0,
    fill="#FFFFFF",
    outline="")



canvas.create_text(
    396.0,
    113.0,
    anchor="nw",
    text="Visualisez ici les principales informations relatives à \nvotre requête !",
    fill="#404852",
    font=("Poppins Regular", 25 * -1)
)

canvas.create_text(
    396.0,
    35.0,
    anchor="nw",
    text="Dashboard Menu",
    fill="#262A41",
    font=("Poppins SemiBold", 50 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("box.png"))
image_3 = canvas.create_image(
    1231.0,
    107.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("logodash.png"))
image_4 = canvas.create_image(
    73.0,
    88.0,
    image=image_image_4
)

canvas.create_text(
    102.0,
    72.0,
    anchor="nw",
    text="ADMIN PANEL",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 36 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Accueil,
    relief="flat"
)
button_2.place(
    x=30.0,
    y=632.7764892578125,
    width=132.0,
    height=46.7235107421875
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_3.place(
    x=182.0,
    y=632.7764892578125,
    width=132.0,
    height=46.7235107421875
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=dashboard3,
    relief="flat"
)
button_4.place(
    x=50.0,
    y=301.28125,
    width=259.9591979980469,
    height=46.7235107421875
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=dashboard2,
    relief="flat"
)
button_5.place(
    x=50.0,
    y=237.640625,
    width=259.9591979980469,
    height=46.7235107421875
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Page Actuelle"),
    relief="flat"
)
button_6.place(
    x=54.04081726074219,
    y=174.0,
    width=259.9591979980469,
    height=46.7235107421875
)


window.after(1, lambda: statistique(canvas))

window.resizable(False, False)
window.mainloop()