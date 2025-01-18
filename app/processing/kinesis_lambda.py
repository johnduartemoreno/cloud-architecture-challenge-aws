import boto3
import base64
import json
import os

s3_client = boto3.client('s3')
bucket_name = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    """
    Procesa eventos de Kinesis y guarda los datos en S3.
    """
    for record in event['Records']:
        # Decodificar datos del evento
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        data = json.loads(payload)
        
        # Generar clave única para el archivo
        s3_key = f"{data['sensor_type']}/sensor_{data['sensor_id']}/{data['timestamp']}.json"
        
        # Guardar en S3
        try:
            s3_client.put_object(
                Bucket=bucket_name,
                Key=s3_key,
                Body=json.dumps(data)
            )
            print(f"Guardado en S3: s3://{bucket_name}/{s3_key}")
        except Exception as e:
            print(f"Error al guardar en S3: {e}")
