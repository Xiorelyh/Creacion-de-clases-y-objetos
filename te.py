class Te:
    duracion = 365

    @staticmethod
    def retorna_tiempo_y_recomendacion(sabor: int):
        if sabor == 1:
            tiempo = 3
            recomendacion = "al desayuno"
            return (
                tiempo,
                recomendacion
            )
        elif sabor == 2:
            tiempo = 5
            recomendacion = "al medio dia"
            return (
                tiempo,
                recomendacion
            )
        elif sabor == 3:
            tiempo = 6
            recomendacion = "al atardecer"
            return (
                tiempo,
                recomendacion
            )
        else:
            return 0, "Sabor no válido"

    @staticmethod
    def retorna_precio(formato):
        if formato == 500:
            return 3000
        elif formato == 300:
            return 5000
        else:
            return 0
