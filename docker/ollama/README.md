Levantas con:
```
docker compose up -d
```


Luego entras al contenedor:
```
docker exec -it ollama bash
```


Dentro:
```
ollama pull gemma:2b
```


El modelo queda guardado en el volumen ./ollama.

## Ejecutar directamente con docker run
```
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ./ollama:/root/.ollama \
  ollama/ollama
```


Luego:
```
docker exec -it ollama ollama pull gemma:2b
```


## Probar desde host

Una vez descargado, puedes probar:
```
curl http://localhost:11434/api/generate -d '{
  "model": "gemma:2b",
  "prompt": "Escribe un haiku sobre bases de datos"
}'
```