import requests
import datetime
import json

def get_stormglass_data(api_key, lat, lng, params=None, start=None, end=None):
    """
    Obtiene datos meteorológicos / oceánicos de StormGlass para
    un punto (lat, lng) y un rango de fechas.
    """

    # Endpoint base de StormGlass
    url = "https://api.stormglass.io/v2/weather/point"

    # Si no se definen params, se da un ejemplo por defecto
    if not params:
        params = "waveHeight,waveDirection,windSpeed"

    # Si no se definen start y end, se hace un intervalo simple
    # Aquí, tomamos "hoy" y "hoy + 6 horas" como ejemplo
    if not start:
        start = datetime.datetime.utcnow().isoformat()
    if not end:
        end_time = datetime.datetime.utcnow() + datetime.timedelta(hours=6)
        end = end_time.isoformat()

    # Construimos un diccionario con los parámetros de la query
    query_params = {
        'lat': lat,
        'lng': lng,
        'params': params,
        'start': start,
        'end': end,
        'source': 'sg'  # Fuente "StormGlass" (sg) para datos
    }

    # Cabeceras: la API Key se va en "Authorization"
    headers = {
        'Authorization': api_key
    }

    try:
        response = requests.get(url, headers=headers, params=query_params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

    return None

if __name__ == "__main__":
    # Tu API Key de StormGlass
    API_KEY = "8de6c8d4-d2ed-11ef-bb67-0242ac130003-8de6c92e-d2ed-11ef-bb67-0242ac130003"

    # Ejemplo de coordenadas (lat, lng) - Costa
    latitud = 58.7984
    longitud = 17.8081

    # Llamamos a la función
    result = get_stormglass_data(API_KEY, latitud, longitud)

    if result:
        # Muestra datos crudos
        print(json.dumps(result, indent=2))
        # Aquí ya podrías parsear "hours" o la parte que te interese

        # -------------------------------------------------------
        # Ejemplo: ahora podrías enviar `result` a tu pipeline:
        #   1. PutRecord en Kinesis
        #   2. PutObject en S3
        #   3. Procesarlo con una Lambda, etc.
        # -------------------------------------------------------
    else:
        print("No se pudieron obtener datos de StormGlass.")
