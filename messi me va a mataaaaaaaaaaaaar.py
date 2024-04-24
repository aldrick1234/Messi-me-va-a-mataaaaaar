import tkinter as tk
from tkinter import messagebox

# Define los mensajes que quieres mostrar
messages = [
    "Messi me va a mataaaaar",
    "En un bosque de sal",
    "La grasa me salvo",
    "Solito hiba a nacer",
    "Solito me paso",
    "Solo con arena y mar",
    "Comi papel y sal"
]

# Crea una ventana oculta
root = tk.Tk()
root.withdraw()

# Muestra los mensajes emergentes
for message in messages:
    messagebox.showinfo("XD", message)
