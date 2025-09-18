# =============================================
# Ejemplo sencillo de Inteligencia Artificial
# Caso de la vida diaria: ¿Debo llevar paraguas?
# Algoritmo: Árbol de Decisión
# Autor: Jose Luis Villar
# =============================================

# Importamos las librerías necesarias
from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

# =============================================
# 1. Crear un conjunto de datos (dataset simulado)
# =============================================
# Cada fila representa un día con:
# - probabilidad de lluvia (%)
# - humedad (%)
# - velocidad del viento (km/h)
# - decisión real tomada (Sí / No)
data = {
    "prob_lluvia": [10, 80, 50, 90, 20, 70, 40, 95, 15, 85],
    "humedad":     [30, 85, 60, 95, 40, 80, 55, 90, 35, 88],
    "viento":      [5, 10, 7, 20, 6, 15, 8, 18, 4, 12],
    "llevar_paraguas": ["No", "Sí", "Sí", "Sí", "No", "Sí", "Sí", "Sí", "No", "Sí"]
}

# Convertimos los datos a un DataFrame (tabla de pandas)
df = pd.DataFrame(data)

# =============================================
# 2. Separar variables independientes (X) y dependiente (y)
# =============================================
# X = características de entrada (clima)
# y = salida esperada (decisión)
X = df[["prob_lluvia", "humedad", "viento"]]
y = df["llevar_paraguas"]

# =============================================
# 3. Entrenar el modelo con un Árbol de Decisión
# =============================================
modelo = DecisionTreeClassifier(random_state=42)  # reproducibilidad
modelo.fit(X, y)  # entrenar el modelo con los datos

# =============================================
# 4. Probar el modelo con un caso nuevo (datos de hoy)
# =============================================
# Supongamos que hoy el pronóstico es:
# - 75% probabilidad de lluvia
# - 70% humedad
# - 12 km/h de viento
hoy = pd.DataFrame({
    "prob_lluvia": [75],
    "humedad": [70],
    "viento": [12]
})

# Hacemos la predicción
prediccion = modelo.predict(hoy)

# =============================================
# 5. Mostrar resultados
# =============================================
print("=============================================")
print(" PREDICCIÓN DEL MODELO DE IA")
print("=============================================")
print("Datos de hoy:")
print(hoy)
print("¿Debe llevar paraguas hoy?:", prediccion[0])

# =============================================
# 6. Extra: Mostrar reglas del Árbol de Decisión
# =============================================
# Esto nos ayuda a entender cómo el modelo tomó la decisión
arbol_texto = export_text(modelo, feature_names=["prob_lluvia", "humedad", "viento"])
print("\nReglas aprendidas por el modelo:")
print(arbol_texto)
