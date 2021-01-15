# IOT web service Testing
This is a simple docker architecture that I create for a school project.
The goal is two connect all together :
- RabbitMQT
- Apache Nifi
- Mongodb
- Influxdb
- Grafana
- Flask API generated with OpenAPI

## Usage
`docker-compose up -d`
### Service URL:
 - [nifi](http://127.0.0.1:8082/nifi/)
 - [RabbitMQ](http://0.0.0.0:15672)
 - [Grafana](http://127.0.0.1:8086/)
 - [Mongo Express](http://127.0.0.1:8081)

