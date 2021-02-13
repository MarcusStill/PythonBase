"""В этом модуле описаны классы, связанные с посетителями."""
class Child():
    """Родительский класс с основными атрибутами посетителя-ребенка."""
    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.visit = 0


    def get_description(self):
        """Высод информации о ребенке."""
        full_name = f"Информация о ребенке: {self.first_name} {self.last_name}, дата рождения: {self.birth_date}, пол: {self.gender}"
        return full_name.title()


    def greeting(self):
        """Представление ребенка."""
        print(f"Меня зовут {self.first_name} {self.last_name}.")


    def read_visit(self):
        """Вывод информации о количестве посещений ребенком детского центра."""
        print(f"Этот ребенок был в детском центре {self.visit} раз.")


    def update_visit(self, number):
        """Обновлении информации о количестве посещений ребенком детского центра."""
        self.visit = number


class Parent(Child):
    """Дочерний класс, который от класса Child наличием атрибутов phone и category (наличие льгот)."""
    def __init__(self, first_name, last_name, birth_date, gender, phone, category):
        super().__init__(first_name, last_name, birth_date, gender)
        self.phone = phone
        self.category = category


    def get_description(self):
        """Высод информации о взрослом посетителе."""
        full_name = f"Информация о взрослом: {self.first_name} {self.last_name} {self.birth_date} {self.gender} №_тел {self.phone} категория {self.category}"
        return full_name.title()


    def update_visit(self):
        """Отмена учета количества посещений взрослым детского центра."""
        print("Количество посещений детского центра родителями не ведется!")