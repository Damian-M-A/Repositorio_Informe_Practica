# Repositorio_Informe_Practica

Repositorio para todo el código desarrollado durante el periodo de práctica.

## Tabla de Contenidos

- [Descripción general](#descripción-general)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Proyectos Principales](#proyectos-principales)
  - [TeslaTut](#teslatut)
  - [Practica CAN](#practica-can)
- [Requisitos](#requisitos)
- [Instalación y uso](#instalación-y-uso)
- [Licencia](#licencia)

---

## Descripción general

Este repositorio agrupa todos los scripts, recursos y bases de datos usados y desarrollados durante la práctica, enfocados en el control, visualización y análisis de señales para sistemas automotrices empleando Python y QML.

## Estructura del Repositorio

```
├── Practica CAN/
│   ├── main_ui.py
│   ├── OBD-v4.1.dbc
│   └── ...otros archivos
├── TeslaTut/
│   ├── main.py
│   └── Controllers/
│       ├── System.py
│       └── HVACHandler.py
└── README.md
```

## Proyectos principales

### TeslaTut

Proyecto de ejemplo de integración entre Python (PySide6) y QML para construir interfaces gráficas interactivas de sistemas de vehículo, inspirado en el sistema Tesla. Los componentes principales son:

- **main.py**  
  Inicia la aplicación QML y conecta la lógica de negocio escrita en Python a través de `System` y `HVACHandler`.

- **Controllers/System.py**  
  Controla los estados del sistema del vehículo: hora, temperatura exterior, nombre de usuario y estado de bloqueo. Utiliza señales y propiedades de Qt compatibles con QML.

- **Controllers/HVACHandler.py**  
  Gestiona el sistema de climatización (HVAC), permitiendo modificar la temperatura objetivo y exposición de control a la interfaz QML.

### Practica CAN

Aplicación para simulación y monitoreo de señales automotrices sobre el bus CAN, con énfasis en visualización en tiempo real usando PyQt5 y pyqtgraph. Los archivos clave son:

- **main_ui.py**  
  Contiene la interfaz gráfica principal, con instrumentos virtuales para velocidad, combustible y gráficas asociadas. Usa temporizadores Qt para actualización continua de datos simulados y reales extraídos de funciones auxiliares.

- **OBD-v4.1.dbc**  
  Base de datos DBC que define los mensajes y señales del bus CAN soportados, compatible con herramientas de diagnóstico y simulación automotrices.

## Requisitos

- Python 3.x
- PySide6 (`pip install PySide6`)
- PyQt5 (`pip install PyQt5`)
- pyqtgraph (`pip install pyqtgraph`)
- numpy (`pip install numpy`)
- Otros módulos requeridos (ver imports en los scripts correspondientes)

## Instalación y uso

### TeslaTut

```bash
cd TeslaTut
python main.py
```

### Practica CAN

```bash
cd "Practica CAN"
python main_ui.py
```

> **Nota:** Puede que sea necesario instalar dependencias adicionales y crear archivos de recursos (ej. imágenes o archivos `.qrc`) según sea necesario por los scripts.


---

### Autor

Desarrollado por Damian-M-A durante el periodo de práctica profesional.
