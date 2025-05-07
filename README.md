# Emuladores y Depuradores para Sistemas Embebidos

---

## 📦 Contenido

- [0. Introducción](#0-introducción)
- [1. Emuladores](#1-emuladores)
  - [1.1 QEMU](#11-qemu)
- [2. Depuradores](#2-depuradores)
  - [2.1 GDB (GNU Debugger)](#21-gdb-gnu-debugger)
  - [2.2 PDB (Python Debugger)](#22-pdb-python-debugger)
- [3. Demostración práctica](#3-demostración-práctica)
- [4. Tutorial](#4-tutorial)
- [6. Referencias](#5-referencias)

---

## 0. Introducción

Los sistemas embebidos están presentes en una gran variedad de dispositivos, desde electrodomésticos hasta automóviles y dispositivos médicos. Sin embargo, desarrollar y depurar estos sistemas puede ser complejo debido a las limitaciones de hardware, las restricciones de recursos y la falta de acceso directo a plataformas físicas en etapas tempranas de desarrollo. 

Esta guía se centra en el uso de herramientas **open source** como emuladores y depuradores, las cuales permiten simular y depurar sistemas sin la necesidad de contar con hardware físico durante el proceso de desarrollo.

## Conceptos básicos

###  Simulación, emulación y depuración

| Término     | Descripción                                                                 |
|-------------|-----------------------------------------------------------------------------|
| Simulación  | Ejecuta una representación del sistema, sin correr binarios reales.         |
| Emulación   | Ejecuta binarios como si estuvieran en el hardware objetivo (ej. QEMU).     |
| Depuración  | Permite observar, controlar y modificar la ejecución de código en tiempo real.|


### ¿Qué se espera de una Simulación y de una Emulación?

| Tipo        | ¿Qué se espera?                                                                 | Ejemplo concreto                                                |
|-------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------|
| **Simulación** | Comportamiento lógico o funcional del sistema, sin ejecutar el código real.     | Simular un sensor de temperatura en MATLAB o un microcontrolador en SystemVerilog.          |
| **Emulación**  | Ejecutar el binario tal como lo haría el hardware real, con tiempos y entorno cercanos al físico. | Usar QEMU para correr una imagen de Linux ARM en tu PC o emular un microcontrolador STM32 para probar firmware.        |

### Diferencia clave:
- **Simulación**: útil para **diseño y validación temprana**.
- **Emulación**: útil para **pruebas funcionales, depuración y validación sin hardware**.


## Modelos y pruebas avanzadas

- **Hardware-in-the-Loop (HIL)**: Pruebas con hardware real o parcialmente simulado.
  > Ejemplo: Probar un firmware en una placa real conectada a un modelo simulado de sensores.
- **Gemelo Digital (Digital Twin)**: Réplica virtual del sistema físico usada para pruebas y validaciones.
  > Ejemplo: Un gemelo digital de un motor industrial permite ajustar parámetros sin detener la producción.


## Prácticas industriales 

| Tema                              | Relevancia                                                                 |
|-----------------------------------|----------------------------------------------------------------------------|
| Toolchains cruzadas               | Compilar/depurar desde PC para microcontroladores o sistemas embebidos objetivo. |
| Scripts de GDB (.gdbinit)         | Automatizar flujos repetitivos en debugging, ya sea hacerlos o usarlos.    |
| CI/CD con QEMU + GDB              | Pruebas de Integración Continua y Despliegue Continuo de firmware sin hardware real.    |
| Interfaces JTAG/SWD               | Depuración física de microcontroladores (MCUs y SoCs).                     |
| Trazas (ej. Tracealyzer, ITM)     | Análisis de eventos y tiempos en RTOS o sistemas críticos.                 |
| Breakpoints                       | Breakpoints en desarrollo, son puntos claves del codigo para analizar.     |
| Optimización vs Depuración        | Uso de flags como `-Og` para depurar código optimizado, es decur, saber cómo las optimizaciones afectan la visibilidad del código al depurar.|
| Análisis post-mortem (core dumps) | Inspección de fallos ya ocurridos.                                        |


## 1. Emuladores

### 1.1 QEMU

QEMU (Quick Emulator) es un emulador y virtualizador de código abierto, versátil y modular, que soporta múltiples arquitecturas como ARM, x86, MIPS y RISC-V. Se utiliza principalmente de dos maneras:

- **Emulación de Sistema**: QEMU emula una máquina completa, permitiendo ejecutar un sistema operativo invitado. En este modo, la CPU puede ser completamente emulada o usar un hipervisor como KVM (Kernel-based Virtual Machine) para ejecutar directamente sobre el CPU del host. Este modo es ideal para testing  ya que permite emular sistemas completos sin necesidad de hardware real [1].

- **Emulación en Modo Usuario**: QEMU permite ejecutar programas compilados para una arquitectura de CPU diferente en otra, emulando siempre la CPU.

Además, QEMU es compatible con **gdbserver** para depuración remota, lo que facilita el desarrollo y la depuración en entornos sin acceso inmediato a hardware físico. Además herramientas como **qemu-img** para crear y modificar imágenes de disco.

🔗 [Documentación oficial de QEMU](https://www.qemu.org/docs/master/)  
🔗 [Repositorio en GitLab](https://gitlab.com/qemu-project/qemu)

### Otros emuladores para explorar

- **Renode** – Emulador especializado en sistemas embebidos con buses y sensores. Ideal para pruebas de RTOS y simulaciones deterministas.
- **Esp32-emulator** – Para plataformas ESP32, útil en desarrollo de IoT.
- **SimAVR** – Emulador para microcontroladores AVR, popular en el desarrollo de proyectos de electrónica.
- **MSPDebug** – Emulador y depurador para microcontroladores MSP430 de Texas Instruments.
- **PicSimLab / SimulIDE** – Emuladores educativos para microcontroladores PIC y AVR, fáciles de usar para iniciarse en la programación de microcontroladores.

---

## 2. Depuradores

### 2.1 GDB (GNU Debugger)

GDB es el depurador estándar para programas escritos en lenguajes como C, C++ , Assembler y otros, especialmente en entornos embebidos. Se utiliza para identificar y corregir errores en el código, permitiendo a los desarrolladores analizar el comportamiento de sus programas en tiempo real [2]. Entre sus funciones permite:

- **Depuración Remota**: GDB soporta depuración remota, lo que permite depurar aplicaciones en sistemas que no tienen acceso directo al entorno de desarrollo, como dispositivos embebidos o máquinas virtuales.

- **Breakpoints y Seguimiento**: GDB permite establecer puntos de interrupción (breakpoints) para detener la ejecución del programa en lugares específicos, inspeccionar la memoria, los registros y el estado del programa en cualquier momento durante su ejecución.

- **Conexión a Emuladores y Hardware Real**: GDB se puede conectar a emuladores como QEMU o a hardware real a través de herramientas como OpenOCD, lo que lo hace útil para trabajar en sistemas sin acceso directo al código fuente o cuando se trabaja con plataformas de hardware especializadas.

🔗 [Sitio oficial de GDB](https://www.sourceware.org/gdb/)  
🔗 [Repositorio oficial](https://sourceware.org/git/binutils-gdb.git)


### 2.2 PDB (Python Debugger)

**PDB** es el depurador estándar incluido en Python, utilizado para diagnosticar y comprender el comportamiento de un programa durante su ejecución. Su funcionamiento se basa en una interfaz interactiva que permite examinar el estado interno del programa paso a paso [3].
PDB resulta especialmente útil para depurar scripts que interactúan con hardware, dispositivos periféricos o procesos concurrentes. Dado que muchos entornos embebidos carecen de interfaces gráficas, PDB proporciona una herramienta efectiva directamente desde la terminal [4].

Características principales:
- **Depuración interactiva**: Permite detener la ejecución en tiempo real, examinar variables, y avanzar instrucción por instrucción.
- **Puntos de interrupción (breakpoints)**: Se pueden establecer ubicaciones específicas para pausar la ejecución y observar el comportamiento del sistema.
- **Análisis post-mortem**: Posibilita revisar el estado del programa inmediatamente después de una excepción o fallo.
- **Integración directa**: Se puede activar desde el código fuente o ejecutar el script en modo depuración desde la terminal.
- **Modularidad y personalización**: Al estar implementado como una clase (Pdb), se adapta a escenarios donde se requiera extender su funcionalidad para depuración avanzada. 

🔗 [Documentación oficial](https://docs.python.org/3/library/pdb.html)  
📦 [Código fuente](https://github.com/python/cpython/blob/main/Lib/pdb.py)

---

### Otros depuradores para explorar

- **OpenOCD** – Conexión entre GDB y hardware físico mediante JTAG/SWD. Compatible con diversas plataformas como ARM y RISC-V.
- **pyOCD** – Depurador basado en Python para plataformas ARM Cortex-M, compatible con CMSIS-DAP.
- **SEGGER J-Link GDB Server** – Herramienta muy utilizada en entornos industriales, ideal para depuración en hardware real.
- **GDBserver** – Usado para depuración remota en sistemas Linux embebidos, trabajando junto con QEMU.
- **Tracealyzer** – Herramienta de análisis y depuración para sistemas con RTOS, ideal para estudiar la ejecución de software en plataformas embebidas.

---

## Casos de uso comunes de uso

| Escenario                        | Herramientas principales             |
|----------------------------------|--------------------------------------|
| MCU bare-metal                   | GDB + OpenOCD                        |
| Linux embebido                   | QEMU + GDB (gdbserver)               |
| RTOS sobre MCU                   | GDB                                  |
| CI/CD para firmware              | QEMU + GDB                           |
| Scripts Python en consola        | `pdb`                                |
| Aplicaciones Python medianas     | `pdb` + `breakpoint()`               |
| Pruebas automatizadas en Python  | `pytest` + `pdb`                     |
| Debug en notebooks interactivos  | `ipdb`, `%debug` (IPython/Jupyter)   |


## 3. Demostración práctica

Esta demostración busca guiar a través de un ejemplo práctico utilizando **QEMU + Python** para emular  un programa simple en un entorno embebido de Raspberry Pi OS Lite based on Debian12 (bookworm), pero en modo **shell root** directamente, sin pasar por **systemd**.

## Parte I: Emulación de Raspberry Pi OS Lite con QEMU en Modo Shell Root
### ✅ Requisitos

- Ubuntu Linux (20.04 o superior)
- Git
- QEMU y Python3 instalado (Se instalan en esta guía y en el tutorial)
- Imagen `.img` de Raspberry Pi OS Lite ( `2024-11-19-raspios-bookworm-armhf-lite.img`, se instala en esta guía)
- Kernel compatible para QEMU ( `kernel-qemu-4.19.50-buster`, ya includo en el repositorio)
- Archivo `.dtb` compatible (`versatile-pb.dtb`, ya includo en el repositorio)

### Paso 1: Desde una terminal se deben instalar los siguiente paquetes:
```bash
sudo apt update
sudo apt install qemu-system-arm qemu-efi
sudo apt install python3
```
### Paso 2: Clonar el Repositorio `emulators-debuggers-class`..
El repositorio completo contiene la siguiente estructura: 
```
emulators-debuggers-class/
  ├── demo/
  │   ├── pdb/
  │   │   ├── pyfetch.py
  │   │   └── pyfetch_2_0.py
  │   └── qemu/
  │       ├── run-qemu.sh
  │       └── qemu-rpi/
  │           ├── kernel-qemu-4.19.50-buster
  │           └── versatile-pb.dtb
  ├── diagnostic/
  │   ├── arbol
  │   ├── arbol.cpp
  │   └── solucion/
  │
  └── tutorial/
        ├── practica_c_gdb
        ├── practica_bonus_asm
        └── practica_qemu 
              ├── 2024-11-19-raspios-bookworm-armhf-lite.img
              ├── run-qemu.sh
              └── qemu-rpi/
                     ├── kernel-qemu-4.19.50-buster
                     └── versatile-pb.dtb
```















## 4. Tutorial

Este tutorial proporciona una guía detallada:

1. **Instalar herramientas necesarias**:
   - Instalar QEMU, GDB y otros programas necesarios en tu sistema operativo.
   
2. **Configurar un entorno de emulación**:
   - Preparar tu entorno para emular sistemas embebidos (ej. ARM, RISC-V).

3. **Compilar y ejecutar un programa en el emulador**:
   - Desde la creación del código fuente hasta la ejecución en QEMU.
   
4. **Configurar y usar GDB para depuración remota**:
   - Conectar GDB a QEMU y realizar depuración paso a paso.

---

## 5. Referencias

[1] QEMU Project. “QEMU: A generic and open source machine emulator and virtualizer,” *GitLab repository*. [Online]. Available: [https://gitlab.com/qemu-project/qemu](https://gitlab.com/qemu-project/qemu)

[2] GNU Project. “GDB: The GNU Debugger,” *Sourceware repository*. [Online]. Available: [https://sourceware.org/git/binutils-gdb.git](https://sourceware.org/git/binutils-gdb.git)

[3] Python Software Foundation. “pdb — The Python Debugger,” *Python 3 Documentation*. [Online]. Available: [https://docs.python.org/3/library/pdb.html](https://docs.python.org/3/library/pdb.html)

[4] Python Software Foundation. “pdb.py — Source code,” *CPython GitHub Repository*. [Online]. Available: [https://github.com/python/cpython/blob/main/Lib/pdb.py](https://github.com/python/cpython/blob/main/Lib/pdb.py)
