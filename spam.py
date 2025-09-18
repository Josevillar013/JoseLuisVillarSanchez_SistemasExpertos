# =============================================
# Inteligencia Artificial
# Caso: Clasificación de mensajes (Spam o No Spam)
# Algoritmo: Naive Bayes
# =============================================

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# =============================================
# 1. Crear dataset de mensajes
# =============================================
# Algunos mensajes típicos de spam y no spam
mensajes = [
    "Gana dinero rápido ahora",
    "Oferta exclusiva para ti",
    "Hola, ¿cómo estás?",
    "Te llamo más tarde",
    "Compra 2 y recibe 1 gratis",
    "Reunión mañana a las 9 am",
    "Has sido seleccionado para un premio",
    "Nos vemos en la escuela",
    "Obtén crédito inmediato sin requisitos",
    "¿Quieres salir a cenar?"
]

etiquetas = [
    "Spam", "Spam", "No Spam", "No Spam", 
    "Spam", "No Spam", "Spam", "No Spam", 
    "Spam", "No Spam"
]

# =============================================
# 2. Convertir texto en vectores numéricos
# =============================================
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(mensajes)

# =============================================
# 3. Entrenar modelo
# =============================================
modelo = MultinomialNB()
modelo.fit(X, etiquetas)

# =============================================
# 4. Probar con un nuevo mensaje
# =============================================
nuevo_mensaje = ["Consigue un crédito fácil y rápido"]
X_nuevo = vectorizador.transform(nuevo_mensaje)
prediccion = modelo.predict(X_nuevo)

# =============================================
# 5. Mostrar resultados
# =============================================
print("=============================================")
print(" CLASIFICADOR DE MENSAJES")
print("=============================================")
print("Mensaje nuevo:", nuevo_mensaje[0])
print("Clasificación:", prediccion[0])
