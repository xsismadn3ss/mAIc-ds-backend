# AI API
Capa de aplicación backend para ejecutar las peticiones de los clientes para el dashboard con IA llamado "análisis al instante". Este proyecto permite generar esquemas de gráficas usando IA.

## Tecnologías utilizadas
- **pydantic**: librería para crear DTOs (Data Transfer Objects) con validaciones.
- **g4f**: GPT 4 All, librería gratis para integrar IA. Debido a que es solo para desarrollo su exactitud y velocidad no es optimizada, pero es útil para hacer demos. 
- **FastAPI**: librería backend para Python,
- **Pandas**: librería con utilidades para ciencia de datos,
- **UV**: gestor de paquetes desarrollado por Astral es útil para crear entornos virtuales e instalar librerías muy rápido gracias a su integración con rust.

## Configurar entorno virtual

1. Instalar uv

Windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Linux/macOS
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Crear y activar entorno virtual:
```bash
uv venv .venv
```

Windows:
```bash
.venv/scripts/activate
```

Linux/MacOS
```bash
source .venv/scripts/activate
```

3. Instalar dependencias
```bash
uv sync
```


## Ejecutar proyecto
Para entornos de desarrollo:
```bash
fastapi dev ./src/main.py
```

En producción:
```bash
uvicorn src.main:app
```
También se puede ejecutar el script ``main.py`` que se encuentra en la raíz del proyecto
```bash
python main.py
```
