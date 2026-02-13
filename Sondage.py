import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from tkinter import ttk
from tkinter import messagebox 
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pygame
import csv
from email.mime.image import MIMEImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

pygame.mixer.init()
pygame.mixer.music.load(r"song\envoi.wav")
Sound1 = pygame.mixer.Sound(r"song\son.mp3")


def enregistrer():
    Genre=(entry_1.get())
    if Genre=="Homme":
        g=1
    elif Genre=="Femme":
        g=2
    elif Genre=="Autres":
        g=3
    else:
        g=-1
    Prénom=(entry_3.get())
    Nom=(entry_2.get())
    Niveau=(entry_4.get())
    if Niveau=="Cycle Bachelor":
        N=1
    elif Niveau=="Cycle Ingénieur":
        N=2
    elif Niveau=="Msc IA & Cyber":
        N=3
    elif Niveau=="Msc Aéro Propulsion":
        N=4
    elif Niveau=="MBA":
        N=5
    else:
        N=-1
    Destination=(entry_5.get())
    if Destination=="Croatie":
        D=1
    elif Destination=="Espagne":
        D=2
    else:
        D=-1
    Mois=(entry_6.get())
    if Mois=="Aout":
        M=2
    elif Mois=="Juillet":
        M=1
    else:
        M=-1
    if g and M and N and D != -1 :
        F=open("Sondage.csv","a", encoding="utf-8")
        F.write(str(g)+";"+Prénom+";"+Nom+";"+str(N)+";"+str(D)+";"+str(M)+";\n")
        F.close()
        messagebox.showinfo("Merci pour vos réponses !", "Un mail contenant votre remerciement vous à été envoyé !" )
        pygame.mixer.music.play()
        Mail = (entry_7.get())
        F=open("Mail.csv","a")
        F.write(Mail+"\n")
        F.close()
        Sound1.stop()
        window.destroy()
    else:
        messagebox.showwarning("Erreur d'envois !", "Vous devez répondre au sondage pour envoyer !" )
    
    qr_img_path = r"assets\frame0\VoilipsQr.png"


    smtp_server = "smtp.gmail.com" 
    smtp_port = 587  
    email_sender = "#mettre votre adresse mail ici"
    email_password = "mettre votre mot de passe ici"  
    email_receiver = Mail


    msg = MIMEMultipart()
    msg["From"] = email_sender
    msg["To"] = email_receiver
    msg["Subject"] = "VOILIP'S VOYAGE 2025 | SONDAGE"


    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; }}
            .container {{ padding: 20px; border: 1px solid #ddd; border-radius: 10px; width: 400px; margin: auto; }}
            .qrcode {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Merci d'avoir répondu au questionnaire,\n Voici votre QR Code !</h2>
            <p>Scannez-le pour accéder à votre surprise :</p>
            <img src="cid:qrcode" class="qrcode"/>
        </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(html_content, "html"))


    with open(qr_img_path, "rb") as img_file:
        img = MIMEImage(img_file.read(), name="VoilipsQr.png")
        img.add_header("Content-ID", "<qrcode>")
        msg.attach(img)


    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()
        print("✅ Email envoyé avec succès !")
    except Exception as e:
        print("❌ Erreur lors de l'envoi :", e)



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


genres = ["Homme", "Femme", "Autres",]
Niveau = ["Cycle Bachelor", "Cycle Ingénieur", "Msc IA & Cyber", "Msc Aéro Propulsion", "MBA",]
Destination = ["Croatie", "Espagne",]
Mois = ["Juillet", "Aout",]


window = Tk()

window.geometry("1200x700")
window.configure(bg = "#555555")
window.title("Page de Sondage")
window.iconbitmap(r'assets\frame0\logo.ico')

Sound1.play()

canvas = Canvas(
    window,
    bg = "#555555",
    height = 700,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    1.1368683772161603e-13,
    0.0,
    1200.0,
    143.0,
    fill="#282828",
    outline="")

canvas.create_text(
    139.9999999999999,
    15.0,
    anchor="nw",
    text="SONDAGE VOILIP’S 2025",
    fill="#FAFFFD",
    font=("Inter", 64 * -1)
)

canvas.create_text(
    145.9999999999999,
    77.0,
    anchor="nw",
    text="Vos réponses seront valorisées",
    fill="#FAFFFD",
    font=("Inter", 36 * -1)
)

#Entry 1 = Genre
entry_1 = ttk.Combobox(window, values=genres, state="readonly")

entry_1.place(
    x=134.9999999999999,
    y=271.0,
    width=314.0,
    height=31.0
)

#Entry 2 = NOM
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_2 = canvas.create_image(
    291.9999999999999,
    197.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=134.9999999999999,
    y=181.0,
    width=314.0,
    height=30.0
)

canvas.create_text(
    132.9999999999999,
    250.0,
    anchor="nw",
    text="Genre",
    fill="#FAFFFD",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    126.99999999999989,
    160.0,
    anchor="nw",
    text="Nom ",
    fill="#FAFFFD",
    font=("Inter", 18 * -1)
)

#Entry 3 = Prénom
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_3 = canvas.create_image(
    783.9999999999999,
    197.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=626.9999999999999,
    y=181.0,
    width=314.0,
    height=30.0
)


#Entry 4 = Niveau
entry_4 = ttk.Combobox(window, values=Niveau, state="readonly")

entry_4.place(
    x=622.9999999999999,
    y=271.0,
    width=314.0,
    height=31.0
)

canvas.create_text(
    618.9999999999999,
    160.0,
    anchor="nw",
    text="Prénom",
    fill="#FAFFFD",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    624.9999999999999,
    250.0,
    anchor="nw",
    text="Niveau",
    fill="#FAFFFD",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    132.9999999999999,
    351.0,
    anchor="nw",
    text="Destination",
    fill="#FAFFFD",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    132.9999999999999,
    452.0,
    anchor="nw",
    text="Mois",
    fill="#FAFFFD",
    font=("Inter", 18 * -1)
)

#Entry 5 = Destination
entry_5 = ttk.Combobox(window, values=Destination, state="readonly")

entry_5.place(
    x=134.9999999999999,
    y=372.0,
    width=314.0,
    height=30.0
)

#Entry 6 = Mois
entry_6 = ttk.Combobox(window, values=Mois, state="readonly")

entry_6.place(
    x=130.9999999999999,
    y=472.0,
    width=313.0,
    height=31.0
)

canvas.create_text(
    137.9999999999999,
    547.0,
    anchor="nw",
    text="Votre Mail",
    fill="#FAFFFD",
    font=("Inter", 18 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_7 = canvas.create_image(
    302.9999999999999,
    585.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=145.9999999999999,
    y=569.0,
    width=314.0,
    height=30.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=enregistrer,
    relief="flat"
)
button_1.place(
    x=220.2233886718749,
    y=637.4273071289062,
    width=143.00286865234375,
    height=32.212039947509766
)

image_image_1 = PhotoImage(
    file=relative_to_assets("photo1.png"))
image_1 = canvas.create_image(
    947.3366088867186,
    533.1665649414062,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("photo2.png"))
image_2 = canvas.create_image(
    684.6356811523436,
    533.1665649414062,
    image=image_image_2
)

canvas.create_text(
    893.9999999999999,
    345.0,
    anchor="nw",
    text=" CROATIE",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    624.9999999999999,
    344.0,
    anchor="nw",
    text="ESPAGNE",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    67.00000000000011,
    70.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
