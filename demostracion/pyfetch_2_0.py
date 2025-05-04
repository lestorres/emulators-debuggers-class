import platform
import psutil
import os
import time

def draw_penguin():
    penguin = r"""
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
    """
    print("\033[96m" + penguin + "\033[0m")  # Color cian

def system_info():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = round(uptime_seconds / 3600, 2)

    print("\033[93m" + "-" * 40 + "\033[0m")  # Línea amarilla
    print("Sistema Operativo : ", platform.system(), platform.release())
    print("Versión del kernel: ", platform.version())
    print("Arquitectura      : ", platform.machine())
    print("Procesador        : ", platform.processor())
    print("CPU núcleos       : ", psutil.cpu_count(logical=True))
    print("Uso CPU (%)       : ", psutil.cpu_percent(interval=1))
    print("RAM Total         : ", f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print("Uso RAM (%)       : ", psutil.virtual_memory().percent)
    print("Tiempo encendido  : ", uptime_hours, "horas")

if __name__ == "__main__":
    os.system('clear')  # En Windows sería 'cls'
    draw_penguin()
    system_info()
