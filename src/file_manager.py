from pathlib import Path
from typing import Optional, List

class FileManager:

    def __init__(
        self,
        folder_path: Optional[Path] = None,
        file_path: Optional[Path] = None
    ):
        
        if not folder_path and not file_path:
            raise ValueError("Debes proporcionar folder_path o file_path")

        self.folder_path = folder_path
        self.file_path = file_path


    def read_folder(self) -> List:

        """
            Método encargado para la lectura de la carpeta
            y el contenido de esta

            Args: 
                - None

            Returns:
                - List: Lista de archivos encontrados en la carpeta
        """

        if self.folder_path is None:
            raise ValueError("No se proporcionó folder_path")

        return list(self.folder_path.iterdir())
    

    def
 

