import matplotlib.pyplot as plt
import matplotlib.patches as patches

def graficar_mastermind(historial_mejores, codigo_objetivo):
    num_generaciones = len(historial_mejores)
    longitud = len(codigo_objetivo)
    
    #el mapa de colores reales
    color_map = {
        "RED": "#FF0000", "BLUE": "#0000FF", "YELLOW": "#FFFF00", 
        "GREEN": "#008000", "ORANGE": "#FFA500", "PURPLE": "#800080"
    }

    #tablero
    fig, ax = plt.subplots(figsize=(7, 10))
    fig.patch.set_facecolor('#63422B')
    ax.set_facecolor('#8B5A2B')

    #tablero bordes
    tablero_rect = patches.Rectangle((0.5, 0.5), longitud + 1, num_generaciones + 3, 
                                     linewidth=3, edgecolor='#432616', facecolor='#A0522D', zorder=1)
    ax.add_patch(tablero_rect)

    #Intentos
    y_inicio = num_generaciones + 2
    for gen_idx, individuo in enumerate(historial_mejores):
        y_pos = y_inicio - gen_idx
        
        #Dibujar los huecos de las fichas
        for i in range(longitud):
            hueco = plt.Circle((i + 1.5, y_pos), 0.42, color='#3E2723', zorder=2)
            ax.add_patch(hueco)
            
            #Dibujar la ficha 
            color_hex = color_map[individuo[i]]
            ficha = plt.Circle((i + 1.5, y_pos), 0.38, color=color_hex, ec='black', lw=1, zorder=3)
            ax.add_patch(ficha)
           

        #Etiqueta de generación
        ax.text(longitud + 2, y_pos, f"GEN {gen_idx:02d}", color='white', 
                va='center', fontweight='bold', family='monospace')

    #CÓDIGO SECRETO
    y_secreto = 1.5
    #Caja para el código objetivo
    caja_secreta = patches.Rectangle((0.8, y_secreto - 0.6), longitud + 0.4, 1.2, 
                                     facecolor='#4E342E', edgecolor='#212121', lw=2, zorder=5)
    ax.add_patch(caja_secreta)
    
    for i, color in enumerate(codigo_objetivo):
        color_hex = color_map[color]
        #Ficha objetivo
        ficha_obj = plt.Circle((i + 1.5, y_secreto), 0.4, color=color_hex, ec='white', lw=2, zorder=6)
        ax.add_patch(ficha_obj)
        

    ax.text(longitud / 2 + 1, y_secreto - 0.9, "CÓDIGO SECRETO", color='#FFD700',
            ha='center', fontweight='bold', fontsize=12)

    #Ajustes de visualización
    ax.set_xlim(0, longitud + 4)
    ax.set_ylim(0, num_generaciones + 5)
    ax.set_aspect('equal')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()