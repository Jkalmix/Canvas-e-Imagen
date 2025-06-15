import tkinter as tk

root = tk.Tk()
root.title("Ejemplo Completo de Tkinter Canvas")
root.geometry("700x650") # Tamaño de la ventana
root.configure(bg="#2C2525")
# 1. Crear el Widget Canvas
# área de dibujo. 
canvas = tk.Canvas(root, width=600, height=500, bg="#EBEBEB", bd=2, relief="sunken")
canvas.pack(pady=20, padx=20) # Empaquetar el canvas en la ventana principal

# --- Creación de Objetos en el Canvas ---

# 2. Dibujar una Línea
# create_line(x1, y1, x2, y2, x3, y3, ... )
# Las coordenadas definen los puntos de la línea.
linea = canvas.create_line(50, 50, 200, 50, 200, 80, # De (50,50) a (200,50)
        fill="blue",     # Color de la línea
        width=3,         # Grosor de la línea
        arrow=tk.LAST,   # Flecha al final de la línea
        dash=(5, 3))     # Patrón de guiones (5px línea, 3px espacio)
canvas.create_text(125, 40, text="Línea con flecha y guiones", font=("Arial", 9), fill="gray")

# 3. Dibujar un Rectángulo
# create_rectangle(x1, y1, x2, y2, opciones)
# (x1,y1) es la esquina superior izquierda, (x2,y2) es la esquina inferior derecha.
rectangulo = canvas.create_rectangle(250, 50, 400, 120,
        fill="#14AC07",    # Color de relleno
        outline="darkgreen", # Color del borde
        width=2)         # Grosor del borde
canvas.create_text(325, 130, text="Rectángulo Relleno", font=("Arial", 9), fill="gray")

    # 4. Dibujar un Óvalo (o Círculo)
    # create_oval(x1, y1, x2, y2, opciones)
    # También definido por un rectángulo delimitador.
ovalo= canvas.create_oval(450, 50, 550, 150, # Un cuadrado delimitador para un círculo
        fill="red",
        outline="maroon",
        width=2)
canvas.create_text(500, 160, text="Círculo (Óvalo)", font=("Arial", 9), fill="gray")

# 5. Dibujar un Polígono
# create_polygon(x1, y1, x2, y2, ..., opciones)
# Lista de coordenadas de los vértices. Se cierra automáticamente el polígono.
poligono= canvas.create_polygon(50, 200, 150, 200, 100, 280, # Coordenadas para un triángulo
                                   fill="purple",
                                   outline="darkviolet",
                                   width=3)
canvas.create_text(100, 290, text="Triángulo (Polígono)", font=("Arial", 9), fill="gray")

    # 6. Dibujar un Arco
    # create_arc(x1, y1, x2, y2, opciones)
    # Definido por un rectángulo delimitador, ángulos de inicio y extensión, y estilo.
pedazo_de_arco = canvas.create_arc(250, 200, 400, 300,
                                        start=45, extent=180, # Empieza a 45 grados, se extiende 180
                                        fill="yellow",
                                        outline="orange",
                                        width=2,
                                        style=tk.PIESLICE) # Estilo: sector de pastel
canvas.create_text(325, 310, text="Arco (pedazo de pastel)", font=("Arial", 9), fill="gray")

arco = canvas.create_arc(450, 200, 550, 300,
                                    start=0, extent=270,
                                    outline="blue",
                                    width=3,
                                    style=tk.ARC) # Estilo: solo el arco, sin relleno
canvas.create_text(500, 310, text="Arco (Solo Línea)", font=("Arial", 9), fill="gray")

    # 7. Dibujar Texto
    # create_text(x, y, text="...", opciones)
    # (x,y) es el punto de anclaje del texto (por defecto el centro).
texto_id = canvas.create_text(300, 350,
                                 text="¡Hola, Canvas! Este es un texto.",
                                 font=("Verdana", 16, "bold"),
                                 fill="navy",
                                 anchor=tk.CENTER) # El texto se centra en (300, 350)
    


root.mainloop()


