import matplotlib.pyplot as plt
import numpy as np

# Define la forma del corazón usando ecuaciones paramétricas
t = np.linspace(0, 2 * np.pi, 500)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Desplazamiento para la "sombra"
offset = 0.5
x_shadow = x - offset
y_shadow = y - offset

# Color negro y un gris oscuro para la sombra
color_negro = '#000000'
color_sombra = '#333333'
color_texto = '#000000'  # Color negro para el texto

# Nombre a agregar
nombre = "Nicole"

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(6, 7))  # Aumentamos un poco la altura para el texto

# Dibujar la "sombra" del corazón primero
ax.fill(x_shadow, y_shadow, color=color_sombra, alpha=0.6)

# Dibujar el corazón negro encima
ax.fill(x, y, color=color_negro)

# Agregar el texto "Nicole" en la parte inferior
min_y = min(y_shadow) - 2  # Ajustamos la posición vertical del texto
ax.text(0, min_y, nombre, fontsize=20, color=color_texto, ha='center', va='top')

# Ajustar los límites de los ejes
ax.set_xlim(min(x_shadow) - 1, max(x) + 1)
ax.set_ylim(min_y - 1, max(y) + 1)

# Desactivar los ejes
ax.axis('off')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

