import tkinter as tk
from app.core.bot_logic import repondre
from app.core.utils import nettoyer_message
from app.config import APP_NAME

def lancer_fenetre():
    fenetre = tk.Tk()
    fenetre.title(APP_NAME)
    fenetre.geometry("400x450")
    fenetre.resizable(False, False)

    chat = tk.Text(fenetre, height=20, width=48, bg="#F7F7F7", fg="#222")
    chat.pack(padx=10, pady=10)

    entree = tk.Entry(fenetre, width=30)
    entree.pack(side=tk.LEFT, padx=(10, 0), pady=5)

    def envoyer():
        message = nettoyer_message(entree.get())
        if not message:
            return
        chat.insert(tk.END, f"🧑 Toi : {message}\n")
        entree.delete(0, tk.END)
        reponse = repondre(message)
        chat.insert(tk.END, f"🤖 Bot : {reponse}\n\n")

    bouton = tk.Button(fenetre, text="Envoyer", command=envoyer, bg="#0078D7", fg="white")
    bouton.pack(side=tk.LEFT, padx=5)

    fenetre.mainloop()
