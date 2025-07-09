import matplotlib.pyplot as plt

nombre = "Andrea"
colores = ['red', 'green', 'blue', 'purple', 'orange', 'cyan']

fig, ax = plt.subplots(figsize=(8, 2))
ax.axis('off')

x_pos = 0
for i, letra in enumerate(nombre):
    color = colores[i % len(colores)]
    t = ax.text(x_pos, 0.5, letra, fontsize=60, color=color, ha='left', va='center')
    bbox = t.get_window_extent(renderer=fig.canvas.get_renderer())
    x_pos_pixels = bbox.x1
    x_pos_data = ax.transData.inverted().transform((x_pos_pixels, 0))[0]
    x_pos = x_pos_data

plt.tight_layout()
plt.show()

