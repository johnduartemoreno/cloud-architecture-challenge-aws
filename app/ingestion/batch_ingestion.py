import os
import pandas as pd
import boto3

# Configuración de AWS S3
s3_client = boto3.client("s3", region_name="us-east-1")
S3_BUCKET_NAME = "aws-data-ingestion-data-bucket"
S3_OBJECT_NAME = "processed/netflix_titles_processed.csv"

# Configuración de logs
log_dir = os.path.join("logs")  # Directorio de logs en la raíz del proyecto
os.makedirs(log_dir, exist_ok=True)

def process_and_upload_csv():
    # Ruta del archivo de entrada
    file_path = os.path.join("app", "ingestion", "data", "netflix_titles.csv")
    
    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        print(f"Archivo no encontrado en {file_path}")
        return
    
    # Leer el archivo CSV
    data = pd.read_csv(file_path)
    print(f"Datos cargados desde {file_path}")
    print(f"Resumen del dataset: {data.shape[0]} filas, {data.shape[1]} columnas")

    # Registrar filas en un archivo de log
    log_file_path = os.path.join(log_dir, "netflix_data.log")  # Ruta completa del archivo de log
    with open(log_file_path, "w") as log_file:
        log_file.write(f"Dataset cargado: {file_path}\n")
        log_file.write(f"Total filas: {data.shape[0]}, columnas: {data.shape[1]}\n")
        log_file.write(data.head().to_string())  # Registrar primeras filas
    print(f"Log escrito en: {log_file_path}")

    # Procesar y subir archivo
    data["processed"] = True
    processed_file_path = os.path.join(log_dir, "netflix_titles_processed.csv")
    data.to_csv(processed_file_path, index=False)
    print(f"Archivo procesado guardado temporalmente en {processed_file_path}")
    
    try:
        s3_client.upload_file(processed_file_path, S3_BUCKET_NAME, S3_OBJECT_NAME)
        print(f"Archivo subido a S3: s3://{S3_BUCKET_NAME}/{S3_OBJECT_NAME}")
    except Exception as e:
        print(f"Error al subir el archivo a S3: {e}")

if __name__ == "__main__":
    process_and_upload_csv()
