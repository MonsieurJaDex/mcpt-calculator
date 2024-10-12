import json


class Config:
    def __init__(self, config_filename: str = "config.json") -> None:
        self.config_filename = config_filename

        # подгрузка файла конфига
        try:
            with open(self.config_filename) as file:
                config_data = file.read()
        except:
            print(f"Ошибка поиска файла {self.config_filename}")

        config_data = json.loads(config_data)

        # подгрузка и обработка полей конфига. (возможна реализация автоматической подгрузки через pydantic-settings)

        # обработка rewrite_file
        try:
            self.rewrite_file = config_data["rewrite_file"]
            if not isinstance(self.rewrite_file, bool):
                print(
                    "Обнаружено неожиданное значение параметра 'rewrite_file' в файле конфига, установлено значение по умолчанию (false)."
                )
                self.rewrite_file = False
        except:
            print(
                "Параметр 'rewrite_file' не был найден в файле конфига, установлено значение по умолчанию (false)."
            )
            self.rewrite_file = False

        # обработка valid_extensitions
        try:
            self.file_extension = config_data["file_extension"]
            if not isinstance(self.file_extension, str):
                print(
                    "Обнаружено неожиданное значение параметра 'valid_extensions' в файле конфига, установлено значение по умолчанию (xlsx)."
                )
                self.file_extension = "xlsx"
        except:
            print(
                "Параметр 'valid_extensitions' не был найден в файле конфига, установлено значение по умолчанию (false)."
            )
            self.file_extension = "xlsx"
