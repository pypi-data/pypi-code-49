# ПРИМЕР СБРОСА ТЕКУЩЕЙ ПОЗИЦИИ ВАЛА ЭНКОДЕРА:

from time import sleep

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *

# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)
enc.invEncoder(True)
f = False;

print("Вращайте вал по часовой стрелке, затем нажмите на вал")

while True:
    # Выводим текущую позицию вала энкодера.
    p = enc.getPosition()
    if p > 0:
        f = True;

    if f:
        print(p)

    # Если нажата кнопка энкодера
    if enc.getButton(KEY_PUSHED):
        # Сбрасываем позицию вала в 0:
        enc.resPosition()

    sleep(.1)
