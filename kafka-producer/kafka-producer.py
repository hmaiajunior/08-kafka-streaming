from confluent_kafka import Producer
from dotenv import load_dotenv
import os
import random
import time

# Carregar variáveis de ambiente do arquivo .env

# Configurações do produtor
conf = {
    'bootstrap.servers': os.getenv('BOOTSTRAP_SERVERS'),
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    #'sasl.username': os.getenv('SASL_USERNAME'),
    #'sasl.password': os.getenv('SASL_PASSWORD'),
    'client.id': os.getenv('CLIENT_ID')
}