import boto3
import json
import requests

# Configuración de AWS Kinesis
kinesis_client = boto3.client("kinesis", region_name="us-east-1")
KINESIS_STREAM_NAME = "aws-data-ingestion-data-stream"

# Configuración de Stormglass API
API_URL = "https://api.stormglass.io/v2/weather/point"
API_KEY = "8de6c8d4-d2ed-11ef-bb67-0242ac130003-8de6c92e-d2ed-11ef-bb67-0242ac130003"

def fetch_stormglass_data():
    params = {
        "lat": 58.7984,
        "lng": 17.8081,
        "params": ",".join(["waveHeight", "waveDirection", "windSpeed"]),
        "start": "2025-01-15",
        "end": "2025-01-15",
        "source": "sg"
    }
    headers = {
        "Authorization": API_KEY
    }
    response = requests.get(API_URL, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()["hours"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

def send_to_kinesis(data):
    for record in data:
        response = kinesis_client.put_record(
            StreamName=KINESIS_STREAM_NAME,
            Data=json.dumps(record),
            PartitionKey=str(record["time"])
        )
        print(f"Enviado a Kinesis: {response}")

if __name__ == "__main__":
    stormglass_data = fetch_stormglass_data()
    if stormglass_data:
        send_to_kinesis(stormglass_data)
