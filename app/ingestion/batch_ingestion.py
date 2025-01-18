import csv
import json
import os
import time

def read_netflix_csv(csv_path):
    """
    Lee el archivo CSV de Netflix y convierte cada fila en un objeto JSON.
    De momento, solo imprime en pantalla para verificar la lectura.
    """
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for idx, row in enumerate(reader, start=1):
            # Convertir la fila (diccionario) a JSON
            data_json = json.dumps(row)

            # Imprimir el JSON resultante (ejemplo)
            print(f"[FILA {idx}]\n{data_json}\n")

            # Pausa opcional para no saturar la consola
            time.sleep(0.1)

if __name__ == "__main__":
    # Construimos la ruta al CSV
    # asumiendo que el CSV está en: app/ingestion/data/netflix_titles.csv
    CSV_PATH = os.path.join(
        os.path.dirname(__file__),
        "data",
        "netflix_titles.csv"
    )

    # Llamamos a la función de lectura
    read_netflix_csv(CSV_PATH)
