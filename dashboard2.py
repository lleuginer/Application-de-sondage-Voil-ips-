import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkinter import Tk, Canvas, Button, PhotoImage
from pathlib import Path
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def statistique(canvas):
    
    compteurs_genre = {"Homme": 0, "Femme": 0, "Autres": 0}
    compteurs_destination = {"Croatie": 0, "Espagne": 0}
    compteurs_mois = {"Juillet": 0, "Août": 0}
    compteurs_niveaux = {"Bachelor": 0, "Ingénieur": 0, "Msc IA & Cyber": 0, "Msc Aéro Propulsion": 0, "MBA": 0}

    
    with open("Sondage.csv", "r", encoding='latin1') as F:
        for line in F.readlines():
            L = line.strip().split(";")
            if len(L) < 6: 
                continue

           
            if L[0] == "1":
                compteurs_genre["Homme"] += 1
            elif L[0] == "2":
                compteurs_genre["Femme"] += 1
            elif L[0] == "3":
                compteurs_genre["Autres"] += 1

            
            if L[4] == "1":
                compteurs_destination["Croatie"] += 1
            elif L[4] == "2":
                compteurs_destination["Espagne"] += 1

            
            if L[5] == "1":
                compteurs_mois["Juillet"] += 1
            elif L[5] == "2":
                compteurs_mois["Août"] += 1

            
            if L[3] == "1":
                compteurs_niveaux["Bachelor"] += 1
            elif L[3] == "2":
                compteurs_niveaux["Ingénieur"] += 1
            elif L[3] == "3":
                compteurs_niveaux["Msc IA & Cyber"] += 1
            elif L[3] == "4":
                compteurs_niveaux["Msc Aéro Propulsion"] += 1
            elif L[3] == "5":
                compteurs_niveaux["MBA"] += 1

   
    def filtrer_categories(labels, valeurs):
        filtered_labels = []
        filtered_valeurs = []
        for label, valeur in zip(labels, valeurs):
            if valeur > 0:  
                filtered_labels.append(label)
                filtered_valeurs.append(valeur)
        return filtered_labels, filtered_valeurs

       
    fig1, ax1 = plt.subplots(figsize=(5, 3))
    labels1, valeurs1 = filtrer_categories(compteurs_genre.keys(), compteurs_genre.values())
    if valeurs1:
        ax1.pie(valeurs1, labels=labels1, autopct='%1.2f%%', colors=['#4169E1', '#0000CD', '#87CEEB'], shadow=True, startangle=140)
        ax1.set_title("Répartition par Genre")
    canvas1 = FigureCanvasTkAgg(fig1, master=window)
    canvas1.draw()
    canvas1.get_tk_widget().place(x=370, y=100, width=600, height=350)  

    
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    labels2, valeurs2 = filtrer_categories(compteurs_destination.keys(), compteurs_destination.values())
    if valeurs2:
        ax2.bar(labels2, valeurs2, color=['#4169E1', '#ADD8E6'])
        ax2.set_title("Destination Choisie")
        ax2.set_ylabel("Nombre de participants")
    canvas2 = FigureCanvasTkAgg(fig2, master=window)
    canvas2.draw()
    canvas2.get_tk_widget().place(x=925, y=450, width=400, height=250)  

   
    fig3, ax3 = plt.subplots(figsize=(5, 3))
    labels3, valeurs3 = filtrer_categories(compteurs_mois.keys(), compteurs_mois.values())
    if valeurs3:
        ax3.bar(labels3, valeurs3, color=['#4169E1', '#ADD8E6'])
        ax3.set_title("Mois Choisi")
        ax3.set_ylabel("Nombre de participants")
    canvas3 = FigureCanvasTkAgg(fig3, master=window)
    canvas3.draw()
    canvas3.get_tk_widget().place(x=435, y=450, width=400, height=250)  

    fig4, ax4 = plt.subplots(figsize=(5, 3))
    labels4, valeurs4 = filtrer_categories(compteurs_niveaux.keys(), compteurs_niveaux.values())
    if valeurs4:
        ax4.pie(valeurs4, labels=labels4, autopct='%1.2f%%', colors=['#4169E1', '#0000CD', '#87CEEB', '#ADD8E6', '#F0FFFF'], shadow=True, startangle=140)
        ax4.set_title("Répartition des Niveaux")
    canvas4 = FigureCanvasTkAgg(fig4, master=window)
    canvas4.draw()
    canvas4.get_tk_widget().place(x=820, y=100, width=600, height=350) 

def Accueil():
    lien = r"gui.py"
    subprocess.Popen(["python", lien])
    window.destroy()

def dashboard():
    lien = r"dashboard.py"
    subprocess.Popen(["python", lien])
    window.destroy()

def dashboard3():
    lien = r"dashboard3.py"
    subprocess.Popen(["python", lien])
    window.destroy()

window = Tk()
window.geometry("1400x750")
window.configure(bg="#101010")
window.title("Espace Admin (Details)")
window.iconbitmap(r'assets\frame0\logo.ico')

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
    369.0,
    0.0,
    1409.0,
    750.0,
    fill="#FFFFFF",
    outline="")


canvas.create_text(
    415.0,
    19.0,
    anchor="nw",
    text="Details Menu",
    fill="#262A41",
    font=("Poppins SemiBold", 50 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    60.0,
    88.0,
    image=image_image_5
)

canvas.create_text(
    110.0,
    65.0,
    anchor="nw",
    text="ADMIN PANEL",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Accueil,
    relief="flat"
)
button_1.place(
    x=36.0,
    y=632.7764892578125,
    width=132.0,
    height=46.7235107421875
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy, 
    relief="flat"
)
button_2.place(
    x=188.0,
    y=632.7764892578125,
    width=132.0,
    height=46.7235107421875
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=dashboard3,
    relief="flat"
)
button_3.place(
    x=50.0,
    y=301.28125,
    width=259.9591979980469,
    height=46.7235107421875
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Page Actuelle"),
    relief="flat"
)
button_4.place(
    x=50.0,
    y=237.640625,
    width=259.9591979980469,
    height=46.7235107421875
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=dashboard,
    relief="flat"
)
button_5.place(
    x=54.04081726074219,
    y=174.0,
    width=259.9591979980469,
    height=46.7235107421875
)


window.after(1, lambda: statistique(canvas))

window.resizable(False, False)
window.mainloop()