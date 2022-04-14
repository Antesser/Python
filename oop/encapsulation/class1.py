#from tkinter import Tk, Tk #библиотека для создания gui - оконных приложений
"объект - единица информации в памяти"
"экземпляр - конкретный объект какого-то класса"
"класс - инструкция по созданию объектов определённого типа"
"метод - функция в классе для воздействия на объект"
"переменные в классе - это поля или свойства"
"атрибуты - все имена в классе: переменных и методов"
class Purse:

    # def show(self,name="Unknown"):#в параметр self передаётся имя переменной x, в которой запущен класс, это нужно, чтобы разделять объекты, с которыми работает метод в данный момент
    #     print("hello " + name)

    def __init__(self, currency, owner = "Unknown"):#__init__ перегруженный оператор, конструктор объекта, код внутри этого метода исполняется, когда создаётся экземпляр какого-то класса
        if currency not in ("USD", "EUR"):
            raise ValueError
        self.__money = 0.00 #переменная money становится свойством экземпляра x при добавлении self, __ два нижних подчёркивания - сильная инкапсуляция, _ одно - мягкая
        self.currency = currency
        self.name = owner

    def top_up_balance(self, quantity):
        self.__money = self.__money + quantity
        return quantity  

    def top_down_balance(self, quantity):
        if self.__money - quantity < 0:
            print("Not enough money")
            raise ValueError ("Not enough money")
        self.__money = self.__money - quantity
        return quantity    

    def info(self):
        print(self.__money)

    def __del__(self):#код исполнится во время удаления объекта
        print("Wallet has been deleted")
        #return self.money


x = Purse("USD")
y = Purse("USD", "Lion")
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))
x.info()
y.info()
#del x #код исполнится дважды, 1 раз при вызове метода del, второй раз по завершении программы
