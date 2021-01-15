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
`sudo docker-compose up -d`

If grafana doesn't work well check that the owner of "grafana.db" is the same as the user in the container.
If it isn't then specify the uid in the docker-compose.yaml.

### Service URL:
 - [nifi](http://127.0.0.1:8082/nifi/)
 - [RabbitMQ](http://0.0.0.0:15672)
 - [Grafana](http://127.0.0.1:3000/d/ayBwnBAMz/general?orgId=1)
 - [Mongo Express](http://127.0.0.1:8081)

