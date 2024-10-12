class InputScanner:
    def __init__(self) -> None:
        # инициализация переменных
        self.product_cost: float | int = None
        self.participation_cost: float | int = None
        self.filename: str | None = None

    def request_data(self) -> None:
        # данные с ввода
        product_cost = input("Введите себестоимость товара: ")
        participation_cost = input("Введите МСУ: ")

        filename = input(
            "Введите желаемое название файла с данными (оставьте поле пустым если хотите создать название автоматически): "
        )

        # проверка ввода имени файла
        if len(filename.strip()) == 0:
            self.filename = None
        else:
            self.filename = filename

        # проверка и конвертация типов
        try:
            self.product_cost = float(product_cost.strip())
            self.participation_cost = float(participation_cost.strip())
        except:
            print("Возникла ошибка ввода. Проверьте корректность введенных данных.")
            quit()
