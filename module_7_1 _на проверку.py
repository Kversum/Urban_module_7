'''
Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать
 следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены
 запятой с пробелами.
Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую
 строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product. Добавляет в
 файл __file_name каждый продукт из products, если его ещё нет в файле (по полю name И по полю category). Если такой
 продукт уже есть, то увеличивает общий вес и выводит строку 'Продукт <название> уже был в магазине, его общий вес
 теперь равен <вес>.
Пример результата выполнения программы:
Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
s1.add(p1, p2, p3)
print(s1.get_products())

Вывод на консоль:
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Продукт Potato уже был в магазине, его общий вес теперь равен 56.0
Как выглядит файл после запусков (см. файл домашнего задания)

Примечания:
Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
При проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
Не забывайте закрывать файл вызывая метод close() у объектов файла.
'''
class Product:
    def __init__(self, name, weight, category):
        self.name = name          # - название продукта (строка)
        self.weight = weight      # общий вес товара (дробное число) (5.4, 52.8 и т.п.)
        self.category = category  # категория товара (строка)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.__file = open(self.__file_name, 'a+')

    def get_products(self):
        self.__file.seek(0)
        return self.__file.read()

    def add(self, *products):
        mach_products = {}
        file = open(self.__file_name, 'r')
        for line in file:
            name, weight, category = line.strip().split(', ')
            mach_products[(name, category)] = weight
        file.close()
        file = open(self.__file_name, 'a')
        for product in products:
            key = (product.name, product.category)
            if key in mach_products:
                mach_products[key] += product.weight
                print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {mach_products[key]}.')
            else:
                mach_products[key] = product.weight
                print(product)
        for (name, category), weight in mach_products.items():
            self.__file.write(f'{name}, {weight}, {category}\n')
        file.close()


s1 = Shop()
p1 = Product('Картофель', 50.5, 'Овощи')
p2 = Product('Макароны', 3.4, 'Бакалея')
p3 = Product('Картофель', 5.5, 'Овощи')

s1.add(p1, p2, p3)

print(s1.get_products())

