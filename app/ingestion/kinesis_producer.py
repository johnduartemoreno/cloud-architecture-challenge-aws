import boto3
import json
import time
from iot_simulator import generate_sensor_data  # Importamos la función del simulador

# Configuración del stream de Kinesis
STREAM_NAME = "aws-data-ingestion-data-stream"
REGION = "us-east-1"  # Cambia si estás utilizando otra región de AWS

# Cliente de Kinesis
kinesis_client = boto3.client("kinesis", region_name=REGION)

def send_to_kinesis(data):
    """
    Envía un registro al stream de Kinesis.
    """
    try:
        response = kinesis_client.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(data),  # Convertimos el dict a JSON
            PartitionKey=str(data["sensor_id"]),  # Usamos el sensor_id como clave de partición
        )
        print(f"Enviado: {data} | SequenceNumber: {response['SequenceNumber']}")
    except Exception as e:
        print(f"Error enviando datos: {e}")

def main():
    """
    Genera datos simulados desde iot_simulator.py y los envía al stream de Kinesis en un bucle continuo.
    """
    print(f"Enviando datos al stream {STREAM_NAME}...")
    while True:
        # Generar un dato simulado
        sensor_data = generate_sensor_data()
        
        # Enviar el dato al stream de Kinesis
        send_to_kinesis(sensor_data)
        
        # Pausa de 1 segundo entre envíos
        time.sleep(1)

if __name__ == "__main__":
    main()
