# umbrella_ai.py
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Creamos datos simulados de clima
data = {
    "prob_lluvia": [10, 80, 50, 90, 20, 70],
    "humedad": [30, 85, 60, 95, 40, 80],
    "viento": [5, 10, 7, 20, 6, 15],   # velocidad del viento km/h
    "llevar_paraguas": ["No", "Sí", "Sí", "Sí", "No", "Sí"]
}

# Convertimos a DataFrame
df = pd.DataFrame(data)

# Variables de entrada (X) y salida (y)
X = df[["prob_lluvia", "humedad", "viento"]]
y = df["llevar_paraguas"]

# Creamos el modelo de IA (árbol de decisión)
modelo = DecisionTreeClassifier()
modelo.fit(X, y)

# Caso nuevo de la vida diaria: pronóstico de hoy
hoy = pd.DataFrame({
    "prob_lluvia": [75],
    "humedad": [70],
    "viento": [12]
})

# Predicción
prediccion = modelo.predict(hoy)

print("¿Debe llevar paraguas hoy?:", prediccion[0])
