import json
import os

# Nombre del archivo de conocimiento
DB_FILE = "knowledge.json"

# Función para cargar conocimiento
def load_knowledge():
    if not os.path.exists(DB_FILE):
        # Conocimiento inicial precargado
        initial_data = {
            "Hola": "¡Hola! ¿Cómo estás?",
            "¿Cómo estás?": "Estoy bien, gracias por preguntar 😊",
            "¿De qué te gustaría hablar?": "Podemos hablar de tecnología, ciencia o lo que quieras."
        }
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(initial_data, f, indent=4, ensure_ascii=False)
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Función para guardar conocimiento
def save_knowledge(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Chat principal
def chat():
    print("🤖 ChatBot con módulo de adquisición de conocimiento")
    print("Escribe 'salir' para terminar.\n")

    knowledge = load_knowledge()

    while True:
        user_input = input("Tú: ").strip()

        if user_input.lower() == "salir":
            print("🤖 ChatBot: ¡Hasta luego!")
            break

        if user_input in knowledge:
            print("🤖 ChatBot:", knowledge[user_input])
        else:
            print("🤖 ChatBot: No sé cómo responder eso.")
            new_response = input("👉 ¿Qué debería contestar? ")
            knowledge[user_input] = new_response
            save_knowledge(knowledge)
            print("🤖 ChatBot: ¡Gracias! Aprendí algo nuevo.")

if __name__ == "__main__":
    chat()
