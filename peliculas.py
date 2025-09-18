# =============================================
# Inteligencia Artificial
# Caso: Recomendación de películas
# Algoritmo: K-Nearest Neighbors (KNN)
# =============================================

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# =============================================
# 1. Crear dataset de películas y gustos
# =============================================
# Variables:
# - genero (1=Acción, 2=Comedia, 3=Drama, 4=Terror, 5=Romántica)
# - duracion (minutos)
# - me_gusta (Sí/No)
data = {
    "genero":   [1, 2, 3, 4, 5, 1, 2, 3, 5, 4],
    "duracion": [120, 90, 150, 100, 110, 130, 85, 160, 95, 105],
    "me_gusta": ["Sí", "Sí", "No", "No", "Sí", "Sí", "Sí", "No", "Sí", "No"]
}

df = pd.DataFrame(data)

# Variables independientes y dependiente
X = df[["genero", "duracion"]]
y = df["me_gusta"]

# =============================================
# 2. Entrenar modelo
# =============================================
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

# =============================================
# 3. Caso nuevo (una película que quiero ver)
# =============================================
nueva_pelicula = pd.DataFrame({
    "genero": [2],     # 2 = Comedia
    "duracion": [100]  # 100 min
})

prediccion = modelo.predict(nueva_pelicula)

# =============================================
# 4. Mostrar resultados
# =============================================
print("=============================================")
print(" RECOMENDADOR DE PELÍCULAS")
print("=============================================")
print("Película nueva:", nueva_pelicula)
print("¿Me gustará?:", prediccion[0])
