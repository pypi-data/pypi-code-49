# ПРИМЕР СМЕНЫ АДРЕСА МОДУЛЯ:

# Подключаем библиотеку для работы с датчиком температуры и влажности
from pyiArduinoI2Cencoder import *
import sys

# Объявляем объект module для работы с функциями и методами библиотеки pyiArduinoI2Cencoder.
# Если при объявлении объекта указать адрес, например, module(0x0B),
# то пример будет работать с тем модулем, адрес которого был указан.
module = pyiArduinoI2Cencoder(None, NO_BEGIN)

# Если сценарию не были переданы аргументы
if len(sys.argv) < 2:
    # Назначаем модулю адрес (0x07 < адрес < 0x7F).
    newAddress = 0x09

# Иначе
else:
    # Новый адрес - первый аргумент
    newAddress = int(sys.argv[1])

# Если датчик найден
if module.begin():
    print("Найден датчик %#.2x" % module.getAddress())

    # Если адрес удалось изменить
    if module.changeAddress(newAddress):
            print("Адрес изменён на %#.2x" % module.getAddress())

    else:
            print("Адрес не изменён!")

else:
    print("Датчик не найден!")
