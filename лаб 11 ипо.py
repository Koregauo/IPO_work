class Militaryaircraft:#создание класса
    """Класс, описывающий военные воздушные суда"""
    def __init__(self, name, type, max_speed, max_altitude, weapon_type, capacity):#инициализация атрибутов
        self.name=name
        self.type=type
        self.max_speed=max_speed
        self.max_altitude=max_altitude
        self.weapon_type=weapon_type
        self.capacity=capacity

    def get_name(self):
        """Возвращает название военного воздушного судна"""
        return self.name

    def get_type(self):
        """Возвращает тип военного воздушного судна"""
        return self.type

    def get_max_speed(self):
        """Возвращает максимальную скорость военного воздушного судна"""
        return self.max_speed

    def get_max_altitude(self):
        """Возвращает максимальную высоту полета военного воздушного судна"""
        return self.max_altitude

    def get_weapon_type(self):
        """Возвращает тип оружия военного воздушного судна"""
        return self.weapon_type

    def get_capacity(self):
        """Возвращает вместимость военного воздушного судна"""
        return self.capacity

    def set_name(self, new_name):
        """Устанавливает новое название военного воздушного судна"""
        self.name=new_name

    def set_type(self, new_type):
        """Устанавливает новый тип военного воздушного судна"""
        self.type=new_type

    def set_max_speed(self, new_max_speed):
        """Устанавливает новую максимальную скорость военного воздушного судна"""
        self.max_speed=new_max_speed

    def set_max_altitude(self, new_max_altitude):
        """Устанавливает новую максимальную высоту полета военного воздушного судна"""
        self.max_altitude=new_max_altitude

    def set_weapon_type(self, new_weapon_type):
        """Устанавливает новый тип оружия военного воздушного судна"""
        self.weapon_type=new_weapon_type

    def set_capacity(self, new_capacity):
        """Устанавливает новую вместимость военного воздушного судна"""
        self.capacity=new_capacity
help(Militaryaircraft)#извлечение документации


aircraft1=Militaryaircraft('F-22 Raptor', 'Истребитель', 2410, 19812, 'Ракеты, бомбы', 1)
aircraft2=Militaryaircraft('Su-35', 'Истребитель', 2400, 18000, 'Ракеты, бомбы, пушка', 1)
aircraft3=Militaryaircraft('B-2 Spirit', 'Стратегический бомбардировщик', 1010, 15700, 'Бомбы', 2)
aircraft4=Militaryaircraft('AH-64 Apache', 'Ударный вертолет', 293, 6100, 'Ракеты, пулеметы', 2)
aircraft5=Militaryaircraft('C-130 Hercules', 'Транспортный самолет', 592, 10000, 'Отсутствует оружие', 92)
