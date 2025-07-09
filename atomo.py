#En el siguiente proyecto se busca mostrar la estructura basica de un àtomo

#importamos librerias correspondientes

import tkinter as tk
from tkinter import ttk # Para botones con mejor estilo
import math # Necesario para la función sin() en la animación de la cuerda

# --- 1. Definición de la Clase Principal: AtomVisualizer ---
# Una clase es como un "plano" para crear objetos.
# Aquí, AtomVisualizer es el plano para nuestra aplicación de ventana.
class AtomVisualizer:
    # --- 1.1 Constructor de la Clase (__init__) ---
    # Se ejecuta automáticamente cuando creas una nueva instancia de AtomVisualizer.
    # Aquí se inicializa la ventana y sus componentes principales.
    def __init__(self, master):
        self.master = master # 'master' es la ventana principal de Tkinter (root).
        master.title("Visualizador de Átomo: Átomo") # Establece el título de la ventana.
        master.geometry("800x650") # Define el tamaño inicial de la ventana (ancho x alto).
        master.resizable(False, False) # Impide que el usuario cambie el tamaño de la ventana.
        master.configure(bg="#222") # Establece el color de fondo de la ventana principal.

        self.current_level = 0 # Variable para rastrear el nivel de visualización actual (0 = Átomo, 1 = Núcleo, etc.).
        # Lista de funciones, cada una representa un nivel de visualización diferente.
        # Esto permite cambiar el contenido mostrado llamando a la función correspondiente.
        self.levels = [
            self._create_level_atom,
            self._create_level_nucleus,
            self._create_level_subatomic,
            self._create_level_string
        ]

        # --- 1.2 Configuración del Lienzo (Canvas) ---
        # El Canvas es el área de dibujo principal de la aplicación.
        self.canvas = tk.Canvas(master, width=700, height=400, bg="#333", bd=0, highlightthickness=0)
        self.canvas.pack(pady=20) # 'pack()' organiza el widget en la ventana. 'pady' añade espacio vertical.

        # --- 1.3 Etiquetas para Título y Descripción ---
        # Widgets 'Label' para mostrar texto dinámico (título del nivel y su descripción).
        self.title_label = ttk.Label(master, text="", font=("Arial", 20, "bold"), background="#222", foreground="#00bcd4")
        self.title_label.pack(pady=(0, 10)) # Posiciona la etiqueta.

        self.description_label = ttk.Label(master, text="", font=("Arial", 12), wraplength=700, justify="center", background="#222", foreground="#eee")
        self.description_label.pack(pady=(0, 15))

        # --- 1.4 Frame para los Botones de Navegación ---
        # Un 'Frame' es un contenedor que ayuda a organizar otros widgets (en este caso, los botones).
        self.button_frame = ttk.Frame(master, style="TFrame")
        self.button_frame.pack(pady=10)

        # --- 1.5 Estilo de los Botones (ttk.Style) ---
        # 'ttk.Style' permite personalizar la apariencia de los widgets ttk.
        # Configura la fuente, el relleno, el color de fondo y el color al pasar el ratón.
        style = ttk.Style()
        style.configure("TButton",
                        font=("Arial", 12),
                        padding=10,
                        background="#4CAF50", # Color verde para el fondo del botón.
                        foreground="white", # Color del texto.
                        relief="flat") # Estilo plano, sin relieve.
        style.map("TButton",
                  background=[('active', '#45a049')]) # Cambia el color de fondo cuando el botón está activo (ratón encima/presionado).

        style.configure("TFrame", background="#222") # Estilo para el frame de los botones.

        # --- 1.6 Creación de los Botones ---
        # 'ttk.Button' crea los botones "Anterior" y "Siguiente".
        # 'command' especifica la función que se llama al hacer clic.
        self.prev_button = ttk.Button(self.button_frame, text="Anterior", command=self.show_previous_level)
        self.next_button = ttk.Button(self.button_frame, text="Siguiente", command=self.show_next_level)

        # Posiciona los botones dentro de su 'button_frame'.
        self.prev_button.pack(side=tk.LEFT, padx=10) # 'side=tk.LEFT' los alinea a la izquierda.
        self.next_button.pack(side=tk.RIGHT, padx=10) # 'side=tk.RIGHT' los alinea a la derecha.

        # --- 1.7 Mostrar el Nivel Inicial ---
        self.show_level(self.current_level) # Llama a esta función para mostrar el primer nivel al iniciar la app.

    # --- 2. Métodos de Navegación y Control ---

    # --- 2.1 Limpiar el Canvas ---
    # Elimina todos los elementos dibujados actualmente en el lienzo.
    def _clear_canvas(self):
        self.canvas.delete("all") # "all" indica que borre todos los elementos.

    # --- 2.2 Mostrar un Nivel Específico ---
    # Controla qué nivel de visualización se muestra.
    def show_level(self, level_index):
        self.current_level = level_index # Actualiza el índice del nivel actual.
        self._clear_canvas() # Borra lo que estaba dibujado antes.
        self.levels[self.current_level]() # Llama a la función del nivel correspondiente para dibujarlo.
        self._update_buttons() # Actualiza el estado de los botones (habilitado/deshabilitado).

    # --- 2.3 Navegar al Siguiente Nivel ---
    # Incrementa el índice del nivel y llama a 'show_level' si no es el último.
    def show_next_level(self):
        if self.current_level < len(self.levels) - 1: # Si no estamos en el último nivel...
            self.show_level(self.current_level + 1) # ...avanza al siguiente.

    # --- 2.4 Navegar al Nivel Anterior ---
    # Decrementa el índice del nivel y llama a 'show_level' si no es el primero.
    def show_previous_level(self):
        if self.current_level > 0: # Si no estamos en el primer nivel...
            self.show_level(self.current_level - 1) # ...regresa al anterior.

    # --- 2.5 Actualizar el Estado de los Botones ---
    # Deshabilita los botones "Anterior" o "Siguiente" si se llega al principio o al final de los niveles.
    def _update_buttons(self):
        if self.current_level == 0:
            self.prev_button.config(state=tk.DISABLED) # Deshabilita el botón "Anterior".
        else:
            self.prev_button.config(state=tk.NORMAL) # Lo habilita.

        if self.current_level == len(self.levels) - 1:
            self.next_button.config(state=tk.DISABLED) # Deshabilita el botón "Siguiente".
        else:
            self.next_button.config(state=tk.NORMAL) # Lo habilita.

    # --- 3. Funciones de Dibujo para Cada Nivel de Visualización ---
    # Cada una de estas funciones es responsable de dibujar los elementos
    # específicos para un determinado nivel de la estructura del átomo.

    # --- 3.1 Dibujar el Nivel "El Átomo" ---
    def _create_level_atom(self):
        self.title_label.config(text="1. El Átomo") # Actualiza el título.
        self.description_label.config(text="El átomo, la unidad básica de la materia, con un núcleo central y electrones orbitando.") # Actualiza la descripción.

        center_x, center_y = 350, 200 # Coordenadas centrales para el dibujo.

        # Núcleo (círculo rojo grande)
        # 'create_oval' dibuja una elipse o un círculo (si el ancho y alto son iguales).
        # Los parámetros son (x1, y1, x2, y2) para la caja delimitadora, y luego opciones de estilo.
        self.canvas.create_oval(center_x - 50, center_y - 50, center_x + 50, center_y + 50,
                                fill="#f44336", outline="#d32f2f", width=2, tags="atom_element")

        # Órbitas de electrones (líneas punteadas, elípticas para variedad)
        self.canvas.create_oval(center_x - 120, center_y - 80, center_x + 120, center_y + 80,
                                outline="#03a9f4", dash=(5, 3), width=2, tags="atom_element") # 'dash' hace la línea punteada.
        self.canvas.create_oval(center_x - 80, center_y - 120, center_x + 80, center_y + 120,
                                outline="#8bc34a", dash=(5, 3), width=2, tags="atom_element")

        # Electrones (círculos pequeños en las órbitas, estáticos)
        self.canvas.create_oval(center_x - 125, center_y - 5, center_x - 115, center_y + 5, fill="#ffeb3b", outline="#ffc107", tags="atom_element")
        self.canvas.create_oval(center_x + 115, center_y - 5, center_x + 125, center_y + 5, fill="#ffeb3b", outline="#ffc107", tags="atom_element")
        self.canvas.create_oval(center_x - 5, center_y - 125, center_x + 5, center_y - 115, fill="#ffeb3b", outline="#ffc107", tags="atom_element")
        self.canvas.create_oval(center_x - 5, center_y + 115, center_x + 5, center_y + 125, fill="#ffeb3b", outline="#ffc107", tags="atom_element")

    # --- 3.2 Dibujar el Nivel "El Núcleo: Protones y Neutrones" ---
    def _create_level_nucleus(self):
        self.title_label.config(text="2. El Núcleo: Protones y Neutrones")
        self.description_label.config(text="El núcleo atómico está compuesto por protones (carga positiva) y neutrones (sin carga).")

        center_x, center_y = 350, 200

        # Datos de las partículas para dibujar.
        particles = [
            {"type": "P", "color": "#e91e63"}, # Púrpura rojizo para protón.
            {"type": "N", "color": "#607d8b"}, # Gris azulado para neutrón.
            {"type": "P", "color": "#e91e63"},
            {"type": "N", "color": "#607d8b"},
            {"type": "P", "color": "#e91e63"}
        ]

        # Offsets para posicionar cada partícula alrededor del centro, simulando una aglomeración.
        offsets = [(-30, -20), (20, -10), (-10, 30), (40, 20), (-40, 10)]
        for i, p in enumerate(particles): # Itera sobre la lista de partículas.
            # Dibuja el círculo de la partícula.
            self.canvas.create_oval(center_x + offsets[i][0] - 25, center_y + offsets[i][1] - 25,
                                    center_x + offsets[i][0] + 25, center_y + offsets[i][1] + 25,
                                    fill=p["color"], outline="#555", width=1, tags="nucleus_element")
            # Dibuja el texto (P o N) en el centro de la partícula.
            self.canvas.create_text(center_x + offsets[i][0], center_y + offsets[i][1],
                                    text=p["type"], fill="white", font=("Arial", 16, "bold"), tags="nucleus_element")

    # --- 3.3 Dibujar el Nivel "Partículas Subatómicas: Quarks y Leptones" ---
    def _create_level_subatomic(self):
        self.title_label.config(text="3. Partículas Subatómicas: Quarks y Leptones")
        self.description_label.config(text="Protones y neutrones están formados por Quarks. Los electrones son Leptones fundamentales.")

        # Texto explicativo para Quarks.
        self.canvas.create_text(350, 100, text="Quarks (dentro de Protones/Neutrones)", font=("Arial", 14, "bold"), fill="#9c27b0", tags="subatomic_element")
        # Rectángulos para representar Quarks Up y Down de forma abstracta.
        self.canvas.create_rectangle(150, 130, 250, 180, fill="#9c27b0", outline="#7b1fa2", width=2, tags="subatomic_element")
        self.canvas.create_text(200, 155, text="Quark Up", fill="white", font=("Arial", 10), tags="subatomic_element")
        self.canvas.create_rectangle(270, 130, 370, 180, fill="#9c27b0", outline="#7b1fa2", width=2, tags="subatomic_element")
        self.canvas.create_text(320, 155, text="Quark Down", fill="white", font=("Arial", 10), tags="subatomic_element")

        # Texto explicativo para Leptones.
        self.canvas.create_text(350, 250, text="Leptones (ej. Electrón)", font=("Arial", 14, "bold"), fill="#ff9800", tags="subatomic_element")
        # Círculo para representar un Electrón de forma abstracta.
        self.canvas.create_oval(250, 280, 350, 330, fill="#ff9800", outline="#f57c00", width=2, tags="subatomic_element")
        self.canvas.create_text(300, 305, text="Electrón", fill="white", font=("Arial", 10), tags="subatomic_element")


    # --- 3.4 Dibujar el Nivel "La Cuerda!" ---
    def _create_level_string(self):
        self.title_label.config(text="4. ¡La Cuerda!")
        self.description_label.config(text="Según la Teoría de Cuerdas, todas las partículas fundamentales son en realidad diminutas cuerdas vibrantes de energía.")

        center_x, center_y = 350, 200

        # Dibuja una línea para representar la cuerda.
        self.string_line = self.canvas.create_line(center_x - 100, center_y, center_x + 100, center_y,
                                                    fill="white", width=4, tags="string_element")
        # Inicia la animación de la cuerda.
        self.animate_string(self.string_line, 0) # Llama a la función de animación con la ID de la línea y una fase inicial.


    # --- 3.5 Función de Animación para la Cuerda ---
    # Esta función se llama repetidamente para crear la ilusión de movimiento.
    def animate_string(self, item_id, phase):
        # Obtiene las coordenadas actuales de la línea.
        x1, y1, x2, y2 = self.canvas.coords(item_id)
        amplitude = 15 # Qué tan alto/bajo vibrará la cuerda.
        frequency = 0.05 # Qué tan rápido cambiará la vibración.

        # Calcula las nuevas posiciones Y para los extremos de la línea usando la función seno.
        # La función seno crea un movimiento ondulante suave.
        new_y1 = y1 + amplitude * (math.sin(phase * frequency))
        new_y2 = y2 + amplitude * (math.sin((phase + 10) * frequency)) # Se añade un desfase para que vibren ligeramente diferentes.

        # Actualiza las coordenadas de la línea en el lienzo.
        self.canvas.coords(item_id, x1, new_y1, x2, new_y2)

        # 'self.master.after()' programa esta misma función para ejecutarse de nuevo después de 50 milisegundos.
        # Esto crea un bucle de animación.
        self.master.after(50, self.animate_string, item_id, phase + 1) # 'phase + 1' cambia la fase para el siguiente fotograma.

# --- 4. Bloque de Ejecución Principal ---
# Este bloque de código se ejecuta solo cuando el script se corre directamente (no cuando se importa).
if __name__ == "__main__":
    root = tk.Tk() # Crea la ventana principal de Tkinter. Este es el objeto 'master' que pasamos a AtomVisualizer.
    app = AtomVisualizer(root) # Crea una instancia de nuestra aplicación AtomVisualizer, pasándole la ventana principal.
    root.mainloop() # Inicia el bucle principal de eventos de Tkinter.
                    # Mantiene la ventana abierta y responde a las interacciones del usuario (clics de botón, etc.).


                    

