import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk 

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
   reg = tk.Toplevel()
   reg.title("Registro de Productos")
   reg.geometry("400x400")
   reg.resizable(False, False)

   # --- Etiquetas y Campos de Texto ---
   lbl_id = tk.Label(reg, text="ID del Producto:", font=("Arial", 12))
   lbl_id.pack(pady=5)
   txt_id = tk.Entry(reg, font=("Arial", 12))
   txt_id.pack(pady=5)
   lbl_desc = tk.Label(reg, text="Descripción:", font=("Arial", 12))
   lbl_desc.pack(pady=5)
   txt_desc = tk.Entry(reg, font=("Arial", 12))
   txt_desc.pack(pady=5)
   lbl_precio = tk.Label(reg, text="Precio:", font=("Arial", 12))
   lbl_precio.pack(pady=5)
   txt_precio = tk.Entry(reg, font=("Arial", 12))
   txt_precio.pack(pady=5)
   lbl_categoria = tk.Label(reg, text="Categoría:", font=("Arial", 12))
   lbl_categoria.pack(pady=5)
   txt_categoria = tk.Entry(reg, font=("Arial", 12))
   txt_categoria.pack(pady=5)

   # --- Función para guardar ---
   def guardar_producto():
      id_prod = txt_id.get().strip()
      descripcion = txt_desc.get().strip()
      precio = txt_precio.get().strip()
      categoria = txt_categoria.get().strip()
      # Validaciones
      if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
         messagebox.showwarning("Campos Vacíos", "Por favor complete todos los campos.")
         return
      # Validar precio como número
      try:
         float(precio)
      except:
         messagebox.showerror("Error", "El precio debe ser un número.")
         return

      # Guardar en archivo de texto
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivo = os.path.join(BASE_DIR,"productos.txt")
      with open(archivo, "a", encoding="utf-8") as archivo:
         archivo.write(f"{id_prod}|{descripcion}|{precio}|{categoria}\n")
         messagebox.showinfo("Guardado", "Producto registrado correctamente.")
         # Limpiar campos
         txt_id.delete(0, tk.END)
         txt_desc.delete(0, tk.END)
         txt_precio.delete(0, tk.END)
         txt_categoria.delete(0, tk.END)
   # --- Botón Guardar ---
   btn_guardar = tk.Button(reg, text="Guardar Producto", command=guardar_producto)
   btn_guardar.pack(pady=20)

def abrir_registro_ventas():
   ven = tk.Toplevel()
   ven.title("Registro de Ventas")
   ven.geometry("420x430")
   ven.resizable(False, False)
   # ------------------------------------
   # Cargar productos desde productos.txt
   # ------------------------------------
   productos = {}
   try:
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivof = os.path.join(BASE_DIR,"productos.txt")
      with open(archivof, "r", encoding="utf-8") as archivo:
         for linea in archivo:
            partes = linea.strip().split("|")
            if len(partes) == 4:
               idp, desc, precio, cat = partes
               productos[desc] = float(precio)
   except FileNotFoundError:
      messagebox.showerror("Error", "No se encontró el archivo productos.txt")
      ven.destroy()
      return

   # Lista de nombres de productos
   lista_productos = list(productos.keys())
   # ------------------------------------
   # CONTROLES VISUALES
   # ------------------------------------
   lbl_prod = tk.Label(ven, text="Producto:", font=("Arial", 12))
   lbl_prod.pack(pady=5)
   cb_producto = ttk.Combobox(ven, values=lista_productos, font=("Arial", 12), state="readonly")
   cb_producto.pack(pady=5)
   lbl_precio = tk.Label(ven, text="Precio:", font=("Arial", 12))
   lbl_precio.pack(pady=5)
   txt_precio = tk.Entry(ven, font=("Arial", 12), state="readonly")
   txt_precio.pack(pady=5)
   lbl_cantidad = tk.Label(ven, text="Cantidad:", font=("Arial", 12))
   lbl_cantidad.pack(pady=5)
   cantidad_var = tk.StringVar(ven)
   ven.cantidad_var = cantidad_var   # importante: mantiene la referencia
   txt_cantidad = tk.Entry(ven, font=("Arial", 12), textvariable=cantidad_var)
   txt_cantidad.pack(pady=5)  
   cantidad_var.trace_add("write", lambda *args: calcular_total())
   lbl_total = tk.Label(ven, text="Total:", font=("Arial", 12))
   lbl_total.pack(pady=5)
   txt_total = tk.Entry(ven, font=("Arial", 12), state="readonly")
   txt_total.pack(pady=5)
   # ------------------------------------
   # FUNCIONES
   # ------------------------------------
   def actualizar_precio(event):      
      prod = cb_producto.get()
      if prod in productos:
         txt_precio.config(state="normal")
         txt_precio.delete(0, tk.END)
         txt_precio.insert(0, productos[prod])
         txt_precio.config(state="readonly")
         calcular_total()
   def calcular_total(*args):      
      try:
         cant = int(txt_cantidad.get())
         precio = float(txt_precio.get())
         total = cant * precio
         txt_total.config(state="normal")
         txt_total.delete(0, tk.END)
         txt_total.insert(0, total)
         txt_total.config(state="readonly")
      except:
         # Si no hay número válido, limpiar el total
         txt_total.config(state="normal")
         txt_total.delete(0, tk.END)
         txt_total.config(state="readonly")
   def registrar_venta():
      prod = cb_producto.get()
      precio = txt_precio.get()
      cant = txt_cantidad.get()
      total = txt_total.get()
      if prod == "" or precio == "" or cant == "" or total == "":
         messagebox.showwarning("Campos Vacíos", "Todos los campos deben estar completos.")
         return
      # Guardar venta
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivov = os.path.join(BASE_DIR,"ventas.txt")
      with open(archivov, "a", encoding="utf-8") as archivo:
         archivo.write(f"{prod}|{precio}|{cant}|{total}\n")
         messagebox.showinfo("Venta Registrada", "La venta se registró correctamente.")
      # Limpiar campos
      cb_producto.set("")
      txt_precio.config(state="normal"); txt_precio.delete(0, tk.END); txt_precio.config(state="readonly")
      txt_cantidad.delete(0, tk.END)
      txt_total.config(state="normal"); txt_total.delete(0, tk.END); txt_total.config(state="readonly")
   # ------------------------------------
   # EVENTOS Y BOTÓN
   # ------------------------------------
   cb_producto.bind("<<ComboboxSelected>>", actualizar_precio)
   btn_guardar = ttk.Button(ven, text="Registrar Venta", command=registrar_venta)
   btn_guardar.pack(pady=25)

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Vinos y Licores\nProyecto Escolar\nVersión 1.0")


