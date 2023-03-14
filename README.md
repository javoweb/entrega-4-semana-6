# Diagrama solución

![Diagrama](https://user-images.githubusercontent.com/4565451/224879488-6246a460-872f-467d-8188-354801b5919d.png)


# Microservicio - Empaquetado


## Eda
### Ejecutar Base de datos
Desplegar la base de datos y se deja abierta en la terminal.

```bash
docker-compose --profile db up
```

### En una nueva terminal desplegar apache pulsar.

```bash
docker-compose --profile pulsar up
```



## CDC & Debezium

**Nota**: Antes de poder ejectuar todos los siguientes comandos DEBE tener la base de datos MySQL corriendo.


### Ejecutar Debezium
Abrir en una terminal:

```bash
docker exec -it broker bash
```

Ya dentro de la contenedora ejecute:
```bash
./bin/pulsar-admin source localrun --source-config-file /pulsar/connectors/debezium-mysql-source-config.yaml --destination-topic-name debezium-mysql-topic
```

### Consumir eventos Debezium

Abrir en una terminal:

```bash
docker exec -it broker bash
```

Ya dentro de la contenedora ejecute, en esta terminal nos muestra los datos que cambian en la base de datos:

```bash
./bin/pulsar-client consume -s "sub-datos" public/default/edadb.empaquetado.eda_empaquetado -n 0
```

### Ejecutar pruebas

```bash
coverage run -m pytest
```

### Ver reporte de covertura
```bash
coverage report
```

# Microservicio - Adquisiciones

### Ejecutar el microservicio

```bash
flask --app src/adquisiciones/api --debug run -p 5001
```

### Ejecutar el cliente

```bash
python src/cliente-adquisiciones/main.py
```

### Ejecutar las notificaciones

```bash
python src/notificaciones/main.py
```

### Monitoreo Ping-Echo

```bash
curl http://localhost:5001/ping
```

# Microservicio - Ordenes

### Instalar dependencias

```bash
pip install -r requirements-ordenes.txt
```

### Ejecutar el microservicio

```bash
uvicorn ordenes.main:app --host localhost --port 8000 --reload
```

En caso de usar docker compose
```bash
docker compose --profile ordenes up  
```

### Probar el manejo de comandos

Entrar dentro del contenedor

```bash
docker exec -it ordenes bash 
```

Ejecutar un curl al endpoint de prueba

```bash
curl http://localhost:8000/prueba-crear-orden 
```

> Nota: A veces es necesario ejecutarlo más de una vez.
