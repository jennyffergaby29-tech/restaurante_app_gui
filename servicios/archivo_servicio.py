import json
import os

class ArchivoServicio:
    @staticmethod
    def cargar_json(ruta_archivo: str) -> list:
        if not os.path.exists(ruta_archivo):
            print(f"Advertencia: El archivo {ruta_archivo} no existe.")
            return []
        
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except Exception as e:
            print(f"Error al leer {ruta_archivo}: {e}")
            return []