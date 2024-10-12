import pandas as pd


class Calculator:
    def __init__(self, product_cost: float, participation_cost: float):
        # инициализация переменных
        self.product_cost: float = float(product_cost)
        self.participation_cost = float(participation_cost)

        self.assembly: float = None
        self.storage_delivery: float = None
        self.client_delivery: float = None
        self.manager_salary: float = None
        self.transaction_insurance: float = None
        self.service: float = None
        self.transaction_support: None

    # служебный метод по нахождению процента от МСУ
    def _percent_of_participation_cost(self, percent: float | int) -> float:
        assert isinstance(percent, float | int)

        return float(self.participation_cost * (0.01 * percent))

    def calculate_MCPT_fields(self):
        # рассчет позиций, данные которых зависят от себестоимости товара
        self.storage_delivery = self.product_cost * 0.01
        self.service = (self.product_cost + self.storage_delivery) * 0.01

        # рассчет позиций, данные из которых зависят от МСУ
        self.assembly = self._percent_of_participation_cost(1.5)
        self.client_delivery = self._percent_of_participation_cost(1)
        self.manager_salary = self._percent_of_participation_cost(1.8)
        self.transaction_insurance = self._percent_of_participation_cost(3)
        self.transaction_support = self._percent_of_participation_cost(0.9)

    # представление данных в виде DataFrame для дальнейшей обработки
    def to_dataframe(self) -> pd.DataFrame:
        # название полей позиций
        positions = [
            "Себестоимость",
            "Минимальная стоимость участия в тендере",
            "Услуга по сборке",
            "Услуга по доставке товара до склада",
            "Услуга по доставке товара до клиента",
            "Заработная плата менеджера",
            "Услуги по страхованию сделки",
            "Сервисное обслуживание",
            "Услуги по сопровождению сделки",
        ]

        # название полей сумм
        prices = [
            self.product_cost,
            self.participation_cost,
            self.assembly,
            self.storage_delivery,
            self.client_delivery,
            self.manager_salary,
            self.transaction_insurance,
            self.service,
            self.transaction_support,
        ]

        # возврат из метода объекта DataFrame
        return pd.DataFrame({"Позиция": positions, "Сумма, руб.": prices})
