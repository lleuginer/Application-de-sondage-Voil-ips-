# ⛵ Application de Sondage & Dashboard Admin - Voyage Voil'ips

Bienvenue sur le ghitub de l'application de gestion de sondage pour le voyage de l'asso **Voil'ips**. Ce projet est une application développée en Python, permettant aux étudiants de voter pour leurs préférences de voyage et aux administrateurs (membre du bureau de l'association VOIL'IPS) de visualiser les statistiques et gérer les communications.

## 📋 Description :

Cette application a été conçue pour faciliter l'organisation d'un voyage étudiant (Association de VOILE de l'IPSA). Elle se divise en deux parties :

1. **Interface Étudiant :** Un formulaire intuitif pour collecter les informations (Nom, Promo, Préférences de destination et de dates).
2. **Interface Administrateur :** Un espace sécurisé permettant de visualiser les résultats du sondage sous forme de statistiques et d'envoyer des e-mails aux participants.

## ✨ Fonctionnalités :

### 👤 Côté Utilisateur

* **Interface Graphique Moderne :** Design épuré réalisé avec `Tkinter`.
* **Sondage Interactif :** Collecte du Genre, Nom, Prénom, Niveau d'étude (Bachelor, Ingénieur, etc.).
* **Choix du Voyage :** Vote pour la destination (ex: Croatie vs Espagne) et la période (Juillet vs Août).
* **Ambiance Sonore :** Musique de fond intégrée via `Pygame`.

### 🛠 Côté Administrateur

* **Authentification Sécurisée :** Page de connexion pour accéder au dashboard.
* **Visualisation des Données :**
* Graphiques générés dynamiquement avec `Matplotlib`.
* Statistiques sur la répartition par genre, par promo, par destination et par mois.


* **Gestion des E-mails :**
* Module d'envoi d'e-mails intégré (`smtplib`).
* Possibilité d'ajouter des pièces jointes.
* Qr Code personnalisé envoyé à la fin de l'inscription.
* Automatisation de l'envoi des mails.
* Sélection des destinataires via une base de données CSV.


## 💻 Librairies Utilisées

* **Langage :** Python 3.x
* **Interface (GUI) :** `Tkinter` (Standard Python)
* **Graphiques :** `Matplotlib`, `Pandas`
* **Audio :** `Pygame`
* **Système & Processus :** `Subprocess`, `Pathlib`
* **E-mailing :** `smtplib`, `email.mime`
* **Données :** Fichiers `.csv` (Manipulation native et Pandas)

## 📂 Structure du Projet

Voici un aperçu des fichiers principaux :

* `gui.py` : **Point d'entrée de l'application**. Menu principal (Sondage ou Connexion).
* `Sondage.py` : Formulaire de collecte de données pour les utilisateurs.
* `Connexion.py` : Page de login pour l'administration.
* `dashboard.py` : Tableau de bord #1 (Stats Destinations & Mois).
* `dashboard2.py` : Tableau de bord #2 (Stats Genres & Niveaux).
* `dashboard3.py` : Interface d'envoi d'e-mails.
* `Sondage.csv` : Base de données stockant les réponses des étudiants.
* `Mail.csv` : Liste des e-mails des étudiants.
* `song` : Dossier de sons d'interface utilisable.
* `assets` : Dossier des différentes images utilisées.

## 🚀 Installation et Utilisation

### Prérequis

Assurez-vous d'avoir Python installé. Vous aurez besoin d'installer les bibliothèques tierces suivantes :

```bash
pip install pandas matplotlib pygame

```

### Lancer l'application

Clonez ce dépôt et lancez le fichier principal :

```bash
git clone https://github.com/votre-nom-utilisateur/nom-du-repo.git
cd nom-du-repo
python gui.py

```

### 🔐 Accès Administrateur (Démonstration)

Pour tester l'interface administrateur, utilisez les identifiants par défaut (codés en dur dans `Connexion.py`) :

* **ID :** `Admin`
* **Mot de passe :** `Admin1234`

## 📸 Aperçu

Application Guy :
<img width="2487" height="1627" alt="image" src="https://github.com/user-attachments/assets/23d4ed12-6921-4c7a-b42c-2d9d55fb0ef1" />

Sondage : 
<img width="2990" height="1825" alt="image" src="https://github.com/user-attachments/assets/8e4bfe5f-a51d-479d-9380-69fa4c1ca9ca" />

Connexion Admin : 
<img width="1442" height="1880" alt="image" src="https://github.com/user-attachments/assets/5ea46583-ee51-4e46-9bba-27f8076a265a" />

Dashboard 1 : 
<img width="3495" height="1942" alt="image" src="https://github.com/user-attachments/assets/c4d1a49a-da40-4e1b-8fe1-4fc076a3da61" />

Dashboard 2 : 
<img width="3497" height="1945" alt="image" src="https://github.com/user-attachments/assets/87a10843-e224-4c39-b4e6-527a4c1bad60" />

Dashboard 3 : 
<img width="3497" height="1942" alt="image" src="https://github.com/user-attachments/assets/f014dbd4-39de-446c-9eae-0821452e827b" />



## 🤝 Auteurs

* **[lleuginer]** 

---

*Projet réalisé dans le cadre scolaire pour l'IPSA, école d'ingénieurs.*

---
