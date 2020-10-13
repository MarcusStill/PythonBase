class MyError(ValueError):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Неправильный ввод! Вы ввели {self.value}. Значение должно быть отличным от 0.'