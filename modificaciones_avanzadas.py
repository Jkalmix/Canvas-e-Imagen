import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
import os

# --- FUNCIONES PARA LAS MANIPULACIONES AVANZADAS ---
def convertir_a_escala_grises(imagen_pil_original):
    """Convierte una imagen a escala de grises."""
    return imagen_pil_original.convert("L")

def aplicar_filtro_desenfoque(imagen_pil_original, radio_desenfoque=5):
    """Aplica un filtro de desenfoque Gaussiano."""
    return imagen_pil_original.filter(ImageFilter.GaussianBlur(radius=radio_desenfoque))

def aplicar_filtro_enfoque(imagen_pil_original):
    """Aplica un filtro de enfoque a la imagen."""
    return imagen_pil_original.filter(ImageFilter.SHARPEN)


# --- CONFIGURACIÓN DE LA INTERFAZ GRÁFICA ---
# Define la ruta de tu imagen.
ruta_del_archivo_imagen = "cowboy.jpg" 
referencias_de_imagenes_tk = [] 
tamano_mostrar_galeria = (200, 200)

# --- VENTANA PRINCIPAL ---
ventana_principal = tk.Tk()
ventana_principal.title("Galería de Modificaciones Avanzadas")

# MEJORA: Eliminamos geometry para que la ventana se ajuste sola al contenido.
# ventana_principal.geometry("900x800") 

try:
    imagen_pil_cargada = Image.open(ruta_del_archivo_imagen) 
    
    # --- INFO E IMAGEN ORIGINAL ---
    tk.Label(ventana_principal, text=f"Imagen '{os.path.basename(ruta_del_archivo_imagen)}' cargada.", fg="darkgreen").pack(pady=(10,0))
    tk.Label(ventana_principal, text=f"Tamaño original: {imagen_pil_cargada.size}").pack()
    tk.Label(ventana_principal, text="Imagen Original (redimensionada para mostrar):").pack(pady=(10,5))
    
    tamano_mostrar_imagen_principal = (350, 350)
    imagen_original_para_mostrar = imagen_pil_cargada.resize(tamano_mostrar_imagen_principal, Image.Resampling.LANCZOS)
    imagen_tk_original = ImageTk.PhotoImage(imagen_original_para_mostrar) 
    
    etiqueta_imagen_original = tk.Label(ventana_principal, image=imagen_tk_original) 
    etiqueta_imagen_original.pack(pady=10)
    etiqueta_imagen_original.image = imagen_tk_original
    referencias_de_imagenes_tk.append(imagen_tk_original)

    # --- GALERÍA DE MODIFICACIONES AVANZADAS ---
    tk.Label(ventana_principal, text="Modificaciones Avanzadas (Filtros)", fg="purple", font=("Arial", 14, "bold")).pack(pady=(10,0))
    
    marco_galeria = tk.Frame(ventana_principal, padx=10, pady=10) 
    marco_galeria.pack(pady=10)

    # 1. Imagen en Escala de Grises
    img_grises = convertir_a_escala_grises(imagen_pil_cargada)
    img_grises_viz = img_grises.resize(tamano_mostrar_galeria, Image.Resampling.LANCZOS)
    img_tk_grises = ImageTk.PhotoImage(img_grises_viz)
    cont_grises = tk.Frame(marco_galeria, bd=2, relief="groove")
    cont_grises.grid(row=0, column=0, padx=10, pady=10)
    tk.Label(cont_grises, image=img_tk_grises).pack(padx=5, pady=5)
    tk.Label(cont_grises, text="Escala de Grises", font=("Arial", 10)).pack(pady=(0, 5))
    referencias_de_imagenes_tk.append(img_tk_grises)

    # 2. Imagen con Desenfoque
    img_desenfocada = aplicar_filtro_desenfoque(imagen_pil_cargada, radio_desenfoque=8)
    img_desenfocada_viz = img_desenfocada.resize(tamano_mostrar_galeria, Image.Resampling.LANCZOS)
    img_tk_desenfocada = ImageTk.PhotoImage(img_desenfocada_viz)
    cont_desenfocada = tk.Frame(marco_galeria, bd=2, relief="groove")
    cont_desenfocada.grid(row=0, column=1, padx=10, pady=10)
    tk.Label(cont_desenfocada, image=img_tk_desenfocada).pack(padx=5, pady=5)
    tk.Label(cont_desenfocada, text="Desenfoque (Blur)", font=("Arial", 10)).pack(pady=(0, 5))
    referencias_de_imagenes_tk.append(img_tk_desenfocada)

    # 3. Imagen con Enfoque
    img_enfocada = aplicar_filtro_enfoque(imagen_pil_cargada)
    img_enfocada_viz = img_enfocada.resize(tamano_mostrar_galeria, Image.Resampling.LANCZOS)
    img_tk_enfocada = ImageTk.PhotoImage(img_enfocada_viz)
    cont_enfocada = tk.Frame(marco_galeria, bd=2, relief="groove")
    cont_enfocada.grid(row=0, column=2, padx=10, pady=10)
    tk.Label(cont_enfocada, image=img_tk_enfocada).pack(padx=5, pady=5)
    tk.Label(cont_enfocada, text="Enfoque (Sharpen)", font=("Arial", 10)).pack(pady=(0, 5))
    referencias_de_imagenes_tk.append(img_tk_enfocada)

except FileNotFoundError:
    messagebox.showerror("Error", f"No se encontró el archivo '{ruta_del_archivo_imagen}'.\nAsegúrate de que esté en la misma carpeta.")
except Exception as e:
    messagebox.showerror("Error Inesperado", f"Ocurrió un error al procesar la imagen: {e}")

# --- INICIAR BUCLE PRINCIPAL ---
ventana_principal.mainloop()
