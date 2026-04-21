import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_DIR = os.path.join(BASE_DIR,"files")

import pandas as pd

def leer_excel(ruta):
    try:
        df = pd.read_excel(ruta)
        return df
    except Exception as e:
        raise

estudiantes = leer_excel(os.path.join(FILES_DIR, "estudiantes.xlsx"))
print(estudiantes)