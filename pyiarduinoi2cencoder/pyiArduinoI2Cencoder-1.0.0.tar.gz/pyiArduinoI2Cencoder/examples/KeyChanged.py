#   ПРИМЕР ФИКСИРУЕТ СМЕНУ СОСТОЯНИЯ КНОПКИ:
# В stdout будет выводится сообщения при
# каждом нажатии и отпускании кнопки.

from time import sleep

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *
# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

print("Нажмите на вал")

while True:
    # Фиксируем смену состояния кнопки:
    # Если состояние кнопки изменилось, то ...
    if enc.getButton(KEY_CHANGED):
        # выводим сообщение в stdout
        print("Click")

    sleep(.1)
