import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from pathlib import Path
from tkinter import ttk
from tkinter import messagebox 
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import pygame
import csv
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame3")


pygame.mixer.init()
pygame.mixer.music.load(r"song\envoi.wav")

def choisir_fichier():
    global fichier_joint
    fichier_joint = filedialog.askopenfilename(title="Sélectionner une pièce jointe")
    if fichier_joint:
        messagebox.showinfo("Fichier sélectionné", f"Fichier joint : {os.path.basename(fichier_joint)}")
    else:
        fichier_joint = None

def envois():
    email_1 = entry_1.get().strip()
    email_2= entry_2.get().strip()

    if email_1:
        selected_email = email_1
    elif email_2:
        selected_email = email_2
    else:
        messagebox.showerror("Erreur", "Veuillez entrer une adresse e-mail dans l'un des champs !")


    smtp_server = "smtp.gmail.com"  
    smtp_port = 587  
    email_sender = "mettre votre adresse mail ici"
    email_password = "mettre votre mot de passe ici"  
    email_receiver = selected_email

    qr_img_path = r"assets\frame0\VoilipsQr.png"

    
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

        if fichier_joint:
            with open(fichier_joint, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(fichier_joint)}")
                msg.attach(part)




    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()
        print("✅ Email envoyé avec succès !")
        pygame.mixer.music.play()
    except Exception as e:
        print("❌ Erreur lors de l'envoi :", e)
    messagebox.showinfo("Merci pour vos réponses !", "Un mail contenant votre remerciement vous à été envoyé !" )


def liste_emails(Fichier):
    emails = []
    try:
        with open(Fichier, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:  
                    emails.append(row[0])  
    except FileNotFoundError:
        print("Fichier non trouvé ! Vérifier le chemin.")
    return emails


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

def dashboard():
    lien = r"dashboard.py"
    subprocess.Popen(["python", lien])
    window.destroy()

window = Tk()

window.geometry("1400x750")
window.configure(bg = "#101010")
window.title("Espace Admin (Mail)")
window.iconbitmap(r'assets\frame0\logo.ico')

fichier_csv = "Mail.csv"
emails = liste_emails(fichier_csv)

canvas = Canvas(
    window,
    bg = "#101010",
    height = 750,
    width = 1400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    369.0,
    0.0,
    1409.0,
    750.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    884.0,
    454.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=choisir_fichier,
    relief="flat"
)
button_1.place(
    x=1090.0,
    y=438.0,
    width=107.0,
    height=56.0
)

canvas.create_text(
    463.0,
    223.0,
    anchor="nw",
    text="MAIL AUTOMATIQUE :",
    fill="#FAFFFD",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    463.0,
    314.0,
    anchor="nw",
    text="Choisissez le mail dans la liste ",
    fill="#FAFFFD",
    font=("Inter", 25 * -1)
)

#Entry 1 = Combobox mails
entry_1 = ttk.Combobox(window, values=emails, state="readonly")

entry_1.place(
    x=471.0,
    y=352.0,
    width=384.0,
    height=45.0
)

canvas.create_text(
    469.0,
    455.0,
    anchor="nw",
    text="Entrer le mail manuellement ",
    fill="#FAFFFD",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    998.0,
    360.0,
    anchor="nw",
    text="Ajoutez un pièce jointe :",
    fill="#FAFFFD",
    font=("Inter", 25 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    669.5,
    513.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=477.0,
    y=490.0,
    width=385.0,
    height=44.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=envois,
    relief="flat"
)
button_2.place(
    x=568.9699096679688,
    y=599.2659912109375,
    width=173.73780822753906,
    height=45.734012603759766
)

canvas.create_text(
    415.0,
    29.0,
    anchor="nw",
    text="Mail Menu",
    fill="#262A41",
    font=("Poppins SemiBold", 50 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    60.0,
    88.0,
    image=image_image_2
)

canvas.create_text(
    110.0,
    65.0,
    anchor="nw",
    text="ADMIN PANEL",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 36 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Accueil,
    relief="flat"
)
button_3.place(
    x=36.0,
    y=632.7764892578125,
    width=132.0,
    height=46.7235107421875
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_4.place(
    x=188.0,
    y=632.7764892578125,
    width=132.0,
    height=46.7235107421875
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Page Actuelle"),
    relief="flat"
)
button_5.place(
    x=50.0,
    y=301.28125,
    width=259.9591979980469,
    height=46.7235107421875
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=dashboard2,
    relief="flat"
)
button_6.place(
    x=50.0,
    y=237.640625,
    width=259.9591979980469,
    height=46.7235107421875
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=dashboard,
    relief="flat"
)
button_7.place(
    x=54.04081726074219,
    y=174.0,
    width=259.9591979980469,
    height=46.7235107421875
)

canvas.create_text(
    415.0,
    102.0,
    anchor="nw",
    text="Il est possible depuis ce menu d’envoyer un mail à une \npersonne déjà inscrite ou bien de le faire  manuellement. ",
    fill="#404852",
    font=("Poppins Regular", 25 * -1)
)
window.resizable(False, False)
window.mainloop()
