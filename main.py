from core import Calculator, InputScanner, FileSaver, Config

# инициализация конфига
config = Config()

# инициализация сканнера и запрос ввода
input_scanner = InputScanner()
input_scanner.request_data()

# инициализация калькулятора и рассчет полей
MCPT_calculator = Calculator(
    input_scanner.product_cost, input_scanner.participation_cost
)
MCPT_calculator.calculate_MCPT_fields()

# инициализация службы сохранения файла и сохранение данных в формат xlsx
file_saver = FileSaver(
    data=MCPT_calculator.to_dataframe(),
    rewrite_file=config.rewrite_file,
    filename=input_scanner.filename,
    file_extension=config.file_extension,
)
file_saver.save()
