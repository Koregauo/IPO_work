class Rub(object):#создание класса рубли
    """ Класс для работы с рублями и копейками."""
    def __init__(self, rub=0, kop=0):#инициализация двух полей
        self.rub = rub
        self.kop = kop
    def __str__(self):#возвращает строковое представление объекта в формате - rub.kop rub
        if self.kop < 10:
            kop_str = '0' + str(self.kop)
        else:
            kop_str = str(self.kop)
        return f'{self.rub}.{kop_str} rub'
    def __lt__(self, other):#позволяет сравнивать объекты типа Rub, возвращает True, если текущий объект меньше объекта other и False в противном случае
        if self.rub < other.rub:
            return True
        elif self.rub == other.rub and self.kop < other.kop:
            return True
        else:
            return False
    def __add__(self, other):#метод, который слаживает рубли к рублям,копеёку к копейке
        #а если копеек 100, то ообнуляет их и переводит в 1 рубль
        total_rub = self.rub + other.rub
        total_kop = self.kop + other.kop
        if total_kop >= 100:
            total_rub += 1
            total_kop -= 100
        return Rub(total_rub, total_kop)
class Goods(object):#создание класса товара
    """ Класс описания товара: название и цена"""
    def __init__(self, name='', rub=0, kop=0):#инициализация 3 полей
        self.name = name
        self.price = Rub(rub, kop)
#создаются создаём список студента и общую стоимость его обедпаа
student_orders = []
total_cost = Rub()
#вводим товар и его стоимость, которые добавляются в список студента
#если выход, то прерываем и считаем итоги, иначе
while True:
    order = input('Введите товар и стоимость как - название rrr.kk rub ')
    if order == 'выход':
        break
    else:
        name, price_str = order.split()
        rub_str, kop_str = price_str.split('.')
        rub = int(rub_str)
        kop = int(kop_str)
        student_orders.append(Goods(name, rub, kop))
        total_cost += Rub(rub, kop)
# Сортировка товаров
student_orders.sort(key=lambda x: x.price, reverse=True)
# Вывод списка товаров и их стоимости
for goods in student_orders:
    print(f'{goods.name}: {goods.price}')
print(f'Общая стоимость обеда: {total_cost}')#вывод общей стоимостм
