# 08-kafka-streaming

Comando úteis para o compose:

docker-compose down

docker-compose down -v --remove-orphans --> Isso removerá os volumes associados ao cluster Kafka e redes órfãs.

docker-compose build --no-cache --> Isso força a recriação das imagens, garantindo que nenhuma configuração antiga seja reaproveitada