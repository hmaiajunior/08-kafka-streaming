from confluent_kafka import Consumer, KafkaError
from dotenv import load_dotenv
import os
import csv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do consumidor
conf = {
    'bootstrap.servers': os.getenv('BOOTSTRAP_SERVERS'),
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    #'sasl.username': os.getenv('SASL_USERNAME'),
    #'sasl.password': os.getenv('SASL_PASSWORD'),
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Criação do consumidor
consumer = Consumer(**conf)

# Inscrição no tópico
topic = os.getenv('TOPIC')
consumer.subscribe([topic])