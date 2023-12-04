class InternetShop:#создание родительского класса интернет ммагазин
    def __init__(self, shop_name, product_name, country, payment_method, purchase_amount, sale_date, customer_name):#инициализация его полей
        self.shop_name = shop_name
        self.product_name = product_name
        self.country = country
        self.payment_method = payment_method
        self.purchase_amount = purchase_amount
        self.sale_date = sale_date
        self.customer_name = customer_name
    def info(self):#метод по выводу информации
        print('название магазина:', self.shop_name)
        print('название продукта:', self.product_name)
        print('страна:', self.country)
        print('вид оплаты:', self.payment_method)
        print('сумма покупки:', self.purchase_amount)
        print('дата продажи:', self.sale_date)
        print('имя покупателя:', self.customer_name)
class LivingRoomFurniture(InternetShop):#создание дочернего классамебель для гостиных
    def __init__(self, shop_name, product_name, country, payment_method, purchase_amount, sale_date, customer_name,
    furniture_type, manufacturer, price):#инициализация полей
        super().__init__(shop_name, product_name, country, payment_method, purchase_amount, sale_date, customer_name)#наследование от родительского класса интернет магазин
        self.furniture_type = furniture_type
        self.manufacturer = manufacturer
        self.price = price
    def info(self):#метод по выводу информации
        super().info()#наследование информации
        print('тип мебели:', self.furniture_type)
        print('производитель:', self.manufacturer)
        print('цена:', self.price)
class KitchenFurniture(InternetShop):#создание дочернего класса мебель для кухни
    def __init__(self, shop_name, product_name, country, payment_method, purchase_amount, sale_date, customer_name,
    length, height, width, material, price):#инициализация полей
        super().__init__(shop_name, product_name, country, payment_method, purchase_amount, sale_date, customer_name)#наследование от родительского класса интернет магазин
        self.length = length
        self.height = height
        self.width = width
        self.material = material
        self.price = price
    def info(self):#метод по выводу инфлрмации
        super().info()#наследование информации род класса
        print('длинна:', self.length)
        print('высота:', self.height)
        print('ширина:', self.width)
        print('материал:', self.material)
        print('цена:', self.price)
class BathroomFurniture(InternetShop):#создание дочернего класса мебель для ванн
    def __init__(self, shop_name, product_name, country, payment_method, purchase_amount, sale_date, customer_name,
    price):#инициализация полей класса
        super().__init__(shop_name, product_name, country, payment_method, purchase_amount, sale_date, customer_name)#наследование от родительского класса интернет магазин
        self.price = price
    def info(self):#метод по выводу информации
        super().info()#наследование информации
        print('цена:', self.price)
        #создание обектов классов
living_room_furniture = LivingRoomFurniture('Просто мебель', 'диван', 'Китай', 'Credit Card', 2500, '2007.10.02',
'Вил Смит', 'угловой диван', 'Золотые руки', 899)
kitchen_furniture = KitchenFurniture('Просто мебель', 'Обеденны столик', 'АмЭрика', 'PayPal', 1500, '2011.11.22',
'Граб Джош', 200, 100, 80, 'древесина', 599)
bathroom_furniture = BathroomFurniture('Просто мебель', 'Туалетный шкаф', 'Италия', 'Bank Transfer', 800, '2019.09.17',
'Абрак Лори', 1399)
#вывод информации
living_room_furniture.info()
print('\n')#для красивогоо отступа
kitchen_furniture.info()
print('\n')#для красивого отступа
bathroom_furniture.info()