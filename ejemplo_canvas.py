import tkinter as tk

root = tk.Tk()
root.title("Ejemplo Completo de Tkinter Canvas")
root.geometry("850x700") # Tamaño de la ventana
root.configure(bg="#252525")
# 1. Crear el Widget Canvas
# área de dibujo. 
canvas = tk.Canvas(root, width=600, height=500, bg="#DFDFDF", bd=2, relief="sunken")
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
canvas.create_text(125, 40, text="Línea con flecha y guiones", font=("Arial", 9), fill="black")

# 3. Dibujar un Rectángulo
# create_rectangle(x1, y1, x2, y2, opciones)
# (x1,y1) es la esquina superior izquierda, (x2,y2) es la esquina inferior derecha.
rectangulo = canvas.create_rectangle(250, 50, 400, 120,
        fill="#14AC07",    # Color de relleno
        outline="darkgreen", # Color del borde
        width=2)         # Grosor del borde
canvas.create_text(325, 130, text="Rectángulo Relleno", font=("Arial", 9), fill="black")

# 4. Dibujar un Óvalo (o Círculo)
# create_oval(x1, y1, x2, y2, opciones)
# También definido por un rectángulo delimitador.
ovalo= canvas.create_oval(450, 50, 550, 150, # Un cuadrado delimitador para un círculo
        fill="red",
        outline="maroon",
        width=2)
canvas.create_text(500, 160, text="Círculo (Óvalo)", font=("Arial", 9), fill="black")

# 5. Dibujar un Polígono
# create_polygon(x1, y1, x2, y2, ..., opciones)
# Lista de coordenadas de los vértices. Se cierra automáticamente el polígono.
poligono= canvas.create_polygon(50, 200, 150, 200, 100, 280, # Coordenadas para un triángulo
    fill="purple",
    outline="darkviolet",
    width=3)
canvas.create_text(100, 290, text="Triángulo (Polígono)", font=("Arial", 9), fill="black")

# 6. Dibujar un Arco
# # create_arc(x1, y1, x2, y2, opciones)
# Definido por un rectángulo delimitador, ángulos de inicio y extensión, y estilo.
pedazo_de_arco = canvas.create_arc(250, 200, 400, 300,
    start=45, extent=180, # Empieza a 45 grados, se extiende 180
    fill="yellow",
    outline="orange",
    width=2,
    style=tk.PIESLICE) # Estilo: sector de pastel
canvas.create_text(325, 310, text="Arco (pedazo de pastel)", font=("Arial", 9), fill="black")

arco = canvas.create_arc(450, 200, 550, 300,
    start=0, extent=270,
    outline="blue",
    width=3,
    style=tk.ARC) # Estilo: solo el arco, sin relleno
canvas.create_text(500, 310, text="Arco (Solo Línea)", font=("Arial", 9), fill="black")

# 7. Dibujar Texto
# create_text(x, y, text="...", opciones)
# (x,y) es el punto de anclaje del texto (por defecto el centro).
texto_id = canvas.create_text(300, 350,
    text="¡Hola, Canvas! Este es un texto.",
    font=("Verdana", 16, "bold"),
    fill="navy",
    anchor=tk.CENTER) # El texto se centra en (300, 350)
    


# --- Controles para las Nuevas Funcionalidades ---

# Frame para agrupar los botones de manipulación
control_frame = tk.Frame(root, bg="#7A7070", bd=2, relief="groove", padx=10, pady=10)
control_frame.pack(pady=10)

tk.Label(control_frame, text="Manipulación de Objetos:", font=("Arial", 12, "bold"), fg="#EBEBEB", bg="#2C2525").pack(pady=5)

# 1. canvas.move(id_o_tag, dx, dy): Mueve un objeto una cantidad relativa. 
def mover_linea_derecha():
    canvas.move(linea, 10, 0) # Mueve la línea 10 píxeles a la derecha

def mover_linea_izquierda():
    canvas.move(linea, -10, 0) 


btn_mover_der = tk.Button(control_frame, text="Mover Línea Derecha", command=mover_linea_derecha)
btn_mover_der.pack(side=tk.LEFT, padx=5, pady=5)

btn_mover_izq = tk.Button(control_frame, text="Mover Línea Izquierda", command=mover_linea_izquierda)
btn_mover_izq.pack(side=tk.LEFT, padx=5, pady=5)


# 2. canvas.itemconfig(id_o_tag, **new_options): Cambia las opciones de visualización.
def alternar_color_rectangulo():
    # 3. canvas.itemcget(id_o_tag, "option"): Recupera el valor actual de una opción.
    current_fill = canvas.itemcget(rectangulo, "fill") # Obtener el color actual
    new_fill = "blue" if current_fill == "#14AC07" else "#14AC07"
    canvas.itemconfig(rectangulo, fill=new_fill, outline="navy", width=4) 

btn_cambiar_color = tk.Button(control_frame, text="Alternar Color Rectángulo", command=alternar_color_rectangulo)
btn_cambiar_color.pack(side=tk.LEFT, padx=5, pady=5)

# 4. canvas.coords(id_o_tag, *new_coordinates): Modifica las coordenadas.
# Esencial para redimensionamientos o posicionamientos absolutos.
def redimensionar_y_reubicar_poligono():
    # Coordenadas nuevas para hacerlo más grande y moverlo hacia abajo
    canvas.coords(poligono,# ID del polígono
                  50, 320, # Nuevo punto 1
                  200, 320,# Nuevo punto 2
                  125, 450)# Nuevo punto 3
    canvas.itemconfig(poligono, fill="cyan", outline="darkblue")

btn_redimensionar_poligono = tk.Button(control_frame, text="Redimensionar Polígono", command=redimensionar_y_reubicar_poligono)
btn_redimensionar_poligono.pack(side=tk.LEFT, padx=5, pady=5)

# 5. canvas.delete(id_o_tag_o_tk.ALL): Elimina objetos del Canvas.
def eliminar_arco():
    canvas.delete(arco) # Eliminar el arco por su tag
    canvas.create_text(300, 420, text="¡Arco Eliminado!", font=("Arial", 12, "bold"), fill="red")

def limpiar_todo_canvas():
    canvas.delete(tk.ALL) # Elimina TODOS los objetos del canvas

btn_eliminar_arco = tk.Button(control_frame, text="Eliminar Arco", command=eliminar_arco)
btn_eliminar_arco.pack(side=tk.LEFT, padx=5, pady=5)

btn_limpiar_todo = tk.Button(control_frame, text="Limpiar Todo el Canvas", command=limpiar_todo_canvas)
btn_limpiar_todo.pack(side=tk.LEFT, padx=5, pady=5)





root.mainloop()

