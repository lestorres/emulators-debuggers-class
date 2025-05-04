import platform
import psutil
import os

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
    print(penguin)

def system_info():
    print("Sistema Operativo : ", platform.system(), platform.release())
    print("Versión del kernel: ", platform.version())
    print("Arquitectura      : ", platform.machine())
    print("Procesador        : ", platform.processor())
    print("CPU núcleos       : ", psutil.cpu_count(logical=True))
    print("RAM Total         : ", f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print("Tiempo encendido  : ", round(psutil.boot_time() / 3600, 2), " horas desde época UNIX")

if __name__ == "__main__":
    os.system('clear')  # Limpia pantalla en Linux/macOS. En Windows usa 'cls'
    draw_penguin()
    print("-" * 40)
    system_info()
