import math

if __name__ == "__main__":
    # Write your solution here

    class HandmadeJewelry:
        def __init__(self, length: float, num_beads: int, accessory: int):
            """
            Создание и подготовка к работе объекта "Украшение ручной работы"

            :param length: Длина украшения в см
            :param num_beads: Количество основных бусин в изделии
            :param accessory: Дополниетельные аксессуары (кулоны, красивые бусины)

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
                raise ValueError("Количество аксессуаров должно быть положительным числом")
            self.accessory = accessory

        def add_accessory(self, num_accessory: int):
            """
            Добавление аксессуаров в изделие.
            :param num_accessory: количество добавляемых аксессуаров
            :raise ValueError: Если количество добавляемых аксессуаров превышает количество бусин, то вызываем ошибку

            """
            if not isinstance(num_accessory, int):
                raise TypeError("Количество добавляемых аксессуаров должно быть int ")
            if num_accessory < 0:
                raise ValueError("Количество добавляемых аксессуаров должно быть положительным числом")
            if num_accessory + self.accessory > self.num_beads:
                raise ValueError("Общее количество аксессуаров не должно превышать количество основных бусин")
            else:
                self.accessory = self.accessory + num_accessory
                self.num_beads = self.num_beads - num_accessory
                return self

        def change_length(self, desired_length: float) -> int:
            """
            Изенение длины изделия.

            :param desired_length: Желаемая длина.
            :raise ValueError: Если желаемая длина < 0,то возвращается ошибка.

            :return: Количество основных бусин, необходимое для покрытия желаемой длины изделия

            """
            ''' size_bead - Характерный размер бусины, составляющей основу изделия 
            (размеры основной бусины и аксессуара совпадают)'''
            size_bead = self.length/(self.num_beads+self.accessory)
            if not isinstance(desired_length, (int, float)):
                raise TypeError("Длина изделя должна быть int или float ")
            if desired_length < 0:
                raise ValueError("Длина изделя должна быть положительным числом")
            else:
                new_num_beads = math.ceil(desired_length/size_bead)
                return new_num_beads - self.accessory

        def __str__(self):
            return f"Длина украшения: {self.length} сантиметров." \
                   f" Общее количество бусин в украшении: {self.num_beads + self.accessory}"

        def __repr__(self):
            return f"{self.__class__.__name__}({self.length!r}, {self.num_beads!r}, {self.accessory!r})"


    class Necklace(HandmadeJewelry):
        def __init__(self, length: float, num_beads: int, accessory: int, clasp: str):
            """
            Перегружаем init.
            :param clasp: вид застежки
            Добавили вид застежки, так как объект из класса HandmadeJewerly
            может быть просто кольцом

            В целях симметрии ожерелье должно содержать нечетное количество акссесуаров.
            :raise ValueError: Если количество аксессуаров является четным числом, то вызываем ошибку

            """
            super().__init__(length, num_beads, accessory)
            if accessory % 2 == 0:
                raise ValueError("Количество аксессуаров должно быть нечетным числом")
            self.accessory = accessory
            self.clasp = clasp

        def __repr__(self):
            """
            Перегружаем repr.
            Добавили вывод вида застежки.
            """
            return f"{self.__class__.__name__}({self.length!r}, {self.num_beads!r}, {self.accessory!r}, {self.clasp!r})"

        """
        Методы str и change_length просто наследуем.
        """

        def add_accessory(self, num_accessory: int):
            """
            Перегружаем метод add_accessory.

            В целях симметрии ожерелье должно содержать нечетное количество акссесуаров.
            Поэтому добавляем условие на четность числа добавляемых аксессуаров.
            :raise ValueError: Если количество добавляемых аксессуаров является нечетным числом, то вызываем ошибку.
            :return: Тот же объект, но с новыми занчениями accessory и num_beads.
            """

            if num_accessory % 2 != 0:
                raise ValueError("Количество добавляемых аксессуаров должно быть четным числом")
            else:
                return super().add_accessory(num_accessory)

    ring = HandmadeJewelry(6.5, 15, 1)
    print(ring)
    necklace = Necklace(31.5, 43, 13, "крабик")
    print(necklace)
    necklace1 = necklace.add_accessory(2)
    print(necklace1)

    pass
