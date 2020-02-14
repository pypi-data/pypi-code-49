# ПРИМЕР ЧТЕНИЯ ТАКТОВ ПОВОРОТА ЭНКОДЕРА:

from time import sleep

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *
# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

print("Вращайте барабан!")

while True:
    # Считываем такты поворота энкодера:
    turn = enc.getEncoder(ENC_TURN)

    # Выводим считанные данные:
    if turn is not 0:
        print(turn)

    # Без задержки в stdout будут появляться только ±1.
    sleep(.1)
