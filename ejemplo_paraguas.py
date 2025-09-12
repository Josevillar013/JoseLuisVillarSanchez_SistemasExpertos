# Ejemplo de IA: ¿Llevar paraguas según el clima?
# Usaremos un árbol de decisión con datos simulados

from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Datos simulados: 1 = sí, 0 = no
# columnas: [lluvia, nublado, viento]
data = [
    [1, 0, 0],  # Lluvia, no nublado, no viento
    [0, 1, 0],  # No lluvia, nublado, no viento
    [0, 0, 1],  # No lluvia, no nublado, viento
    [1, 1, 1],  # Lluvia, nublado, viento
    [0, 1, 1],  # No lluvia, nublado, viento
    [1, 0, 1],  # Lluvia, no nublado, viento
    [0, 0, 0],  # No lluvia, no nublado, no viento
]
# Etiquetas: 1 = llevar paraguas, 0 = no llevar
labels = [1, 0, 0, 1, 0, 1, 0]

# Crear DataFrame
X = pd.DataFrame(data, columns=["lluvia", "nublado", "viento"])
y = pd.Series(labels)

# Entrenar el modelo
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Probar con un nuevo día: llueve, está nublado y hay viento
nuevo_dia = pd.DataFrame([[1, 1, 1]], columns=["lluvia", "nublado", "viento"])
resultado = clf.predict(nuevo_dia)

print("¿Debo llevar paraguas hoy?", "Sí" if resultado[0] == 1 else "No")
