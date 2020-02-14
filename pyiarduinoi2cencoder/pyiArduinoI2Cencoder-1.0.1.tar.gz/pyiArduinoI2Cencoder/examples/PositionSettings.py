# ПРИМЕР НАСТРОЙКИ ПОКАЗАНИЙ ПОЗИЦИИ ВАЛА:

from time import sleep

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *

# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

# Инициируем работу с энкодером.
enc.begin()
# Указываем считать до 5 полных оборотов, без отрицательных значений.
enc.setPosSettings(5, False)

while True:

    p = enc.getPosition()
    # Выводим текущую позицию вала энкодера.
    print(p)
    sleep(.5)

