import pyautogui
import random
import time
import threading

def move_cursor():
    def keep_screen_active():
        while True:
            # Emula una pulsación de tecla cada 60 segundos
            pyautogui.press('shift')
            time.sleep(60)

    # Inicia el hilo para mantener la pantalla activa
    threading.Thread(target=keep_screen_active, daemon=True).start()

    while True:
        # Genera coordenadas aleatorias dentro de la pantalla
        x = random.randint(0, pyautogui.size()[0])
        y = random.randint(0, pyautogui.size()[1])

        # Mueve el cursor a las coordenadas aleatorias de forma más lenta
        pyautogui.moveTo(x, y, duration=0.5)

        # Espera un breve instante antes de generar nuevas coordenadas aleatorias
        time.sleep(0.5)

        # Espera 5 segundos antes de generar nuevas coordenadas aleatorias
        time.sleep(5)

# Ejecuta la función principal
move_cursor()
