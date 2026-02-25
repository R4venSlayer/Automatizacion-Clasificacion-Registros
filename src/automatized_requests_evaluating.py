from preprocess_data import PreprocessingInformation
from file_manager import FileManager
from pathlib import Path

from typing import Dict

BASE_DIR = Path(__file__).resolve().parent.parent

def get_files() -> Dict:

    """
    Método encargado de obtener los archivos alojados
    en las respectivas carpetas de fuentes.

    return:
        -   Dict : Diccionario con las rutas de los diferentes archivos encontrados
    """
    # Extracción del contenido de las carpetas main_data y required_data

    # - Rutas dónde se almacena la data a procesar

    folder_path_main_data = BASE_DIR / "data" / "main_data"
    folder_path_required_data = BASE_DIR / "data" / "required_data"

    # - Lectura de la carpeta con la data principal
    content_folder_main_data = FileManager(folder_path = folder_path_main_data).extract_folder_content()
    
    # - Lectura de la carpeta con la data requerida para las validaciones
    content_folder_required_data = FileManager(folder_path = folder_path_required_data).extract_folder_content()

    # Diccionario con las rutas encontradas en la base
    content_directory = {"main_data" : content_folder_main_data, "required_data" : content_folder_required_data}

    return content_directory

def select_base():


    ...

def main():

    # Extracción de archivos en el directorio de bases
    content_directory = get_files()

    # 
    
if __name__ == "__main__":
    main()