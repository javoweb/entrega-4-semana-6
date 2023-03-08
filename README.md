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
