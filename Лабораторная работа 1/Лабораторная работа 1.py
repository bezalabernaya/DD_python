import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class HandmadeJewelry:
    def __init__(self, length: float, num_beads: int, accessory: int):
        """
        Создание и подготовка к работе объекта "Украшение ручной работы"

        :param length: Длина украшения в см
        :param num_beads: Количество бусин в изделии
        :param accessory: Дополниетельные аксессуары (кулоны, красивые бусины)

        Примеры:
        >>> necklace = HandmadeJewelry(34, 60, 4)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина украшения int или float")
        if length <= 0:
            raise ValueError("Длина украшения должна быть положительным числом")
        self.length = length

        if not isinstance(num_beads, int):
            raise TypeError("Количество бусин int")
        if num_beads <= 0:
            raise ValueError("Количество бусин должно быть положительным числом")
        self.num_beads = num_beads

        if not isinstance(accessory, int):
            raise TypeError("Количество аксессуаров должно быть int ")
        if accessory < 0:
            raise ValueError("Количество аксессуаров не может быть отрицательным числом")
        self.additional_accessory = accessory

    def availability_of_accessories(self) -> bool:
        """
        Функция которая проверяет есть ли аксессуары в украшении

        :return: есть ли аксессуары в украшении

        Примеры:
        >>> necklace = HandmadeJewelry(34, 60, 4)
        >>> necklace.availability_of_accessories()
        """
        ...

    def add_accessory(self, num_accessory: int) -> None:
        """
        Добавление аксессуаров в изделие.
        :param num_accessory: количество добавляемых аксессуаров
        :raise ValueError: Если количество добавляемых аксессуаров превышает количество бусин, то вызываем ошибку

        Примеры:
        >>> necklace = HandmadeJewelry(34, 60, 4)
        >>> necklace.add_accessory(200)
        """
        if not isinstance(num_accessory, int):
            raise TypeError("Количество добавляемых аксессуаров должно быть int ")
        if num_accessory < 0:
            raise ValueError("Количество добавляемых аксессуаров должно быть положительным числом")
        ...

    def change_in_length(self, desired_length: float) -> int:
        """
        Изенение длины изделия.

        :param desired_length: Желаемая длина
        :raise ValueError: Если желаемая длина < 0,то возвращается ошибка.

        :return: Количество бусин, необходимое для покрытия желаемой длины изделия

        Примеры:
        >>> necklace = HandmadeJewelry(34, 60, 4)
        >>> necklace.change_in_length(40)
        """


class Meal:
    def __init__(self, meat: float, vegetables: float):
        """
        Создание и подготовка к работе объекта "Блюдо"

        :param meat: мясо в граммах, входящее в состав блюда
        :param vegetables: овощи в граммах, входящее в состав блюда

        Примеры:
        >>> soup = Meal(34, 60)  # инициализация экземпляра класса
        """
        if not isinstance(meat, (int, float)):
            raise TypeError("мясо в граммах int или float")
        if meat < 0:
            raise ValueError("мясо в граммах должно быть неотрицательным числом")
        self.meat = meat

        if not isinstance(vegetables, (int, float)):
            raise TypeError("овощи в граммах int или float")
        if vegetables <= 0:
            raise ValueError("овощи в граммах должны быть неотрицательным числом")
        self.vegetables = vegetables


    def vegetarian_dish(self) -> bool:
        """
        Функция которая проверяет есть ли мясо в блюде

        :return: есть ли мясо в блюде

        Примеры:
        >>> soup = Meal(34, 60)
        >>> soup.vegetarian_dish()
        """
        ...

    def add_vegetables(self, num_vegetables: float) -> None:
        """
        Добавление овощей в блюдо.
        :param num_vegetables: желаемое количество грамм овощей в блюде
        :raise ValueError: Если вес добавляемых овощей превышает изначальный вес блюда (meat+vegetables), то вызываем ошибку.

        Примеры:
        >>> soup = Meal(34, 60)
        >>> soup.add_vegetables(200)
        """
        if not isinstance(num_vegetables, (int,float)):
            raise TypeError("вес добавляемых овощей должн быть int или float")

class Cosmetic:
    def __init__(self, eyeshadow: int, mascara: bool):
        """
        Создание и подготовка к работе объекта "Косметика"

        :param eyeshadow: количество цветов в палетке теней
        :param mascara: наличие туши в косметичке

        Примеры:
        >>> makeup = Cosmetic(10, True)  # инициализация экземпляра класса
        """
        if not isinstance(eyeshadow, int):
            raise TypeError("количество цветов в палетке теней int ")
        if eyeshadow <= 0:
            raise ValueError("количество цветов в палетке теней должн быть положительным числом")
        self.eyeshadow = eyeshadow

        if not isinstance(mascara, bool):
            raise TypeError("Тушь либо есть либо нет")
        self.mascara = mascara

    def add_eyeshadow(self, num_eyeshadow: int) -> int:
        """
        Функция которая добавляет в косметичку новую палетку теней

        :return: новое количество достуных цветов теней

        Примеры:
        >>> makeup = Cosmetic(10, True)
        >>> makeup.add_eyeshadow(5)
        """
        if not isinstance(num_eyeshadow, int):
            raise TypeError("Количество добавляемых цветов теней должно быть int ")
        if num_eyeshadow < 3:
            raise ValueError("В добавляемой палетке должно быть минимум 3 цвета")


    def num_unique_makeup(self) -> int:
        """
        Функция расчитывает сколько можно сделать уникальных макиежей с ипользованием всех продуктов в косметичке.
        (каждый цвет - отдельный макияж, тени + тушь - отдельный макияж)

        :return: Количество уникальных макиежей

        Примеры:
        >>> makeup = Cosmetic(10, True)
        >>> makeup.num_unique_makeup()
        """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
