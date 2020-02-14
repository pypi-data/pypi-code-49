#   ДАННЫЙ ПРИМЕР ФИКСИРУЕТ НАЖАТИЕ КНОПКИ:
# При каждом нажатии кнопки, будет выводится
# сообщение в stdout

from time import sleep
# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *
# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

print("Нажмите на вал")

while True:
    #  Фиксируем событие нажатия кнопки:
    # Если кнопка энкодера нажимается, то ...
    if enc.getButton(KEY_PUSHED):

        # Выводим текст в stdout
        print("test")

    sleep(.1)
