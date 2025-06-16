import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# --- FUNCIONES PARA LAS MANIPULACIONES BÁSICAS DE IMAGEN ---
def redimensionar_imagen(imagen_pil_original, nuevo_ancho_px, nuevo_alto_px):
    """Redimensiona una imagen a las dimensiones especificadas."""
    return imagen_pil_original.resize((nuevo_ancho_px, nuevo_alto_px))

def rotar_imagen(imagen_pil_original, grados_de_rotacion):
    """Rota una imagen. expand=True ajusta el tamaño para que no se corte."""
    # CORRECCIÓN: Ahora la función usa el parámetro que se le pasa.
    return imagen_pil_original.rotate(grados_de_rotacion, expand=True)

def recortar_imagen(imagen_pil_original, coordenadas_caja_recorte):
    """Recorta una porción rectangular de la imagen."""
    return imagen_pil_original.crop(coordenadas_caja_recorte)

# --- CONFIGURACIÓN DE LA INTERFAZ GRÁFICA ---
# Define la ruta de tu imagen.
ruta_del_archivo_imagen = "cowboy.jpg" 
referencias_de_imagenes_tk = [] 
tamano_mostrar_galeria = (200, 200)

# --- VENTANA PRINCIPAL ---
ventana_principal = tk.Tk()
ventana_principal.title("Galería de Modificaciones Básicas")

# MEJORA: Eliminamos geometry para que la ventana se ajuste sola al contenido.
# ventana_principal.geometry("900x800") 

try:
    imagen_pil_cargada = Image.open(ruta_del_archivo_imagen) 
    
    # --- INFO E IMAGEN ORIGINAL ---
    tk.Label(ventana_principal, text=f"Imagen '{os.path.basename(ruta_del_archivo_imagen)}' cargada.", fg="darkgreen").pack(pady=(10,0))
    tk.Label(ventana_principal, text=f"Tamaño original: {imagen_pil_cargada.size}").pack()
    tk.Label(ventana_principal, text="Imagen Original (redimensionada para mostrar):").pack(pady=(10,5))
    
    tamano_mostrar_imagen_principal = (350, 350)
    imagen_original_para_mostrar = imagen_pil_cargada.resize(tamano_mostrar_imagen_principal)
    imagen_tk_original = ImageTk.PhotoImage(imagen_original_para_mostrar) 
    
    etiqueta_imagen_original = tk.Label(ventana_principal, image=imagen_tk_original) 
    etiqueta_imagen_original.pack(pady=10)
    etiqueta_imagen_original.image = imagen_tk_original
    referencias_de_imagenes_tk.append(imagen_tk_original)

    # --- GALERÍA DE MODIFICACIONES BÁSICAS ---
    tk.Label(ventana_principal, text="Modificaciones Básicas", fg="blue", font=("Arial", 14, "bold")).pack(pady=(10,0))
    
    marco_galeria = tk.Frame(ventana_principal, padx=10, pady=10) 
    marco_galeria.pack(pady=10)

    # 1. Imagen Redimensionada
    img_redim = redimensionar_imagen(imagen_pil_cargada, 200, 200) 
    img_tk_redim = ImageTk.PhotoImage(img_redim) 
    cont_redim = tk.Frame(marco_galeria, bd=2, relief="groove") 
    cont_redim.grid(row=0, column=0, padx=10, pady=10)
    tk.Label(cont_redim, image=img_tk_redim).pack(padx=5, pady=5)
    tk.Label(cont_redim, text="Resize (200x200)", font=("Arial", 10)).pack(pady=(0, 5))
    referencias_de_imagenes_tk.append(img_tk_redim)

    # 2. Imagen Rotada
    img_rotada = rotar_imagen(imagen_pil_cargada, 45) # Rotamos 45 grados
    img_rotada_viz = img_rotada.resize(tamano_mostrar_galeria) 
    img_tk_rotada = ImageTk.PhotoImage(img_rotada_viz) 
    cont_rotada = tk.Frame(marco_galeria, bd=2, relief="groove") 
    cont_rotada.grid(row=0, column=1, padx=10, pady=10)
    tk.Label(cont_rotada, image=img_tk_rotada).pack(padx=5, pady=5)
    tk.Label(cont_rotada, text="Rotar (45°)", font=("Arial", 10)).pack(pady=(0, 5))
    referencias_de_imagenes_tk.append(img_tk_rotada)

    # 3. Imagen Recortada (50% Central)
    ancho, alto = imagen_pil_cargada.size
    caja = (ancho // 4, alto // 4, ancho * 3 // 4, alto * 3 // 4)
    img_recortada = recortar_imagen(imagen_pil_cargada, caja) 
    img_recortada_viz = img_recortada.resize(tamano_mostrar_galeria, Image.Resampling.LANCZOS)
    img_tk_recortada = ImageTk.PhotoImage(img_recortada_viz) 
    cont_recortada = tk.Frame(marco_galeria, bd=2, relief="groove") 
    cont_recortada.grid(row=0, column=2, padx=10, pady=10)
    tk.Label(cont_recortada, image=img_tk_recortada).pack(padx=5, pady=5)
    tk.Label(cont_recortada, text="Recortar (Centro)", font=("Arial", 10)).pack(pady=(0, 5))
    referencias_de_imagenes_tk.append(img_tk_recortada)

except FileNotFoundError:
    messagebox.showerror("Error", f"No se encontró el archivo '{ruta_del_archivo_imagen}'.\nAsegúrate de que esté en la misma carpeta.")
except Exception as e:
    messagebox.showerror("Error Inesperado", f"Ocurrió un error al procesar la imagen: {e}")

# --- INICIAR BUCLE PRINCIPAL ---
ventana_principal.mainloop()
