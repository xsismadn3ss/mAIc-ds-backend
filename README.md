# AI API
Capa de backend para ejecutar las peticiones de los clientes para eldashboard con IA llamado "analisis alinstante".

## Requerimientos
Desarrollar un backend desarrollado en **python** usando **FastAPI**. Se deben utilizar librerías como **Pandas** para procesar las hojas de cálculo y generar los dataframes.

## Features
- Desarrollar un Endpoint que admita archivos CSV y XLSX (excell), en la  lógica de negocio se deben procesar los datos y generar los dataframes, posteriormente se deben mandar los dataframes al LLM para que los interprete correctamente y los develva cómo un JSON con el siquiente esquema.

```json
{
    "title": "...",
    "chart_type": "...",
    "parameters": [
        {"x_axis": "Categoria 1", "y_axis": "valor1"},
        // ...
    ]
}
```

- Desarrollar un segundo endpoint para obtener los datos necesarios de un gráfico específico. En este endpoint se reciben los parameters del gráfico y devuele los datos agregados y formateados listos para ser visualizados.