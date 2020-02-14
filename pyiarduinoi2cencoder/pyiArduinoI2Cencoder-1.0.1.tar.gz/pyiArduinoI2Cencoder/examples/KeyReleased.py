#   ДАННЫЙ ПРИМЕР ФИКСИРУЕТ ОТПУСКАНИЕ КНОПКИ:
# При каждом отпускании кнопки, будет выводится
# сообщение в stdout

from time import sleep
# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *
# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

print("Нажмите на вал")

while True:

    # Если кнопка энкодера отпускается, то ...
    if enc.getButton(KEY_RELEASED):
        # Выводим текст в stdout
        print("Click")

    sleep(.1)
