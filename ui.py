import tkinter as tk
from bot import repondre

def lancer_ui():
    fenetre = tk.Tk()
    fenetre.title("Mon Bot 🤖")
    fenetre.geometry("400x400")

    chat = tk.Text(fenetre, height=15, width=48, bg="#F0F0F0")
    chat.pack(padx=10, pady=10)

    entree = tk.Entry(fenetre, width=30)
    entree.pack(side=tk.LEFT, padx=(10, 0), pady=5)

    def envoyer():
        message = entree.get()
        if not message.strip():
            return
        chat.insert(tk.END, f"Toi : {message}\n")
        chat.insert(tk.END, repondre(message) + "\n")
        entree.delete(0, tk.END)

    bouton = tk.Button(fenetre, text="Envoyer", command=envoyer, bg="#0078D7", fg="white")
    bouton.pack(side=tk.LEFT, padx=5)

    fenetre.mainloop()