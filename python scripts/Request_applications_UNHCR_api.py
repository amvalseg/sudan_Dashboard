import requests
import pandas as pd
# URL de la API
url = "https://api.unhcr.org/population/v1/asylum-applications/"
# Parámetros de la solicitud
params = {
    "yearFrom": 2023,
    "yearTo": 2024,
    "coo": "SDN",
    "coa_all": "true",
    "cf_type": "ISO",
    "limit": 100,  # Ajusta el límite por página si es necesario
    "page": 1       # Página inicial (comienza en la 1)
}

# Cabeceras para aceptar el contenido en formato CSV
headers = {
    "Accept": "applications/json"  # Cambié a JSON porque los datos están en JSON, no CSV
}

# Lista para almacenar los datos de todas las páginas
all_data = []

# Realizar solicitudes hasta que todas las páginas se hayan procesado
while True:
    # Realizar la solicitud GET
    response = requests.get(url, params=params, headers=headers)

    # Comprobar si la respuesta es exitosa (código 200)
    if response.status_code == 200:
        # Obtener la respuesta en formato JSON
        response_json = response.json()

        # Extraer los datos de la columna "items" (que contiene los resultados reales)
        page_data = response_json.get('items', [])

        # Aplanar el diccionario en "items" para un formato adecuado de DataFrame
        # pd.json_normalize se encarga de aplanar la estructura
        page_df = pd.json_normalize(page_data)

        # Añadir los datos de esta página a la lista
        all_data.append(page_df)

        # Comprobar si hay más páginas
        current_page = params["page"]
        total_pages = response_json.get('maxPages', 1)  # Comprobar cuántas páginas hay

        # Si ya hemos procesado todas las páginas, salir del bucle
        if current_page >= total_pages:
            break

        # Incrementar el número de página para la siguiente solicitud
        params["page"] = current_page + 1

    else:
        # Si la solicitud falla, levantar una excepción
        raise Exception(f"Error en la solicitud: {response.status_code} - {response.text}")

# Concatenar todos los DataFrames de las páginas en uno solo
final_data = pd.concat(all_data, ignore_index=True)

final_data