import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
from PIL import Image, ImageTk 

# -------------------------
# FUNCIONES (pantallas vacías por ahora)
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Vinos y Licores\nProyecto Escolar\nVersión 1.0")

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Aromas del valle")
ventana.geometry("500x600")
ventana.resizable(False, False)
ventana.configure(bg="#7E221C")  # Fondo vino oscuro

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR, "ventas2025.png"))  # Cambiar si es necesario
    imagen = imagen.resize((250, 250))
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo)
    lbl_logo.pack(pady=20)
except:
    lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo del sistema)", font=("Arial", 14))
    lbl_sin_logo.pack(pady=40)

# -------------------------
# ESTILO DE BOTONES
# -------------------------
estilo = ttk.Style()
estilo.configure("TButton",
                 font=("Arial", 12),
                 padding=10,
                 background="#7E221C",
                 foreground="white")

# Forzar color en estado activo
estilo.map("TButton",
          background=[('active', '#ff7f7f')],
          foreground=[('active', 'white')])

# -------------------------
# ESTILO DE BOTONES
estilo = ttk.Style()
estilo.configure("TButton",
                 font=("Arial", 12),
                 padding=10,
                 background="#7a0026",  # Botón vino oscuro
                 foreground="#000000")

estilo.map("TButton",
          background=[('active', '#5c001d')],
          foreground=[('active', '#000000')])

# -------------------------
# BOTONES PRINCIPALES (todos mismo tamaño)
# -------------------------
btn_width = 25

btn_reg_prod = ttk.Button(ventana, text="Registro de Productos",  command=abrir_registro_productos)
btn_reg_prod.pack(pady=10)
btn_reg_prod.configure(width=btn_width)

btn_reg_ventas = ttk.Button(ventana, text="Registro de Ventas", command=abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)
btn_reg_ventas.configure(width=btn_width)

btn_reportes = ttk.Button(ventana, text="Reportes", command=abrir_reportes)
btn_reportes.pack(pady=10)
btn_reportes.configure(width=btn_width)

btn_acerca = ttk.Button(ventana, text="Acerca de", command=abrir_acerca_de)
btn_acerca.pack(pady=10)
btn_acerca.configure(width=btn_width)

ventana.mainloop()
