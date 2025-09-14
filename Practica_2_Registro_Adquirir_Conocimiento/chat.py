# Importamos librerias necesarias
import json           # Para manejar la base de conocimiento en formato JSON
import os             # Para comprobar si el archivo de conocimiento existe
from colorama import Fore, Style, init   # Para darle color a la salida en consola

# Inicializamos colorama (sirve para que los colores funcionen en Windows/Linux)
init(autoreset=True)

# Definimos el nombre del archivo donde se guardara el conocimiento
DB_FILE = "knowledge.json"

# ------------------------------
# Funciones de manejo del conocimiento
# ------------------------------

def load_knowledge():
    """Carga el conocimiento desde el archivo JSON o lo crea si no existe."""

    # Si el archivo de conocimiento no existe, creamos uno nuevo con frases iniciales
    if not os.path.exists(DB_FILE):
        initial_data = {
            "Hola": "Hola! Como estas?",
            "Como estas?": "Estoy bien, gracias por preguntar :)",
            "De que te gustaria hablar?": "Podemos hablar de tecnologia, ciencia o lo que quieras."
        }
        # Guardamos esas frases iniciales en un archivo JSON
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(initial_data, f, indent=4, ensure_ascii=False)

    # Abrimos y cargamos el archivo JSON con el conocimiento almacenado
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_knowledge(data):
    """Guarda el conocimiento en el archivo JSON."""
    # Escribe el diccionario "data" en el archivo JSON con indentacion bonita
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# ------------------------------
# Funcion principal del ChatBot
# ------------------------------

def chat():
    """Ejecuta el chat interactivo con adquisicion de conocimiento."""

    # Mensaje de bienvenida con formato de colores
    print(Fore.CYAN + "===========================================")
    print(Fore.YELLOW + "     🤖 ChatBot: Registro_Adquirir_Conocimiento")
    print(Fore.CYAN + "===========================================")
    print(Fore.GREEN + "Escribe 'salir' para terminar la conversacion.\n")

    # Cargamos el conocimiento inicial desde el archivo JSON
    knowledge = load_knowledge()

    # Bucle infinito del chat hasta que el usuario escriba "salir"
    while True:
        # Pedimos al usuario que escriba un mensaje
        user_input = input(Fore.BLUE + "Tu: " + Style.RESET_ALL).strip()

        # Si el usuario escribe "salir", terminamos el chat
        if user_input.lower() == "salir":
            print(Fore.MAGENTA + "🤖 ChatBot: Hasta luego! 👋")
            break

        # Si el mensaje del usuario existe en la base de conocimiento
        if user_input in knowledge:
            # Respondemos con la respuesta asociada
            print(Fore.YELLOW + "🤖 ChatBot: " + knowledge[user_input])
        else:
            # Si no existe una respuesta, pedimos al usuario que nos ensene
            print(Fore.RED + "🤖 ChatBot: No se como responder eso.")
            new_response = input(Fore.CYAN + "👉 Que deberia contestar? " + Style.RESET_ALL)
            
            # Guardamos el nuevo conocimiento en el diccionario
            knowledge[user_input] = new_response
            # Persistimos el nuevo conocimiento en el archivo JSON
            save_knowledge(knowledge)
            # Confirmamos al usuario que el bot aprendio algo nuevo
            print(Fore.GREEN + "🤖 ChatBot: Gracias! Aprendi algo nuevo.")
            # Mostramos en consola que se agrego exactamente
            print(Fore.LIGHTBLACK_EX + f"(Nuevo conocimiento: '{user_input}' -> '{new_response}')\n")


# ------------------------------
# Ejecutar el chat
# ------------------------------

# Este condicional asegura que el chat solo se ejecute si el archivo
# es ejecutado directamente (y no importado desde otro script)
if __name__ == "__main__":
    chat()
