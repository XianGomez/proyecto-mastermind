def poblarGeneracion(hijos, tamanhoPoblacion):
    #Si faltan individuos para llegar al tamaño original, se completan. Si sobran, se recortan
    nuevaPoblacion = hijos[:tamanhoPoblacion]
    return nuevaPoblacion