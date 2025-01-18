import time
import random
import json

def generate_sensor_data():
    sensor_id = random.randint(1, 5)
    sensor_type = random.choice(["temp", "humidity", "pressure"])
    value = round(random.uniform(0, 100), 2)
    timestamp = time.time()
    return {
        "sensor_id": sensor_id,
        "sensor_type": sensor_type,
        "value": value,
        "timestamp": timestamp
    }

if __name__ == "__main__":
    for _ in range(10):
        data = generate_sensor_data()
        print(json.dumps(data))
        # Aquí podrías enviar a tu pipeline, p. ej.:
        # kinesis.put_record(...) o s3.put_object(...)
        time.sleep(1)
