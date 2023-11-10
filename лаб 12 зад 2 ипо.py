class MilitaryAircraft:
    """Класс, описывающий военные воздушные суда"""
    def __init__(self, name=None, aircraft_type=None, max_speed=None, max_altitude=None, weapon_type=None, capacity=None):
        """Конструктор, выполняющий инициализацию атрибутов"""
        self.name = name
        self.aircraft_type = aircraft_type
        self.max_speed = max_speed
        self.max_altitude = max_altitude
        self.weapon_type = weapon_type
        self.capacity = capacity
    def get_name(self):
        """Возвращает название военного воздушного судна"""
        return self.name
    def get_aircraft_type(self):
        """Возвращает тип военного воздушного судна"""
        return self.aircraft_type
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
        self.name = new_name

    def set_aircraft_type(self, new_aircraft_type):
        """Устанавливает новый тип военного воздушного судна"""
        self.aircraft_type = new_aircraft_type

    def set_max_speed(self, new_max_speed):
        """Устанавливает новую максимальную скорость военного воздушного судна"""
        self.max_speed = new_max_speed

    def set_max_altitude(self, new_max_altitude):
        """Устанавливает новую максимальную высоту полета военного воздушного судна"""
        self.max_altitude = new_max_altitude

    def set_weapon_type(self, new_weapon_type):
        """Устанавливает новый тип оружия военного воздушного судна"""
        self.weapon_type = new_weapon_type

    def set_capacity(self, new_capacity):
        """Устанавливает новую вместимость военного воздушного судна"""
        self.capacity = new_capacity
#всё выше почти как в просшлой лабе, но здесь инициализация через сеттеры
#ниже у нас идёт функция деструктора и вывод сообщения о его выполнении
    def __del__(self):
        """Деструктор"""
        print('Деструктор выполнился')
#создание пустого списка и добавление в него техники и информации о ней, которую ввёл пользователь
aircraft_list=[]
for i in range(10):
    name=input('Введите название военного воздушного судна  ')
    aircraft_type=input('Введите тип военного воздушного судна  ')
    max_speed=int(input('Введите максимальную скорость военного воздушного судна  '))
    max_altitude=int(input('Введите максимальную высоту полета военного воздушного судна  '))
    weapon_type=input('Введите тип оружия военного воздушного судна  ')
    capacity=int(input('Введите вместимость военного воздушного судна  '))
    aircraft=MilitaryAircraft(name, aircraft_type, max_speed, max_altitude, weapon_type, capacity)
    aircraft_list.append(aircraft)
#вывод всей техники
for aircraft in aircraft_list:
    print('Название ', aircraft.get_name())
    print('Тип ', aircraft.get_aircraft_type())
    print('Максимальная скорость ', aircraft.get_max_speed())
    print('Максимальная высота полета ', aircraft.get_max_altitude())
    print('Тип оружия ', aircraft.get_weapon_type())
    print('Вместимость ', aircraft.get_capacity())
    print()
del aircraft_list#вроде как вызов деструктора и удаление листа из памяти
