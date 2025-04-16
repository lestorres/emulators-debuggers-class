# emulators-debuggers-class
A practical introduction to emulators and debuggers for embedded systems development

# 🧰 Emuladores y Depuradores para Sistemas Embebidos
Repositorio con recursos y apuntes sobre el uso de **emuladores y depuradores open source** en el desarrollo de sistemas embebidos.

---

## 📦 Contenido

- [1. Emuladores](#1-emuladores)
  - [1.1 QEMU](#11-qemu)
  - [1.2 Renode](#12-renode)
  - [1.3 Otros emuladores por fabricante](#13-otros-emuladores-por-fabricante)
- [2. Depuradores](#2-depuradores)
  - [2.1 GDB (GNU Debugger)](#21-gdb-gnu-debugger)
  - [2.2 OpenOCD](#22-openocd)
  - [2.3 Otros depuradores (solo mención)](#23-otros-depuradores-solo-mención)
- [3. Casos de uso en la industria](#3-casos-de-uso-en-la-industria)

---

## 1. Emuladores

### 1.1 QEMU

- Emulador versátil para múltiples arquitecturas: ARM, x86, MIPS, RISC-V.
- Usado en sistemas Linux embebido, CI/CD y pruebas automatizadas.
- Compatible con depuración remota usando GDB.

🔗 [Documentación oficial](https://www.qemu.org/docs/master/)

---

### 1.2 Renode

- Emulador especializado en sistemas embebidos reales (SoCs, buses, sensores).
- Ideal para firmware, RTOS (Zephyr, FreeRTOS) y simulaciones deterministas.

🔗 [Renode Docs](https://renode.readthedocs.io/en/latest/)  
🔗 [GitHub](https://github.com/renode/renode)

---

### 1.3 Otros emuladores por fabricante (solo mención)

- **Esp32-emulator** – Experimental para ESP32.  
- **SimAVR** – Para microcontroladores AVR.  
- **MSPDebug** – Para MSP430 de TI.  
- **PicSimLab / SimulIDE** – Enfocados en educación (PIC, AVR).

---

## 2. Depuradores

### 2.1 GDB (GNU Debugger)

- Depurador estándar open source para C/C++ en sistemas embebidos.
- Soporta depuración remota, paso a paso, breakpoints y análisis en memoria.  
🔗 [GDB](https://www.sourceware.org/gdb/)

---

### 2.2 OpenOCD

- Interfaz entre GDB y hardware físico vía JTAG/SWD.
- Soporta múltiples plataformas: ARM Cortex-M, RISC-V, etc.  
🔗 [OpenOCD](https://openocd.org/pages/documentation.html)

---

### 2.3 Otros depuradores (solo mención)

- **pyOCD** – CMSIS-DAP para Cortex-M.  
- **SEGGER J-Link + GDB Server** – Muy usado en entornos industriales.

---

### 2.4 Casos de uso de los debbugers

| Caso de uso                    | Herramientas comunes             |
|-------------------------------|----------------------------------|
| MCU bare-metal                | GDB + OpenOCD / J-Link           |
| Linux embebido                | GDB + gdbserver                  |
| RTOS sobre MCU                | GDB + Tracealyzer / SystemView  |
| Pruebas automatizadas (CI/CD) | GDB + QEMU                       |
| Depuración en IDEs            | STM32CubeIDE, MPLAB X, PlatformIO|

---