# -------------------------
# CREAR BOTÓN REDONDEADO
# -------------------------
def boton_redondeado(ventana, texto, comando):
    canvas = tk.Canvas(ventana, width=260, height=50, bg="#83150D", highlightthickness=0)
    canvas.pack(pady=10)

    # Dibujar botón redondeado
    radius = 20
    x1, y1, x2, y2 = 5, 5, 255, 45

    canvas.create_round_rect = canvas.create_arc

    # Fondo negro redondeado
    canvas.create_arc(x1, y1, x1 + radius*2, y1 + radius*2, start=90, extent=90, fill="black", outline="")
    canvas.create_arc(x2 - radius*2, y1, x2, y1 + radius*2, start=0, extent=90, fill="black", outline="")
    canvas.create_arc(x1, y2 - radius*2, x1 + radius*2, y2, start=180, extent=90, fill="black", outline="")
    canvas.create_arc(x2 - radius*2, y2 - radius*2, x2, y2, start=270, extent=90, fill="black", outline="")
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill="black", outline="")
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill="black", outline="")

    # Texto del botón
    canvas.create_text(130, 25, text=texto, fill="white", font=("Arial", 12, "bold"))

    # Zona clickable
    canvas.bind("<Button-1>", lambda e: comando())
    return canvas


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Aromas del valle")
ventana.geometry("500x600")
ventana.resizable(False, False)
ventana.configure(bg="#83150D")  # Fondo vino oscuro

# -------------------------
# LOGO SIN BORDE BLANCO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img = Image.open(os.path.join(BASE_DIR, "ventas2025.png")).convert("RGBA")
    img = img.resize((250, 250))

    # Convertir blanco a transparente
    datos = img.getdata()
    nueva = []
    for item in datos:
        if item[:3] == (255, 255, 255):  # si es blanco
            nueva.append((255, 255, 255, 0))  # hacerlo transparente
        else:
            nueva.append(item)
    img.putdata(nueva)

    img_logo = ImageTk.PhotoImage(img)
    lbl_logo = tk.Label(ventana, image=img_logo, bg="#83150D")
    lbl_logo.pack(pady=20)

except:
    lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo del sistema)", font=("Arial", 14), bg="#7E221C", fg="white")
    lbl_sin_logo.pack(pady=40)


# -------------------------
# BOTONES REDONDEADOS
# -------------------------
boton_redondeado(ventana, "Registro de Productos", abrir_registro_productos)
boton_redondeado(ventana, "Registro de Ventas", abrir_registro_ventas)
boton_redondeado(ventana, "Reportes", abrir_reportes)
boton_redondeado(ventana, "Acerca de", abrir_acerca_de)


ventana.mainloop()
