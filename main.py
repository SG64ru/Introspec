from inspect import getmodule


class Int_In:
    def inrospection_info(obj):
        print("Тип для obj = ", type(obj))
        print("Атрибуты и методы для obj = ", dir(obj))
        print("Модуль для obj = ", getmodule(obj))
        print("Отнесение к типу str для obj = ", isinstance(obj, str))
        print("Отнесение к типу int для obj = ", isinstance(obj, int))
        print("Проверка вызываемости атрибута ", callable(obj))
        print("id атрибута", id(obj))





    jjj = inrospection_info(10)

    print("Тип для функции = ", type(inrospection_info))
    print("Атрибуты и методы для функции = ", dir(inrospection_info))
    print("Модуль для функции = ", getmodule(inrospection_info))
    print("Отнесение к типу str для функции = ", isinstance(inrospection_info, str))
    print("Отнесение к типу int для функции = ", isinstance(inrospection_info, int))
    print("Проверка вызываемости функции ", callable(inrospection_info))
    print("id функции", id(inrospection_info))

    print("Тип для переменной функции = ", type(jjj))
    print("Атрибуты и методы для переменной функции = ", dir(jjj))
    print("Модуль для переменной функции = ", getmodule(jjj))
    print("Отнесение к типу str для переменной функции = ", isinstance(jjj, str))
    print("Отнесение к типу int для переменной функции = ", isinstance(jjj, int))
    print("Проверка вызываемости переменной функции ", callable(jjj))
    print("id переменной функции", id(jjj))


print("Class =", type(Int_In))
print("Тип для класса = ", type(Int_In))
print("Атрибуты и методы для класса = ", dir(Int_In))
print("Модуль для класса = ", getmodule(Int_In))
print("Отнесение к типу str для класса = ", isinstance(Int_In, str))
print("Отнесение к типу int для класса = ", isinstance(Int_In, int))
print("Проверка вызываемости класса ",callable(Int_In))
print("id класса", id(Int_In))
print(hasattr(Int_In, "obj"))

