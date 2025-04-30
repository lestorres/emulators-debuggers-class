# Emuladores y Depuradores para Sistemas Embebidos

---

## 📦 Contenido

- [0. Introducción](#0-introducción)
- [1. Emuladores](#1-emuladores)
  - [1.1 QEMU](#11-qemu)
  - [1.2 Otros emuladores para explorar](#12-otros-emuladores-para-explorar)
- [2. Depuradores](#2-depuradores)
  - [2.1 GDB (GNU Debugger)](#21-gdb-gnu-debugger)
  - [2.2 Otros depuradores para explorar](#22-otros-depuradores-para-explorar)
- [3. Casos de uso comunes](#3-casos-de-uso-comunes)
- [4. Demostración práctica](#4-demostración-práctica)
- [5. Tutorial](#5-tutorial)
- [6. Referencias](#6-referencias)

---

## 0. Introducción

Los sistemas embebidos están presentes en una gran variedad de dispositivos, desde electrodomésticos hasta automóviles y dispositivos médicos. Sin embargo, desarrollar y depurar estos sistemas puede ser complejo debido a las limitaciones de hardware, las restricciones de recursos y la falta de acceso directo a plataformas físicas en etapas tempranas de desarrollo. 

Este documento se centra en el uso de herramientas **open source** como emuladores y depuradores, las cuales permiten simular y depurar sistemas sin la necesidad de contar con hardware físico durante el proceso de desarrollo.

---

## 1. Emuladores

### 1.1 QEMU

QEMU (Quick Emulator) es un emulador y virtualizador de código abierto, versátil y modular, que soporta múltiples arquitecturas como ARM, x86, MIPS y RISC-V. Se utiliza principalmente de dos maneras:

- **Emulación de Sistema**: QEMU emula una máquina completa, permitiendo ejecutar un sistema operativo invitado. En este modo, la CPU puede ser completamente emulada o usar un hipervisor como KVM (Kernel-based Virtual Machine) para ejecutar directamente sobre el CPU del host. Este modo es ideal para testing  ya que permite emular sistemas completos sin necesidad de hardware real.

- **Emulación en Modo Usuario**: QEMU permite ejecutar programas compilados para una arquitectura de CPU diferente en otra, emulando siempre la CPU.

Además, QEMU es compatible con **gdbserver** para depuración remota, lo que facilita el desarrollo y la depuración en entornos sin acceso inmediato a hardware físico. Además herramientas como **qemu-img** para crear y modificar imágenes de disco.

🔗 [Documentación oficial de QEMU](https://www.qemu.org/docs/master/)  
🔗 [Repositorio en GitLab](https://gitlab.com/qemu-project/qemu)

### 1.2 Otros emuladores para explorar

- **Renode** – Emulador especializado en sistemas embebidos con buses y sensores. Ideal para pruebas de RTOS y simulaciones deterministas.
- **Esp32-emulator** – Para plataformas ESP32, útil en desarrollo de IoT.
- **SimAVR** – Emulador para microcontroladores AVR, popular en el desarrollo de proyectos de electrónica.
- **MSPDebug** – Emulador y depurador para microcontroladores MSP430 de Texas Instruments.
- **PicSimLab / SimulIDE** – Emuladores educativos para microcontroladores PIC y AVR, fáciles de usar para iniciarse en la programación de microcontroladores.

---

## 2. Depuradores

### 2.1 GDB (GNU Debugger)

GDB es el depurador estándar para programas escritos en lenguajes como C, C++ , Assembler y otros, especialmente en entornos embebidos. Se utiliza para identificar y corregir errores en el código, permitiendo a los desarrolladores analizar el comportamiento de sus programas en tiempo real. Entre sus funciones permite:

- **Depuración Remota**: GDB soporta depuración remota, lo que permite depurar aplicaciones en sistemas que no tienen acceso directo al entorno de desarrollo, como dispositivos embebidos o máquinas virtuales.

- **Breakpoints y Seguimiento**: GDB permite establecer puntos de interrupción (breakpoints) para detener la ejecución del programa en lugares específicos, inspeccionar la memoria, los registros y el estado del programa en cualquier momento durante su ejecución.

- **Conexión a Emuladores y Hardware Real**: GDB se puede conectar a emuladores como QEMU o a hardware real a través de herramientas como OpenOCD, lo que lo hace útil para trabajar en sistemas sin acceso directo al código fuente o cuando se trabaja con plataformas de hardware especializadas.

🔗 [Sitio oficial de GDB](https://www.sourceware.org/gdb/)  
🔗 [Repositorio oficial](https://sourceware.org/git/binutils-gdb.git)

### 2.2 Otros depuradores para explorar

- **OpenOCD** – Conexión entre GDB y hardware físico mediante JTAG/SWD. Compatible con diversas plataformas como ARM y RISC-V.
- **pyOCD** – Depurador basado en Python para plataformas ARM Cortex-M, compatible con CMSIS-DAP.
- **SEGGER J-Link GDB Server** – Herramienta muy utilizada en entornos industriales, ideal para depuración en hardware real.
- **GDBserver** – Usado para depuración remota en sistemas Linux embebidos, trabajando junto con QEMU.
- **Tracealyzer** – Herramienta de análisis y depuración para sistemas con RTOS, ideal para estudiar la ejecución de software en plataformas embebidas.

---

## 3. Casos de uso comunes

| Escenario                     | Herramientas principales   |
|------------------------------|----------------------------|
| MCU bare-metal               | GDB + OpenOCD              |
| Linux embebido               | QEMU + GDB (gdbserver)     |
| RTOS sobre MCU               | GDB                        |
| CI/CD para firmware          | QEMU + GDB                 |

---

## 4. Demostración práctica

Esta sección te guiará a través de un ejemplo práctico utilizando **QEMU + GDB** para emular y depurar un programa simple en un entorno embebido.

### Pasos a seguir:

1. **Instalación de herramientas**:
   - Instalar QEMU y GDB en tu máquina local.
   
2. **Compilación del programa**:
   - Usar `gcc` o `clang` para compilar un programa en C que se pueda ejecutar en la arquitectura que estás emulando (por ejemplo, ARM o RISC-V).

3. **Emulación con QEMU**:
   - Ejecutar QEMU con la imagen compilada.
   - Iniciar el emulador con parámetros adecuados para permitir la conexión remota de GDB.

4. **Depuración remota con GDB**:
   - Conectar GDB a QEMU usando `gdbserver`.
   - Establecer breakpoints y examinar registros y memoria.

---

## 5. Tutorial

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

## 6. Referencias

[1] QEMU Project. “QEMU: A generic and open source machine emulator and virtualizer,” GitLab repository. [Online]. Available: https://gitlab.com/qemu-project/qemu

[2] GNU Project. “GDB: The GNU Debugger,” Sourceware repository. [Online]. Available: https://sourceware.org/git/binutils-gdb.git
