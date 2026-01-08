import matplotlib.pyplot as plt
import matplotlib.patches as patches

from parametros import parametros

_, maxGeneraciones, _, _, _, _ = parametros() 

def graficarMastermind(historialMejores, codigoObjetivo, exito=True):
    maxFilas = maxGeneraciones 
    longitud = len(codigoObjetivo)
    
    colorMap = {
        "RED": "#FF0000", "BLUE": "#0000FF", "YELLOW": "#FFFF00", 
        "GREEN": "#008000", "ORANGE": "#FFA500", "PURPLE": "#800080"
    }

    fig, ax = plt.subplots(figsize=(7, 10))
    fig.patch.set_facecolor('#63422B')
    ax.set_facecolor('#8B5A2B')

    tableroRect = patches.Rectangle((0.5, 0.5), longitud + 1, maxFilas + 3, 
                                     linewidth=3, edgecolor='#432616', facecolor='#A0522D', zorder=1)
    ax.add_patch(tableroRect)

    yInicio = maxFilas + 2
    
    for filaIdx in range(maxFilas):
        yPos = yInicio - filaIdx
        
        for i in range(longitud):
            hueco = plt.Circle((i + 1.5, yPos), 0.42, color='#3E2723', zorder=2)
            ax.add_patch(hueco)
            
            if filaIdx < len(historialMejores):
                individuo = historialMejores[filaIdx]
                colorHex = colorMap[individuo[i]]
                ficha = plt.Circle((i + 1.5, yPos), 0.38, color=colorHex, ec='black', lw=1, zorder=3)
                ax.add_patch(ficha)

        ax.text(longitud + 2, yPos, f"GEN {filaIdx:02d}", color='white', 
                va='center', fontweight='bold', family='monospace')

    if not exito:
        ax.text(longitud / 2 + 1, maxFilas + 4, "MÁXIMO ALCANZADO", 
                color='#FF3D00', ha='center', fontsize=16, fontweight='black',
                bbox=dict(facecolor='black', alpha=0.7, edgecolor='none', pad=5))

    ySecreto = 1.5
    cajaSecreta = patches.Rectangle((0.8, ySecreto - 0.6), longitud + 0.4, 1.2, 
                                     facecolor='#4E342E', edgecolor='#212121', lw=2, zorder=5)
    ax.add_patch(cajaSecreta)
    
    for i, color in enumerate(codigoObjetivo):
        colorHex = colorMap[color]
        fichaObj = plt.Circle((i + 1.5, ySecreto), 0.4, color=colorHex, ec='white', lw=2, zorder=6)
        ax.add_patch(fichaObj)

    ax.text(longitud / 2 + 1, ySecreto - 0.9, "CÓDIGO SECRETO", color='#FFD700',
            ha='center', fontweight='bold', fontsize=12)

    ax.set_xlim(0, longitud + 4)
    ax.set_ylim(0, maxFilas + 6) 
    ax.set_aspect('equal')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
