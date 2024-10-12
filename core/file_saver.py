import datetime
import os

import pandas as pd


class FileSaver:
    def __init__(self, data: pd.DataFrame, rewrite_file: bool, file_extension: str, filename: str | None) -> None:
        self.data = data
        self.filename = filename
        self.rewrite_file = rewrite_file
        self.file_extension = file_extension

        # применение стандартного имени файла при отсутствии ввода и преобразование введенного имени файла в валидное
        if not filename:
            self.filename = f"MCPT_details_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.xlsx"
        else:
            if not filename.endswith(f".{self.file_extension}"):
                self.filename = self.filename.replace(".", "")
                self.filename += f".{self.file_extension}"

    # метод сохранения данных в файл
    def save(self) -> None:
        # вывод сообщения если файл существует и не поставлено разрешение на перезапись файлов в файле конфига
        if self.filename in os.listdir() and not self.rewrite_file:
            print(f"Файл с именем: {self.filename} уже существует.\nПоставьте настройку rewrite_file в значение true в файле config.json, если вы хотите, чтобы программа изменяла существующие файлы.")
            return
        
        # инициализация writer'а и запись файла в папку outputs (возможна реализация через модуль os или pathlib)
        writer = pd.ExcelWriter(f"outputs/{self.filename}", engine="xlsxwriter")
        self.data.to_excel(excel_writer=writer, sheet_name="Детализация рассчетов по МСУ", index=None)
        writer.close()

        print(f"Данные сохранены в файле {self.filename}")

