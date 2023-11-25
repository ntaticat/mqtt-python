# MQTT-Python

Python Script that connects to MQTT and subscribes to a topic

## Docker configuration

```[bash]
docker volume create mosquittoconf
```

```[bash]
docker run -it -d -name="mosquitto" -p 1883:1883 -p 9001:9001 -v mosquittoconf:/mosquitto/ eclipse-mosquitto
```
